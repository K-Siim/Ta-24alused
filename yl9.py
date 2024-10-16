külg1 = float(input ("Sisesta kolmnurga esimene külg:"))
külg2 = float(input ("Sisesta kolmnurga teine külg:"))
külg3 = float(input ("Sisesta kolmnurga kolmas külg:"))
if (külg1 + külg2 > külg3) and (külg1 + külg3 > külg2) and (külg2 + külg3 > külg1):
    if külg1 == külg2 == külg3:
        print("Kolmnurk on võrdkülgne.")
    elif külg1 == külg2 or külg1 == külg3 or külg2 == külg3:
        print("Kolmnurk on võrdhaarne.")
    else:
        print("Kolmnurk on erikülgne.")
else:
    print("Sellise külgede pikkusega kolmnurk ei saa eksisteerida.")