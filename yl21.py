import random

def arvu_arvamise_mäng():
    mõeldud_arv = random.randint(0, 100)
    print("Mul on sulle üks arv vahemikus 0 kuni 100. Tee enda pakkumine!")

    while True:
        try:
            pakkumine = int(input("Sisesta oma pakkumine: "))
            if pakkumine < mõeldud_arv:
                print("Liiga väike! Proovi uuesti.")
            elif pakkumine > mõeldud_arv:
                print("Liiga suur! Proovi uuesti.")
            else:
                print(f"Õige! Arv mille välja mõtlesin oli see {mõeldud_arv}.")
                break
        except ValueError:
            print("Palun sisesta kehtiv täisarv.")
arvu_arvamise_mäng()
