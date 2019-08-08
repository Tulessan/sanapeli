# tässä tehdään varsinainen sanapeli

import listanluonti as ll
import sanat as ss


def Kysele():
    Sanat = ll.Luonti("sanalista.txt")
    Play = True
    while Play:
        Sana = input("Please give a word: ").lower()
        if not Sana.isalpha():
            print("You should use alphanumeric characters only...")
        else:
            pass
        Tulos = ss.Sanatesti(Sana, Sanat)
        if len(Tulos) > 0:
            print("Possible words from your word:")
            print(Tulos)
        else:
            print("No words can be formed from your word.")
        Jatko = input("Do you want to play again? (Y/N)")
        if Jatko.lower() == "y":
            pass
        else:
            Play = False

Kysele()