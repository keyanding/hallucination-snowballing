"""Case-level descriptive figures; no changes to selection or experiment logs."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/calibration_v3_4_4'
m=json.loads((OUT/'metrics.json').read_text(encoding='utf-8'))
levels=m['cohorts']['development']
x=list(range(3)); labels=list(levels)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})
fig,axes=plt.subplots(1,3,figsize=(14,4.7),layout='constrained')
series=[ [('L: first option','L_first','#215a9b'),('R: earliest record','R_earliest','#ce6b22')],
         [('N: strict coverage','N_coverage','#318066'),('N: wrong / valid','N_wrong_given_valid','#a1455b')],
         [('L: identity changes','L_order_sensitive','#215a9b'),('R: identity changes*','R_order_sensitive_complete','#ce6b22')]]
for ax,items,title in zip(axes,series,['Selection by display position','Natural no-list outputs','Identity sensitivity across rotations']):
    for label,key,color in items:
        y=[levels[d][key]['rate'] for d in labels]
        ci=[levels[d]['case_bootstrap_95'][key] for d in labels]
        lo=[v-c['lower'] for v,c in zip(y,ci)]
        hi=[c['upper']-v for v,c in zip(y,ci)]
        ax.errorbar(x,y,yerr=[lo,hi],marker='o',capsize=4,label=label,color=color,lw=2)
    ax.set_xticks(x,labels);ax.set_ylim(-.03,1.03);ax.set_title(title,fontsize=11,fontweight='bold')
    ax.set_yticks([0,.25,.5,.75,1],['0%','25%','50%','75%','100%']);ax.grid(axis='y',alpha=.2);ax.legend(loc='best',fontsize=9)
axes[0].axhline(.25,color='#777777',ls=':',lw=1)
fig.suptitle('v3.4.4 | 24 new paired development cases',fontsize=15,fontweight='bold')
fig.supxlabel('95% percentile intervals resample cases, not rotations. *R sensitivity conditions on four strict-valid outputs.\nDepth, branch count and prompt length covary; these are descriptive construction settings.',fontsize=9)
fig.savefig(OUT/'interface_comparison.png',dpi=180)
fig.savefig(OUT/'interface_comparison.svg')
