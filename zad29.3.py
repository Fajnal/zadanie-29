alfabet = {                                                     #tworzenie słownika alfabet
    '11': 'a',          '001011': 'i',      '1000011': 'r',
    '011': 'b',         '010011': 'j',      '1001011': 's',
    '0011': 'c',        '100011': 'k',      '1010011': 't',
    '1011': 'd',        '101011': 'l',      '00000011': 'u',
    '00011': 'e',       '0000011': 'm',     '00001011': 'w',
    '01011': 'f',       '0001011': 'n',     '00010011': 'x',
    '10011': 'g',       '0010011': 'o',     '00100011': 'y',
    '000011': 'h',      '0100011': 'p',     '01000011': 'z'
}
tekst = ''                                                      #tworzenie pustej zmiennej "tekst"
wiadomosc = ''                                                  #tworzenie pustej zmiennej "wiedomosc"
ciag = input()                                                  #tworzenie zmiennej, do której użytkownik przypisuje wartość
for kulka in ciag:                                              #pętla
    tekst += kulka                                              #dodawanie aktualnej kulki do ciągu tekst
    if kulka == '1' and pamiec == '1':                          #sprawdzanie czy aktualna i poprzednia kulka to "1"
        wiadomosc += alfabet[tekst]                             #przypisywanie do zmiennej "wiadomosc" litery odpowiadającej zmiennej tekst
        tekst = ''                                              #resetowanie wartości zmiennej "tekst"
        kulka = '0'                                             #resetowanie wartości zmiennej "kulka"
    pamiec = kulka                                              #przypisywanie aktualnej kulki do pamięci
print(wiadomosc)                                                #wyświetlanie zdekodowanego tekstu