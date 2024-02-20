#pusta kulka = 0
#pelna kulka = 1
litera = ''                                 #przypisywanie braku wartości do zmiennej litera
pamiec = ''                                 #przypisywanie braku wartości do zmiennej pamiec
kulka = ''                                  #przypisywanie braku wartości do zmiennej kulka
wiadomosc = input()                         #wpisywanie zakodowanej wiadomości przez użytkownika
for kulka in wiadomosc:                     #pętla
    litera+= kulka                          #dodawanie aktualnej kulki do ciągu litery
    if kulka == '1' and pamiec == '1':      #sprawdzanie czy aktualna i poprzednia kulka to "1"
        break                               #zaprzestanie wykonywania pętli
    pamiec = kulka                          #przypisywanie aktualnej kulki do pamięci
print(litera)                               #wyświetlanie ciągu kulek odpowiadających za literę
print(wiadomosc)                            #wiadomość przed usunięciem pierwszej litery
wiadomosc = wiadomosc[len(litera):]         #usuwanie pierwszej litery
print(wiadomosc)                            #wiadomość po usunięciu pierwszej litery