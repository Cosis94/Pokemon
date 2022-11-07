import pandas as pd
Full_List = []
with open ("Pokedex.txt", "r") as f:
    lines = f.readlines()[24:]
    for elements in lines:
        Full_List.append(elements.split())

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
#1 Nummer

#print(df)
#df.to_excel("Pokedex.xlsx")

for x in selected_List:
    if len(x) != 23:
        print(len(x))