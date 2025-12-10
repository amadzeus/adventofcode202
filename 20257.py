from os import remove

csv_file = "input20257"
import time


def load_input_file(path):
    fulltab=[]
    tabsplit=[]
    result=3
    with open(csv_file, 'r', encoding='utf-8') as f:
        linia = f.readline()
        while linia:

            fulltab.append(linia[:-1])
            linia=f.readline()
    # print(fulltab[140])
    print(len(fulltab))

    for i in range(len(fulltab)):
        temptab =[]
        # print(i)
        for indeks, znak in enumerate(fulltab[i]):
            # print(j)
            if znak=='^':
                temptab.append(indeks)
        tabsplit.append(temptab)
    print(tabsplit)
    for j in tabsplit:

        if j==[]:
            tabsplit.remove(j)

    temptab=[tabsplit[0][0]]
    # print(tabsplit[0][0])
    for k in range(1,len(tabsplit)):
        print('tabelaorginalan: '+str(tabsplit[k]))
        for beam in tabsplit[k]:
            # print(beam)
            # print(beam-1)
            # print(beam+1)
            if beam in temptab:
                temptab.remove(beam)
                result+=1
            if beam-1 not in temptab:
                temptab.append(beam-1)

            if beam+1 not in temptab:
                temptab.append(beam+1)



        print(temptab)
        print(result)

        # for check in tabsplit[k]:
        #     if check+1 or check-1 in tabsplit[k-1]:
        #         result+=1
        #     else:
        #         temptab.remove(check)

    print(result)
        # print(tabsplit[k])

    print(time.perf_counter())
load_input_file(csv_file)