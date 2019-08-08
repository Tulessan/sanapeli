# tässä tehdään varsinainen sanapeli

import listanluonti as ll
import sanat as ss


def Kysele():
    Sanat = ll.Luonti("sanalista.txt")
    Play = True
    while Play:
        Sana = input("Anna sana: ")
        Tulos = ss.Sanatesti(Sana, Sanat)
        if len(Tulos) > 0:
            print("Tässä mahdolliset sanat:")
            print(Tulos)
        else:
            print("Ei mahdollisia sanoja.")
        Jatko = input("Pelataanko uudelleen? (K/E)")
        if Jatko.lower() == "k":
            pass
        else:
            Play = False

Kysele()