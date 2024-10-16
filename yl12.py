puuviljad = ["banaan", "mango", "viinamari"]
print("Puuviljad:", puuviljad)
print("Esimene puuvili:", puuviljad[0])
puuviljad.append("apelsin")
print("Puuviljad pärast lisamist:", puuviljad)
print("Viimane puuvili:", puuviljad[-1])
puuviljad[1] = "õun"  
print("Muudetud puuviljad:", puuviljad)
if "õun" in puuviljad:
    print("Õun on listis.")
else:
    print("Õun ei ole listis.")
print("Listi pikkus:", len(puuviljad))
puuviljad.remove("banaan")  
print("Puuviljad pärast eemaldamist:", puuviljad)
puuviljad.reverse()
print("Puuviljad vastupidises järjekorras:", puuviljad)
puuviljad.sort()
print("Sorteeritud puuviljad:", puuviljad)
