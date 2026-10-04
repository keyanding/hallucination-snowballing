"""Plot recorded counterbalanced order effects; never runs the model."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

root=Path(__file__).resolve().parents[1]
out=root/'results/calibration_v3_4_3'
m=json.loads((out/'metrics.json').read_text(encoding='utf-8'))
fig,axes=plt.subplots(1,3,figsize=(12,4),layout='constrained')
colors=['#277da8','#f8961e','#a84469']
x=np.arange(1,5)
for offset,(difficulty,s) in enumerate(m['by_difficulty'].items()):
    xs=x+(offset-1)*.24
    axes[0].bar(xs,[s['PSR'][str(p)]['rate'] for p in x],width=.23,color=colors[offset],label=difficulty)
    axes[1].bar(xs,[s['GPA'][str(p)]['rate'] for p in x],width=.23,color=colors[offset])
    axes[2].plot(x,[s['delta_by_position'][str(p)]['mean'] for p in x],marker='o',color=colors[offset],label=difficulty)
axes[0].axhline(.25,color='gray',linestyle='--',linewidth=1)
axes[2].axhline(0,color='gray',linestyle='--',linewidth=1)
for ax in axes:
    ax.set_xticks(x)
    ax.set_xlabel('Candidate answer-list position')
    ax.spines[['top','right']].set_visible(False)
axes[0].set_title('Position selection rate')
axes[1].set_title('Accuracy by gold position')
axes[2].set_title('Identity-matched score shift')
axes[0].set_ylim(0,1)
axes[1].set_ylim(0,1)
axes[0].set_ylabel('Proportion (descriptive)')
axes[2].set_ylabel('Mean Delta (nats/token)')
axes[0].legend(frameon=False,fontsize=8)
fig.suptitle('v3.4.3: six cases, three conditions, four fixed rotations per set',fontsize=12)
fig.savefig(out/'position_controls.png',dpi=180)
fig.savefig(out/'position_controls.svg')
plt.close(fig)
