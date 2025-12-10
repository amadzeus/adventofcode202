from os import remove

csv_file = "input20257t"
import time


def load_input_file(path):
    fulltab = []
    tabsplit = []
    result = 3
    with open(csv_file, 'r', encoding='utf-8') as f:
        linia = f.readline()
        while linia:
            fulltab.append(linia[:-1])
            linia = f.readline()



    for i in range(len(fulltab)):
        temptab = []
        # print(i)
        for indeks, znak in enumerate(fulltab[i]):
            # print(j)
            if znak == '^':
                temptab.append(indeks)
        tabsplit.append(temptab)
    print(tabsplit)
    for j in tabsplit:

        if j == []:
            tabsplit.remove(j)

    temptab = [tabsplit[0][0]]
    print(tabsplit[:-1])
    print(len(tabsplit[:-1]))
    totalres=0
    for k in range(1, len(tabsplit)):
        result = 0
        print('tabelaorginalan: ' + str(tabsplit[k]))
        for beam in tabsplit[k]:
            # print(beam)
            # print(beam-1)
            # print(beam+1)
            if beam in temptab:
                temptab.remove(beam)
                result += 1
            if beam - 1 not in temptab:
                temptab.append(beam - 1)

            if beam + 1 not in temptab:
                temptab.append(beam + 1)

        print(temptab)
        print(result)
        totalres += result


    print(totalres+3)
    # print(tabsplit[k])
    wynik = 1
    for i in range(1,totalres+3):
        wynik  *= i
    print(wynik)
    print(time.perf_counter())


load_input_file(csv_file)