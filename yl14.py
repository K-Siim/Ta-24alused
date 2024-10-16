
failinimi = input("Sisesta failinimi kujul 'failinimi.ext': ")
osad = failinimi.split(".")
if len(osad) > 1:
    print("Faili laiend on:", osad[-1])
else:
    print("Failil pole laiendit.")
