def ceny (cennik, produkt):
  if produkt in cennik:
    return cennik[produkt]
  else:
    return 0

cennik = {"woda": 2, "chleb": 3, "komputer": 5000, "roślina": 20, "piwko": 3, "papieroski": 16}

ilosc_produktow = int(input("Ceny ilu produktów chcesz sprawdzić?")) #zapytanie o to ile cen produktow sprawdzic
for i in range (ilosc_produktow):
    produkt = input("Cenę którego produktu chcesz poznać?")
    print(ceny(cennik, produkt))


