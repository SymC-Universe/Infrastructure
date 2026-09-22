from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import andes

OUT=Path("research/CHI_CAPITALCHI_GRID_KUNDUR_G2_RESULT_20260922.json")
BAND=(0.15,1.00)
STATES={
"INTACT":[],
"N1_LINE4":["Line_4"],"N1_LINE5":["Line_5"],"N1_LINE6":["Line_6"],
"N2_LINE4_LINE5":["Line_4","Line_5"],"N2_LINE4_LINE6":["Line_4","Line_6"],
"N2_LINE5_LINE6":["Line_5","Line_6"],"LINE8_INTERNAL_OUT":["Line_8"]}

def fresh():
    ss=andes.load(andes.get_case("kundur/kundur_full.xlsx"),no_output=True)
    # disable source Toggle events before any outcome routine
    if len(ss.Toggle.idx.v):
        ss.Toggle.u.v[:] = 0
    return ss

def line_pos(ss,name):
    names=list(ss.Line.name.v)
    if name not in names: raise RuntimeError(f"missing line {name}")
    return names.index(name)

def set_out(ss,names):
    for n in names: ss.Line.u.v[line_pos(ss,n)]=0

def eig_state(name,outs):
    ss=fresh(); set_out(ss,outs)
    pf=bool(ss.PFlow.run())
    if not pf: return {"name":name,"pflow":False,"eig":False,"modes":[]}
    ok=bool(ss.EIG.run())
    vals=np.asarray(ss.EIG.mu)
    modes=[]
    if ok:
      for z in vals:
        a=float(np.real(z)); b=float(np.imag(z))
        if b<=0: continue
        f=b/(2*math.pi)
        if BAND[0]<=f<=BAND[1]:
          den=math.hypot(a,b)
          modes.append({"real":a,"imag":b,"frequency_hz":f,
                        "chi_mode":(-a/den if den else None)})
    modes.sort(key=lambda x:x["frequency_hz"])
    return {"name":name,"pflow":pf,"eig":ok,"modes":modes}

def assign(ref,test):
    # exhaustive permutation: Kundur band is small; avoids extra scipy dependency
    import itertools
    if len(ref)!=len(test): return None
    n=len(ref)
    if n==0:return []
    best=None
    for p in itertools.permutations(range(n)):
      cost=sum(abs(complex(test[p[i]]["real"],test[p[i]]["imag"])-
                   complex(ref[i]["real"],ref[i]["imag"]))/
               max(abs(complex(ref[i]["real"],ref[i]["imag"])),1e-12) for i in range(n))
      if best is None or cost<best[0]: best=(cost,p)
    return list(best[1])

def matched_delta(ref,test):
    p=assign(ref,test)
    if p is None:return None
    return [test[p[i]]["chi_mode"]-ref[i]["chi_mode"] for i in range(len(ref))]

def speed_gap(ss):
    # GENROU omega state addresses and source inertia M
    idx=list(ss.GENROU.idx.v); M=np.asarray(ss.GENROU.M.v,dtype=float)
    addrs=np.asarray(ss.GENROU.omega.a,dtype=int)
    t=np.asarray(ss.dae.ts.t,dtype=float)
    y=np.asarray(ss.dae.ts.y)
    w=y[:,addrs]
    a1=[i for i,x in enumerate(idx) if str(x) in ("1","2")]
    a2=[i for i,x in enumerate(idx) if str(x) in ("3","4")]
    g1=np.sum(w[:,a1]*M[a1],axis=1)/np.sum(M[a1])
    g2=np.sum(w[:,a2]*M[a2],axis=1)/np.sum(M[a2])
    return t,g1-g2

def rms(t,x,a,b):
    q=x[(t>=a)&(t<=b)]
    return float(np.sqrt(np.mean(q*q))) if len(q) else None

def peak(t,x,a,b):
    q=np.abs(x[(t>=a)&(t<=b)])
    return float(np.max(q)) if len(q) else None

def tds_run(label,line=None,reclose=False):
    ss=fresh()
    # add clean Toggle events rather than edit model parameters after initialization
    if line is not None:
      ss.add("Toggle",{"model":"Line","dev":line,"t":2.0})
      if reclose:ss.add("Toggle",{"model":"Line","dev":line,"t":4.0})
    if not ss.PFlow.run(): return {"label":label,"status":"PFLOW_FAIL"}
    ss.TDS.config.tf=10.0
    if not ss.TDS.run(): return {"label":label,"status":"TDS_FAIL"}
    t,g=speed_gap(ss)
    o={"label":label,"status":"PASS","n":int(len(t))}
    if line is None:
      o["rms_0_10"]=rms(t,g,0,10)
    elif reclose:
      pk=peak(t,g,2,4)
      o.update({"peak_abs_gap_2_4":pk,"post_reclose_peak_abs_gap_4_10":peak(t,g,4,10),
                "rms_gap_4_6":rms(t,g,4,6),"rms_gap_8_10":rms(t,g,8,10)})
      thresh=0.10*pk if pk is not None else None
      reclaim=None
      if thresh is not None:
        ids=np.where(t>=4)[0]
        for i in ids:
          j=np.searchsorted(t,t[i]+1.0,side="left")
          if j<len(t) and np.all(np.abs(g[i:j+1])<=thresh):
            reclaim=float(t[i]);break
      o["first_reclaim"]=reclaim
    else:
      o.update({"peak_abs_gap_2_10":peak(t,g,2,10),"rms_gap_2_5":rms(t,g,2,5),
                "rms_gap_7_10":rms(t,g,7,10),"rms_gap_8_10":rms(t,g,8,10)})
    return o

def main():
    ref1=eig_state("INTACT_REPEAT_1",[])
    ref2=eig_state("INTACT_REPEAT_2",[])
    drep=matched_delta(ref1["modes"],ref2["modes"])
    repeat_ok=drep is not None and ref1["pflow"] and ref1["eig"] and ref2["pflow"] and ref2["eig"]
    eps_chi=max(1e-8,100*max([abs(x) for x in drep],default=0.0)) if repeat_ok else None

    static={}
    for k,v in STATES.items(): static[k]=eig_state(k,v)
    n1=[]
    for k in ("N1_LINE4","N1_LINE5","N1_LINE6"):
      s=static[k]; d=matched_delta(static["INTACT"]["modes"],s["modes"])
      material=(d is None or (eps_chi is not None and max([abs(x) for x in d],default=0)>eps_chi))
      n1.append({"state":k,"matched_delta_chi":d,"material_modal_change":bool(material)})
    if not repeat_ok: sdisp="STATIC_TOPOLOGY_RESULT_UNRESOLVED"
    else:
      nm=sum(x["material_modal_change"] for x in n1)
      sdisp="TOPOLOGY_CONDITIONS_MODAL_CHI" if nm>=2 else "LOCAL_MODAL_INVARIANCE_IN_TESTED_N1_CORRIDOR"

    base=tds_run("INTACT_NO_EVENT")
    eps_rms=max(1e-10,100*base.get("rms_0_10",0.0)) if base["status"]=="PASS" else None
    permanent={}; temporary={}
    for line in ("Line_4","Line_5","Line_6","Line_8"):
      permanent[line]=tds_run("PERMANENT_"+line,line,False)
    for line in ("Line_4","Line_5","Line_6"):
      temporary[line]=tds_run("RECLOSE_"+line,line,True)
    rec=[]
    fail=False
    for line in ("Line_4","Line_5","Line_6"):
      p=permanent[line]; q=temporary[line]
      if p["status"]!="PASS" or q["status"]!="PASS": fail=True; imp=None; resolved=False
      else:
        imp=p["rms_gap_8_10"]-q["rms_gap_8_10"]
        resolved=bool(eps_rms is not None and imp>eps_rms)
      rec.append({"line":line,"late_rms_improvement":imp,"resolved":resolved})
    if fail:rdisp="RECOVERY_RESULT_UNRESOLVED"
    else:
      nr=sum(x["resolved"] for x in rec)
      rdisp=("TOPOLOGY_RESTORATION_CHANGES_REALIZED_RESPONSE" if nr==3 else
             "LINE_DEPENDENT_RECOVERY" if nr in (1,2) else
             "NO_RESOLVED_RECLAIM_INCREMENT_FROM_RECLOSURE")

    out={"schema":"SYMC_CHI_CAPITALCHI_GRID_KUNDUR_G2_V01","date":"2026-09-22",
      "status":"PASS" if repeat_ok and not fail else "PARTIAL_OR_REFUSED",
      "epistemic_class":"P0_D_CONTROLLED_NETWORK","promotion_effect":"NONE",
      "band_hz":list(BAND),"repeat":{"delta_chi":drep,"eps_chi":eps_chi,"ok":repeat_ok},
      "static_states":static,"n1_adjudication":n1,"static_disposition":sdisp,
      "tds_baseline":base,"eps_rms":eps_rms,"permanent":permanent,"temporary":temporary,
      "reclosure_adjudication":rec,"recovery_disposition":rdisp,
      "native_method_disposition":"STANDARD_TOOLKIT_SUBSUMES_MECHANISM"}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":main()
