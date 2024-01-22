import pandas as pd
import numpy as np

movie_list= pd.DataFrame({"rok":[1994,1997,2003,2005,2012,2015,2019],
                          "film":["Pulp Fiction","Jackie Brown","Kill Bill" ,"Sin city - Miasto Grzechu","Django","Nienawistna osemka","Pewnego razu w Hollywood"],
                          "gdzie obejrzec":["Netfilx","Prime","Prime","Prime","Prime","piratebay","Netflix"]})
coop_list=pd.DataFrame({"gra":["Sackboy","Moving Out","Children of morta","For the King","Key We","Lovers in dangerous spacetime","Trash Patrol","Unravel 2","Ship of fools","Tools Up"],
                        "zostalo":["proby rycerzy","achivy","achivy","achivy","podstawka","misje?","NOWA","wszystko","rogalik","dodatek"]})

# print(movie_list)
# print(coop_list)
co_jest=input("Co dzisiaj robimy? film/gra: ")
def rozrywka(co_jest):
    if co_jest == "film":
        film_na_dzis=movie_list["film"].sample().to_string(index=False)
        print(film_na_dzis)
        decyzja=input("Będzie? TAK/NIE ")
        if decyzja=="TAK":
            print("No to siuuuu, obejrzysz na: ")
            print(movie_list[(movie_list["film"]==film_na_dzis)].to_string(index=False))
        else:
            return rozrywka(co_jest)
        
    else:
        gra_na_dzis=coop_list["gra"].sample().to_string(index=False)
        print(gra_na_dzis)
        lepsza_decyzja=input("Będzie? TAK/NIE ")
        if lepsza_decyzja=="TAK":
            print("No to pepega!")
            print(coop_list[(coop_list["gra"]==gra_na_dzis)].to_string(index=False))
        else:
            return rozrywka(co_jest!="film")


rozrywka(co_jest)
