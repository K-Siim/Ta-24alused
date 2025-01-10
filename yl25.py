
thisdict = {
    "eesnimi": "Kevin",
    "perenimi": "Siim",
    "sünniaasta": "2001",
    "elukoht": "Kihelkonna",
    "magustoit": "Tort"
}

# Elukoha väljastamine kahel viisil
print(thisdict["elukoht"])       # Otsene viide võtmele
print(thisdict.get("elukoht"))   # Kasutades get() meetodit

# Muudan magustoidu väärtust
thisdict["magustoit"] = "Jäätis"

# Kordus üle dictionary võtmete
for key in thisdict:
    print(key)

# Kordus üle dictionary väärtuste (variant 1)
for value in thisdict.values():
    print(value)

# Kordus üle dictionary väärtuste (variant 2)
for key in thisdict:
    print(thisdict[key])

# Kontrollin, kas isikukood on dictionary's olemas
isikukood_olemas = "isikukood" in thisdict
print("Isikukood olemas:", isikukood_olemas)

# Dictionary suuruse leidmine
dictionary_suurus = len(thisdict)
print("Dictionary suurus:", dictionary_suurus)

# Lisan elemendi enda pikkuse jaoks
thisdict["pikkus"] = "180 cm"

# Eemaldan elemendi sünniaasta (variant 1)
thisdict.pop("sünniaasta", None)




