# tässä luetaan sanalista ja filtteröidään

def Luonti(Tiedostonimi):
    Kahva = open(Tiedostonimi, mode="r", encoding="utf-16")
    Temp = Kahva.read().splitlines()
    Data = []
    for I in Temp:
        if I.isalpha():
            if I.islower():
                Data.append(I)
            else:
                pass
        else:
            pass
    return(Data)

