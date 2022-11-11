import pandas as pd
import re

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
            
selected_List[0].pop(1)
selected_List[0].pop(1)
#print(selected_List[0])
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

#dataframe_24 
df_24 = pd.DataFrame(List_24)
#dataframe_25
df_25 = pd.DataFrame(List_25)
#dataframe_26 
df_26 = pd.DataFrame(List_26)

#print(df)

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
df_rest = df[df["Bool"]==1]



print(len(df_rest))
