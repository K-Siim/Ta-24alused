x = int(input("Lisa korrutustabeli number: "))
y = int(input("Lisa mitu rida soovid korrutustabelist saada: "))
if y > 12:
    print("The number of rows has been limited to 12.")
    y=12
for i in range(1, y + 1):
 result = x * i
 print(f"{x} * {i} = {result}")