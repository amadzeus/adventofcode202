csv_file = "input20257"
import time


def load_input_file(path):
    result = 0
    fulltab = []
    tabsplit = []
    result = 1
    with open(csv_file, 'r', encoding='utf-8') as f:
        linia = f.readline()
        while linia:
            fulltab.append(linia[:-1])
            linia = f.readline()

    for i in range(len(fulltab) - 1):
        temptab = []
        # print(i)
        for indeks, znak in enumerate(fulltab[i]):
            # print(j)
            if znak == '^':
                temptab.append(indeks)
        if temptab != []:
            tabsplit.append(temptab)
    print(tabsplit)
    slownik = {tabsplit[0][0]: 1}

    print(slownik)

    for i in tabsplit:
        print(i)
        for j in i:
            print(j)
            if j in slownik.keys():

                if j-1 not in slownik.keys():
                    slownik.setdefault(j-1,1)
                elif slownik[j-1]==0:
                    slownik[j-1]=slownik[j]
                else:
                    slownik[j-1]+=slownik[j]
                if j+1 not in slownik.keys():
                    slownik.setdefault(j+1,1)
                elif slownik[j+1]==0:
                    slownik[j+1]=slownik[j]
                else:
                    slownik[j+1]+=slownik[j]
                slownik[j]=0
            print(slownik)
            for z in range(50):
                if z in slownik.keys() and slownik[z]>0:
                    print(str(z) +' : ' +str(slownik[z]))
        print('-----------------')
    print(sorted(slownik.items()))
    print('-----')
    print(sum(slownik.values()))

    # temptab = [[tabsplit[0][0],1]]
    # print(tabsplit[:-1])
    # # print(len(tabsplit[:-1]))
    # print(temptab)

    print(time.perf_counter())


load_input_file(csv_file)

# 3254- That's not the right answer; your answer is too low