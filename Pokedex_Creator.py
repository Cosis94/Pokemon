import pandas as pd
Full_List = []
with open ("Pokedex.txt", "r", encoding="utf-8") as f:
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
count = 0
new_List = []
for x in selected_List:
    if len(x) != 23:
       # print(x)
       # print(len(x))
        count +=1
       # print(count)
        new_List.append(x)

count = 0 
for x in new_List:
    print(x)

    count +=1
    print(len(x))
    print(count)
    print("\n")
print(len(new_List))