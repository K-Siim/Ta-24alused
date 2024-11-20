import random

def kivi_paber_käärid():
    valikud = ["kivi", "paber", "käärid"]
    print("Tere tulemast mängu Kivi-Paber-Käärid!")
    
    while True:
        arvuti_valik = random.choice(valikud)
        kasutaja_valik = input("Sisesta oma valik (kivi, paber, käärid või 'Lõpp', et mäng lõpetada): ").lower()
        
        if kasutaja_valik == "Lõpp":
            print("Aitäh mängimast!")
            break
        elif kasutaja_valik not in valikud:
            print("Ei mõista sind! Palun vali 'kivi', 'paber' või 'käärid'.")
            continue
        
        print(f"Arvuti valis: {arvuti_valik}")
        
        if arvuti_valik == kasutaja_valik:
            print("Viik! Proovi uuesti.")
        elif (kasutaja_valik == "kivi" and arvuti_valik == "käärid") or \
             (kasutaja_valik == "paber" and arvuti_valik == "kivi") or \
             (kasutaja_valik == "käärid" and arvuti_valik == "paber"):
            print("Sa võitsid! Tubli töö!")
        else:
            print("Arvuti võitis! Proovi uuesti.")
        
        print()  

kivi_paber_käärid()
