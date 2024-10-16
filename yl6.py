arv1 = int(input("Sisesta arv:"))
arv2 = int(input("Sisesta arv:"))
arv3 = int(input("Sisesta arv:"))
if arv1 >= arv2 and arv1 >= arv3:
    maximum = arv1
elif arv2 >= arv1 and arv2 >= arv3:
    maximum = arv2
else:
    maximum = arv3
print("Suurim arv on:", maximum)