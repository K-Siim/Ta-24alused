
sisend_str = input("Sisesta string: ")
sisend_str = sisend_str.strip()
if len(sisend_str) >= 7 and len(sisend_str) % 2 == 1:

    keskkoht = len(sisend_str) // 2
    keskmised_sümbolid = sisend_str[keskkoht-1:keskkoht+2]
    

    print("Kolm keskmist sümbolit on:", keskmised_sümbolid)
else:
    print("String ei vasta tingimustele.")
