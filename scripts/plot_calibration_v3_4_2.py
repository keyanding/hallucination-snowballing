"""Plot frozen v3.4.2 results without running or selecting model conditions."""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

root=Path(__file__).resolve().parents[1]
out=root/'results/calibration_v3_4_2'
metrics=json.loads((out/'metrics.json').read_text(encoding='utf-8'))
fig,axes=plt.subplots(1,3,figsize=(12,4),layout='constrained')
for ax,field,title,cmap in zip(axes,['ER','GM','NBF'],['C error rate','Median gold margin (nats/token)','Near-boundary fraction'],['YlOrRd','RdBu','YlOrRd']):
    values=np.array([[metrics['development'][f'D{d}B{b}'][field] if field=='GM' else metrics['development'][f'D{d}B{b}'][field]['rate'] for b in range(3)] for d in range(1,5)])
    bounds={'vmin':0,'vmax':1} if field!='GM' else {'vmin':-max(float(np.abs(values).max()),1),'vmax':max(float(np.abs(values).max()),1)}
    im=ax.imshow(values,cmap=cmap,aspect='auto',**bounds)
    for i in range(4):
        for j in range(3):
            ax.text(j,i,f'{values[i,j]:.2f}' if field=='GM' else f'{values[i,j]:.1%}',ha='center',va='center',color='black',bbox=dict(facecolor='white',edgecolor='none',alpha=.8,pad=2))
    ax.set_xticks([0,1,2],['0','1','2'])
    ax.set_yticks([0,1,2,3],['1','2','3','4'])
    ax.set_xlabel('Competing branches')
    ax.set_ylabel('Composition depth')
    ax.set_title(title,fontsize=11)
    fig.colorbar(im,ax=ax,shrink=.85)
fig.suptitle('Qwen3-4B NF4/BF16 — frozen development grid (8 paired cases/cell)',fontsize=13)
fig.savefig(out/'development_grid.png',dpi=180)
fig.savefig(out/'development_grid.svg')
plt.close(fig)
