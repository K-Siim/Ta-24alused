nimi = str(input ("Sisestage oma nimi:"))
print('Tere', nimi)
elukoht = str(input ("Kus te elate?:"))
if elukoht.lower() == "saaremaal":  
    print("Saaremaa on imeline koht elamiseks!")
vanus = int(input("Kui vana sa oled? "))
if vanus < 18:
    print("Sa oled liiga noor, et autot juhtida.")
elif vanus == 18:
    print("Palju õnne täisealiseks saamise puhul! Nüüd saad autot juhtida.")
else:
    print("Sa võid autot juhtida.")