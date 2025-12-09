csv_file = "input20256t"
import time


def load_input_file(path):
    result = 0
    słownik_tabel={}
    checktab = 0
    for line in open(csv_file):
        # print('-----')
        linia = line.split()
        # print(linia)

        for indeks, wartosc in enumerate(linia):
            if linia[0] == "+" or linia[0]=="*":
                tabname = f"tabela{indeks}"
                słownik_tabel[tabname].append(wartosc)

            elif checktab==0:
                # print(indeks)
                # print(wartosc)
                tabname=f"tabela{indeks}"
                słownik_tabel[tabname]=[wartosc]

                # print(słownik_tabel)
            else:
                tabname=f"tabela{indeks}"
                słownik_tabel[tabname].append(wartosc)

                # print(słownik_tabel[tabname])
        checktab = 1

    print(słownik_tabel)
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