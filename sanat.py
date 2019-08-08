# sanavaihtoehtojen etsintä tiedostosta

def Testi(Sana1: str, Sana2: str):
    Sana1 = list(Sana1)
    Sana2 = list(Sana2)
    Out = False
    for K in Sana2:
        if K not in Sana1:
            Out = False
            break
        else:
            Sana1.remove(K)
            Out = True
    return(Out)


def Sanatesti(Sana: str, Sanalista):
    Lista = []
    for S in Sanalista:
        if len(S) <= len(Sana):
            if Testi(Sana, S):
                Lista.append(S)
            else:
                pass
        else:
            pass
    return(Lista)



