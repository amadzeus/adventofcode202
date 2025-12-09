csv_file = "input20256"
import time


def load_input_file(path):
    result = 0
    słownik_tabel={}
    checktab = 0
    fulltab=[]
    spacecount = 0
    tablicawynikow=[]
    with open(csv_file, 'r', encoding='utf-8') as f:
        linia = f.readline()
        while linia:
            # print(linia.splitlines())
            fulltab.append(linia.splitlines())
            linia=f.readline()

    fulltab.append([])


    print(fulltab)
    print(fulltab[-1])
    for j in fulltab[-2]:
        print(j)
        print(j[1])
        for i in j:

            if i==' ':
                spacecount+=1
                # print(spacecount)
            else:
                fulltab[-1].append(spacecount)
                spacecount=0
    del fulltab[-1][0]

    fulltab[-1].append(4)
    print(fulltab)
    # print(fulltab)
    print(fulltab[0][0][0])
    print(fulltab[5])
    indekstemp=0

    for i in fulltab[5]:
        j=i
        # print(i)
        # print(indekstemp)
        # print((fulltab[0][0][indekstemp:][j-1]))
        if fulltab[4][0][indekstemp:][0] == '+':
            result =0
        if fulltab[4][0][indekstemp:][0] == '*':
            result =1

        while j>0:
            # print(i)
            j -= 1
            liczba = int((fulltab[0][0][indekstemp:][j]) +
                          (fulltab[1][0][indekstemp:][j])+
                          (fulltab[2][0][indekstemp:][j])+
                          (fulltab[3][0][indekstemp:][j]))
            print(liczba)
            # print(fulltab[4][0][indekstemp:][0])
            if fulltab[4][0][indekstemp:][0]=='+':
                result+=liczba
                print('aktualny wynik: '+str(result))
            if fulltab[4][0][indekstemp:][0]=='*':

                result*=liczba
        indekstemp += i+1
        tablicawynikow.append(result)
    print(tablicawynikow)
    print(sum(tablicawynikow))
    # for i in reversed(range(len(fulltab[1][0]))):
    #     # print(i)
    #     print(fulltab[0][0][i])
    #     print(fulltab[1][0][i])
    #     print(fulltab[2][0][i])
    #     print(fulltab[3][0][i])
    #     liczba =int((fulltab[0][0][i])+
    #     (fulltab[1][0][i])+
    #     (fulltab[2][0][i])+
    #     (fulltab[3][0][i]))
    #     print(liczba)
        # zawartosc_pliku = f.readline()
        # print(f"{zawartosc_pliku}") # Wypisze: ' 5 '
        # print(f"Długość odczytanego stringu: {len(zawartosc_pliku)}")
        # print(zawartosc_pliku)
        # print(zawartosc_pliku.splitlines())
    # for i in zawartosc_pliku:
    #
    #     print(i)

    #     for indeks, wartosc in enumerate(linia):
    #         # if linia[0] == "+" or linia[0]=="*":
    #         #     tabname = f"tabela{indeks}"
    #         #     słownik_tabel[tabname].append(wartosc)
    #         if f"tabela{indeks}" not in słownik_tabel :
    #             # print(indeks)
    #             # print(wartosc)
    #             tabname=f"tabela{indeks}"
    #             słownik_tabel[tabname]=[wartosc]
    #
    #             # print(słownik_tabel)
    #
    #             tabname=f"tabela{indeks}"
    #             słownik_tabel[tabname].append(wartosc)
    #
    #             # print(słownik_tabel[tabname])
    #     checktab = 1
    #
    # print(słownik_tabel)
    # print(słownik_tabel['tabela0'])

    # for i in słownik_tabel.values():
    #     print(i)
    #     if i[-1]=='+':
    #         print(sum(i[:-1]))
    #         result+=sum(i[:-1])
    #     if i[-1]=='*':
    #         res=1
    #         for k in i[:-1]:
    #             res*=int(k)
    #         result+=res
    #         print(res)
    # print(result)
    print(time.perf_counter())
load_input_file(csv_file)