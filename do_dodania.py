#jedwas co odjebal
def ceny (cennik, produkt):
  if produkt in cennik:
    return cennik[produkt]
  else:
    return 0
suma=0
cennik = {"woda": 2, "chleb": 3, "komputer": 5000, "roślina": 20, "piwko": 3, "papieroski": 16}
print("produkty:\nwoda\nchleb\nkomputer\nroslina\npiwko\npapieroski")
ilosc_produktow = int(input("Ceny ilu produktów chcesz sprawdzić?")) #zapytanie o to ile cen produktow sprawdzic
for i in range (ilosc_produktow):
    produkt = input("Cenę którego produktu chcesz poznać?")
    suma+=cennik[produkt]
    print(ceny(cennik, produkt))
print("Całość za zakupy:",suma,"złotych")  

