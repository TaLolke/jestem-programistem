import pandas as pd
import numpy as np
# arra1 = [1,5,9,7,5]
# data= pd.read_csv("moje_dane.csv")
# pierwsze=data.head()
# # print(pierwsze)

# data.index=["Jeden","Dwa","Trzy","Cztery","Piec"] #nadaje nazwy indexom zgodnie z listą

# # print(data.Do) #od razu printuje indexy+ kolumnę Do, działa tak samo jak data["Do"]

# # print(data.iloc[1]) # drukuje pierwszy wiersz jako kolumnę (bez indexu), indexy teraz to wcześniejsze nazwy kolumn


# #można dodawać kolumny i od razu je wypełniać (tutaj liczby od 0 do 4)
# data["nowa"]= np.arange(5)

# # Dodanie nowej kolumny i jej wartość jest True jeśli watość innej kolumny jest == X
# data["nowa_kolumna"]= data["Dane"]=="Europa"
# del data["nowa_kolumna"] # usuwa kolumnę
# print(data)

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
diamonds["Quality-color"]=diamonds.cut+", "+diamonds.color
# new_columns= ["Twoja","STara","pierze","w","rzece","new_one","kolejny",'new_table', 'new_price', 'new_x', 'new_y']
# diamonds.columns=new_columns
print(diamonds.head())
diamonds.drop(['cut','x'],axis=1,inplace=True)
print(diamonds.head())
