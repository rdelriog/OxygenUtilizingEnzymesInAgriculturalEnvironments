import glob
import webbrowser
import urllib
from g_maps_link_generator import generate_google_maps_link
sample_ids=['']
a=open("data.tsv", "w")
b=open("number.tsv", "w")
#CALCULATE NUMBER OF EC 
sample_dict={}
times={}

GLOBAL_RESULTS=("C:\\Users\\admin\\Desktop\\DOCUMENTS FOR ISSI CODE\\results_table.tsv")	#FOLDER WITH RESULTS TABLE
with open(GLOBAL_RESULTS,'r') as lines:		
    for line in lines :
         splitted=line.split("\t")
         file_id=splitted[0]
         sap_id=file_id.split("_")[0]
         num_EC=int(splitted[1])
         EC_dia=splitted[2]
         
         if sap_id not in sample_dict:
             sample_dict[sap_id]=0
             sample_dict[sap_id]=num_EC
             times[sap_id]=1
             sample_ids.append(sap_id)
         else:
             sample_dict[sap_id]+=num_EC   
             times[sap_id]+=1
for sap_id in sample_dict:
	sample_dict[sap_id]=sample_dict[sap_id]/times[sap_id]
#CALCULATE NUMBER OF SEQUENCES						
print("stoop")
sample_ids2=['']
seq_dict={}
filepath_sequence = "";
FILE_SEQUENCE= (filepath_sequence)
with open(FILE_SEQUENCE, 'r') as lines:
	for line in lines:
		splitted=line.split("\n")
		split2=splitted[0].split()
		file_id=split2[0]
		sample_ids2.append(file_id)
		num_seq=split2[1]
		seq_dict[file_id]=num_seq

#CALCULATE THE PREDICTED NUMBER OF ORGANISMS
sample_ids3=['']
sample_id_organ={}
files= glob.glob("C:\\Users\\admin\\Desktop\\DOCUMENTS FOR ISSI CODE\\organisms\\*") 	#FOLDER ORGANISMS
for file in files:
	num_lines=0
	org = 0

	with open (file, 'r') as h:
		for line in h:
			num_lines+=1
			if num_lines==2:
				separado=line.split("\t")
				sample_id_org= separado[1]
				sample_ids3.append(sample_id_org)
			if num_lines>=3:
				separado= line.split("\t")
				org+=float(separado[1])
		sample_id_organ[sample_id_org]=org		

#CALCULATE TOTAL NUMBER OF ENZYMES

sample_ids4=['']
sample_id_enzymes={}
files= glob.glob("C:\\Users\\admin\\Desktop\\DOCUMENTS FOR ISSI CODE\\individual outputs\\*")
#FOLDER WITH INDIVIDUAL OUTPUTS

for enz_file in files:
	num_enzymes=0
	samp_id=enz_file.split("_")[0]
	samp_id=samp_id.split("\\")[6]
	with open(enz_file, 'r') as f:
		for linez in f:
			num_enzymes += 1
		

		if samp_id not in sample_id_enzymes:
			sample_id_enzymes[samp_id]=0
			sample_ids4.append(samp_id)
			sample_id_enzymes[samp_id]=num_enzymes-1
		else:
			sample_id_enzymes[samp_id]+=num_enzymes-1	

#OBTAIN GEOGRAPHIC INFORMATION

z=open("datatest.tsv", "w")
depth_dict={}
long_dict={}
lat_dict={}
nolines=0
idsample=''
depth=''
longitude=''
latitude=''
file=("C:\\Users\\admin\\Desktop\\DOCUMENTS FOR ISSI CODE\\samples_metadata.csv")
with open(file, 'r')as lines:
	for line in lines:
		nolines+=1
		if nolines>1:
			splitted=line.split(",")
			idsample=splitted[2]
			depth=splitted[-3]
			longitude=splitted[-2]
			latitude=splitted[-1]
			z.write(str(idsample)+ "\t"+ str(depth)+ "\t" + str(longitude) + "\t" + str(latitude.rstrip()))
			depth_dict[idsample]=depth
			long_dict[idsample]=longitude
			lat_dict[idsample]=latitude
			z.close

#DICTIONARIES FOR EVERY PART:

#EC= sample_dict
#SEQUENCES= seq_dict
#ORGANISMS= sample_id_organ
#ENZYMES= sample_id_enzymes
#DEPTH= depth_dict
#LONGITUDE= long_dict
#LATITUDE= lat_dict
'''
j=len(sample_ids)
k=len(sample_ids2)
l=len(sample_ids3)
m=len(sample_ids4)
n=[j,k,l,m]
n.sort()
lista=n[3]
if lista==j:
	sample_ids=sample_ids
if lista==k:
	sample_ids=sample_ids2
if lista==l:
	sample_ids=sample_ids3
if lista==m:
	sample_ids=sample_ids4
'''

default=0

sample_ids.sort()
aa=len(sample_ids)
urls=[]
for i in range (1, aa):
	idnow=sample_ids[i]
	if idnow in sample_dict:
		num_ec=sample_dict[idnow]
	else:
		num_ec=0

	if idnow in seq_dict:
		num_seq_file=	seq_dict[idnow]
	else:
		num_seq_file=1e900000000

	if idnow in sample_id_organ:
		num_organisms= sample_id_organ[idnow]
	else: 
		num_organisms=1e90000000

	if idnow in sample_id_enzymes:
		num_enzymes= sample_id_enzymes[idnow]
	else:
		num_enzymes=0

	if idnow in depth_dict:
		depthh= depth_dict[idnow]
	else:
		depthh=0

	if idnow in long_dict:
		longitudee= long_dict[idnow]
	else: 
		longitudee=0

	if idnow in lat_dict:
		latitudee=lat_dict[idnow].rstrip()
	else:
		latutudee=0
	
	#b.write(idnow + "\t" str(num_ec) +"\t" + str(num_enzymes) +"\t" + str(num_seq_file) +"\t" + str(num_organisms))	
	a.write(idnow + "\t" + str(num_ec)+ "\t" + str(float(num_ec)/730) + "\t" +
	str(float(num_ec)/float(num_seq_file))+"\t"+str(float(num_enzymes)/float(num_seq_file))+
	"\t"+str(float(num_ec)/float(num_organisms))+ "\t"+ str(depthh)+ "\t" + str(longitudee) +
	"\t" + str(latitudee) + "\n")
	url=str(generate_google_maps_link(latitudee, longitudee, 100))
	
	if url not in urls:
		#webbrowser.open(url)
		urls.append(url)
		b.write(url + "\n")
	

a.close
b.close


import plotly
import pandas as pd                     
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)
df = pd.read_csv("C:\\Users\\admin\\Desktop\\DOCUMENTS FOR ISSI CODE\\samples_metadata.csv")
df.head()

sample_ids=['']

df['text'] = df['run_id']+"\t"+df['sample name']+"\t"+df['biome']
colors = ["rgb(0,0,0)","rgb(247,255,0)","rgb(0,162,255)","rgb(255,255,255)","lightgrey"]
cities = []
scale = 5000
c=colors[1]


#contaminated=black
#permforst=yellow
#wetland=blue
#with out definition=white
for i, row in df.iterrows():
    df_sub =df[i:i+1]
    biome = row['biome']
    farme=biome.split(":")[-1]
    sample_id= row['run_id']
    #print(sample_id)
    if farme=='Contaminated':
        c=colors[0]
    elif farme=='Permafrost':
        c=colors[1]
    elif farme=='Wetlands':
        c=colors[2]
    else:
        c=colors[3]
    
    if sample_id in sample_dict:
    	num_EC=sample_dict[sample_id]
    else:
    	num_EC=0
    
    if sample_id in seq_dict:
    	num_seq=seq_dict[sample_id]
    else:
    	num_seq=1

    city = go.Scattergeo(
            lon = df_sub['longitude'],
            lat = df_sub['latitude'],
            text = df_sub['text'],
            marker = go.scattergeo.Marker(
                    
                    size=(int(num_EC)/int(num_seq)*10000),
                    color = c,
                    line = go.scattergeo.marker.Line(
                            width=0.5, color='rgb(255,65,54)'
                            ),
                            sizemode = 'area'
                            ),
                    name = '{}'.format(sample_id) )         
    cities.append(city)
    
    

layout = go.Layout(
        title = go.layout.Title(
            text = 'soil samples map'
        ),showlegend = True,
        geo = go.layout.Geo(
            scope = 'world',
            projection = go.layout.geo.Projection(
                type='natural earth'
            ),
            showland = True,
            landcolor = 'rgb(10, 81, 45)',
            #ubunitwidth=5,
            #countrywidth=5,
            #subunitcolor="rgb(0, 0, 255)",
            #countrycolor="rgb(0, 0, 255)"
        )
    )
                                                
                
fig = go.Figure(data=cities,layout=layout)
plotly.offline.plot(fig)

		

