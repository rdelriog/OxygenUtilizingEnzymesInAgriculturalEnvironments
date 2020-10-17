import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

filepath = "" #Filepath here
df = pd.read_csv(filepath)
agricultured=[]
natural=[]
contaminated=[]
fig=[]
for i, row in df.iterrows():
    df_sub =df[i:i+1]
    MGNIFY= row['MGnify assignment']
    num_ECPer_num_org=row['num_ec_per_organism']
    if MGNIFY=='agricultured':
        agricultured.append( num_ECPer_num_org)
    if  MGNIFY=='contaminated':
        contaminated.append(num_ECPer_num_org)
    if MGNIFY=='natural':
        natural.append(num_ECPer_num_org)

colors = ['#E69F00', '#56B4E9', '#F0E442']
names = ['natural', 'contaminated', 'agricultured']

c=pd.Series(natural)

plt.hist([natural, contaminated, agricultured], bins = int(180/15), normed=True,color = colors, label=names)                 
sns.distplot([natural],bins = int(180/15), hist = False, kde = True,kde_kws = {'linewidth': 3},label =names[0],color=colors[0])
sns.distplot([contaminated],bins = int(180/15) ,hist = False, kde = True,kde_kws = {'linewidth': 3},label =names[1],color=colors[1],)
sns.distplot([agricultured],bins = int(180/15) ,hist = False, kde = True,kde_kws = {'linewidth': 3},label =names[2],color=colors[2])
plt.legend()
plt.xlabel('num_ec/num_organs')
plt.ylabel('frequency')
plt.title('histogram of the number of oxygen utilizing enzyme per organism')      

    
