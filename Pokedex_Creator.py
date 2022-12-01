import pandas as pd
import re
import numpy as np

Full_List = []
with open ("Pokedex.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()[24:]
    for elements in lines:
        Full_List.append(elements.split())


List_22 = []
List_23 = []
List_24 = []
List_25 = []
List_26 = []
selected_List = []

for x in Full_List:
    if "Fußnoten" in x:
        break
    else:
        if len(x)==1:
            continue
        else:
            selected_List.append(x)

##########################
#Correct the first entry    
selected_List[0].pop(1)
selected_List[0].pop(1)
##########################

#Ausgangs DataFrame df
df = pd.DataFrame(data=selected_List)
df = df[[1,8,10,12,14,22]]
df = df.reset_index()

#1 Nummer

#df.to_excel("Pokedex.xlsx")


#Listen Creator with all not OK List Values
new_List = []
count = 0
for x in selected_List:
    if len(x) == 22:
        List_22.append(x)
    if len(x) == 24:
        List_24.append(x)
    if len(x) == 25:
        List_25.append(x)
    if len(x) == 26:
        List_26.append(x)



#dataframe_22 
df_22 = pd.DataFrame(List_22)
df_22 = df_22.replace("||", "")
df_22 = df_22.replace("|", "")
df_22 = df_22.replace('style="height:',"")
df_22 = df_22.replace('28px;"',"")
df_22 = df_22.replace('<span',"")
df_22 = df_22.replace([".+span>"],"",regex=True)
df_22 = df_22.replace(["Tran.+"],"",regex=True)
df_22 = df_22.replace(['.+Datei.+'],"",regex=True)
df_22 = df_22.replace(['.+icon.+'],"",regex=True)
df_22 = df_22.replace(['.+link.+'],"",regex=True)
df_22 = df_22.replace(['.+früher.+'],"",regex=True)
df_22 = df_22.replace(['Mr.'],"",regex=True)
df_22 = df_22.replace(['Jr.'],"",regex=True)
df_22 = df_22.replace(['M.$'],"",regex=True)
df_22 = df_22.replace('/',"")
df_22 = df_22[df_22!=""]
df_22 = df_22.dropna(axis=1, how='all')
df_22 = df_22.replace("[NaN]","",regex=True)
#print(df_22) 


#dataframe_24 
df_24 = pd.DataFrame(List_24)
df_24 = df_24.replace("||", "")
df_24 = df_24.replace("|", "")
df_24 = df_24.replace('style="height:',"")
df_24 = df_24.replace('28px;"',"")
df_24 = df_24.replace('<span',"")
df_24 = df_24.replace([".+span>"],"",regex=True)
df_24 = df_24.replace(["Tran.+"],"",regex=True)
df_24 = df_24.replace(['.+Datei.+'],"",regex=True)
df_24 = df_24.replace(['.+icon.+'],"",regex=True)
df_24 = df_24.replace(['.+link.+'],"",regex=True)
df_24 = df_24.replace(['.+früher.+'],"",regex=True)
df_24 = df_24.replace(['Mr.'],"",regex=True)
df_24 = df_24.replace(['Jr.'],"",regex=True)
df_24 = df_24.replace(['M.$'],"",regex=True)
df_24 = df_24.replace('/',"")
df_24 = df_24[df_24!=""]
df_24 = df_24.dropna(axis=1, how='all')
df_24 = df_24.replace("[NaN]","",regex=True)
#print(df_24) 

#dataframe_25
df_25 = pd.DataFrame(List_25)
df_25 = df_25.replace("||", "")
df_25 = df_25.replace("|", "")
df_25 = df_25.replace('style="height:',"")
df_25 = df_25.replace('28px;"',"")
df_25 = df_25.replace('<span',"")
df_25 = df_25.replace([".+span>"],"",regex=True)
df_25 = df_25.replace(["Tran.+"],"",regex=True)
df_25 = df_25.replace(['.+Datei.+'],"",regex=True)
df_25 = df_25.replace(['.+icon.+'],"",regex=True)
df_25 = df_25.replace(['.+link.+'],"",regex=True)
df_25 = df_25.replace(['.+früher.+'],"",regex=True)
df_25 = df_25.replace(['Mr.$'],"",regex=True)
df_25 = df_25.replace(['Jr.$'],"",regex=True)
df_25 = df_25.replace(['M.$'],"",regex=True)
df_25 = df_25.replace('/',"")
df_25 = df_25[df_25!=""]
df_25 = df_25.dropna(axis=1, how='all')
df_25 = df_25.replace("[NaN]","",regex=True)
#print(df_25) 


#dataframe_26 
df_26 = pd.DataFrame(List_26)
df_26 = df_26.replace("||", "")
df_26 = df_26.replace("|", "")
df_26 = df_26.replace('style="height:',"")
df_26 = df_26.replace('28px;"',"")
df_26 = df_26.replace('<span',"")
df_26 = df_26.replace([".+span>"],"",regex=True)
df_26 = df_26.replace(["Tran.+"],"",regex=True)
df_26 = df_26.replace(['.+Datei.+'],"",regex=True)
df_26 = df_26.replace(['.+icon.+'],"",regex=True)
df_26 = df_26.replace(['.+link.+'],"",regex=True)
df_26 = df_26.replace(['.+früher.+'],"",regex=True)
df_26 = df_26.replace(['Mr.'],"",regex=True)
df_26 = df_26.replace(['Jr.'],"",regex=True)
df_26 = df_26.replace(['M.$'],"",regex=True)
df_26 = df_26.replace('/',"")
df_26 = df_26[df_26!=""]
df_26 = df_26.dropna(axis=1, how='all')
df_26 = df_26.replace("[NaN]","",regex=True)
#print(df_26) 




#Unterteilung in 3 Fälle
df_22_1 = df_22[df_22[1]=="???"]
df_22_1 = df_22_1.dropna(axis=1, how='all')

df_22_2 = df_22[df_22[1].isna()]
df_22_2 = df_22_2.dropna(axis=1, how='all')

df_22_3 = df_22[df_22[1]!="???"]
df_22_3 = df_22_3[df_22_3[1].notna()]
df_22_3 = df_22_3.dropna(axis=1, how='all')
#print(df_22_2)
#print(df_22_1)
#print(df_22_3)

#Final für df_22
df_22_final = df_22_3[df_22_3.columns[[0,1,2,3,4,-1]]]

######################################################################

df_24_1 = df_24[df_24[1]=="???"]
df_24_1 = df_24_1.dropna(axis=1, how='all')
df_24_1 = df_24_1[df_24_1.columns[[0,1,2,3,4,-1]]]

df_24_2 = df_24[df_24[1].isna()]
df_24_2 = df_24_2.dropna(axis=1, how='all')

df_24_3 = df_24[df_24[1]!="???"]
df_24_3 = df_24_3[df_24_3[1].notna()]
df_24_3 = df_24_3.dropna(axis=1, how='all')
df_24_3 = df_24_3[df_24_3.columns[[0,1,3,4,5,-1]]]

#print(df_24_2)
#print(df_24_1)
#print(df_24_3)

#Final für df_24
df_24_3.columns = df_24_1.columns 
df_24_final = pd.concat([df_24_1,df_24_3],ignore_index=True,axis=0)

######################################################################

df_25_1 = df_25[df_25[1]=="???"]
df_25_1 = df_25_1.dropna(axis=1, how='all')

df_25_2 = df_25[df_25[1].isna()]
df_25_2 = df_25_2.dropna(axis=1, how='all')

df_25_3 = df_25[df_25[1]!="???"]
df_25_3 = df_25_3[df_25_3[1].notna()]
df_25_3 = df_25_3.dropna(axis=1, how='all')

#print(df_25_2)
#print(df_25_1)
#print(df_25_3)

#Final für df_25

######################################################################

df_26_1 = df_26[df_26[1]=="???"]
df_26_1 = df_26_1.dropna(axis=1, how='all')

df_26_2 = df_26[df_26[1].isna()]
df_26_2 = df_26_2.dropna(axis=1, how='all')

df_26_3 = df_26[df_26[1]!="???"]
df_26_3 = df_26_3[df_26_3[1].notna()]
df_26_3 = df_26_3.dropna(axis=1, how='all')
#print(df_26_2)
#print(df_26_1)
#print(df_26_3)

#Final für df_26

######################################################################

Liste_default = [re.sub(r'[0-9]*','', str(x)) for x in df[1]]

#print(Liste_default)
for x in range(0,len(Liste_default)):
    if Liste_default[x]=="":
        Liste_default[x] = 0
    else:
        Liste_default[x] = 1
#print(Liste_default)

df["Bool"] = Liste_default

df_final = df[df["Bool"]==0]
#df_rest = df[df["Bool"]==1]

#print(df_final)

















