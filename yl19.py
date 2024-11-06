tekst = input("Sisesta enda tekst siia:")
täishäälikud = "aeiouõäöü"
i = 0
a = 0
while i<(len(tekst)):
    if tekst[i] in (täishäälikud):
        a += 1
    i += 1
print ("Täishäälikuid on tekstis  ", a)



