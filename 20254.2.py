csv_file = "input20254"
import time


def load_input_file(path):
    papertab=[]
    testab=[]
    for line in open(csv_file):
        # print(line[:-1])
        testtab=list(line[:-1])
        # print(testtab)
        papertab.append(testtab)
    # print(papertab)
    #wyświetlam sobie tablice
    # for wiersz in papertab:
    #     for element in wiersz:
    #         print(element,end=" ")
    #     print()
    # buduje sobie obudowaną tablicę
    obudowanaTablica =[]
    for i in papertab:
        nowyWiersz = ['#']+i
        obudowanaTablica.append(nowyWiersz)
    for wiersz in obudowanaTablica:
        wiersz.append('#')
    # print(obudowanaTablica[0])
    # print(len(obudowanaTablica[0]))
    toptab=['#']*(len(obudowanaTablica[0]))
    obudowanaTablica.insert(0,toptab)
    obudowanaTablica.append(toptab)
    # print(obudowanaTablica[0])
    # for wiersz in obudowanaTablica:
    #     print(wiersz)

    #  sprawdzanie indeksów tych znaków i zapis do tablicy
    indekstab=[]
    for j in papertab:
        control = 0
        for k in j:
            if '@' ==k:
                tabindex=[]
                tabindex.append(papertab.index(j))
                tabindex.append(control)
                indekstab.append(tabindex)
                # print(tabindex)
            control += 1

    print(indekstab)
    # porównuję sobie znaki w tablicy ale w mojej obuowanej
    finalresult=0
    result=1

    while result>0:
        for r in papertab:
            for p in r:
                if p == 'x':
                   p.replace('x','.')
        indtemp = []
        print(result)
        for m in indekstab:

            licznikalfa=0
            if obudowanaTablica[m[0]][m[1]]=='@':
                licznikalfa+=1
            if obudowanaTablica[m[0]+1][m[1]]=='@':
                licznikalfa+=1
            if obudowanaTablica[m[0]+2][m[1]]=='@':
                licznikalfa+=1
            if obudowanaTablica[m[0]][m[1]+1]=='@':
                licznikalfa+=1
            if obudowanaTablica[m[0]][m[1]+2]=='@':
                licznikalfa+=1
            if obudowanaTablica[m[0]+2][m[1]+1]=='@':
                licznikalfa+=1
            if obudowanaTablica[m[0]+2][m[1]+2]=='@':
                licznikalfa+=1
            if obudowanaTablica[m[0]+1][m[1]+2]=='@':
                licznikalfa+=1
            if licznikalfa<4:
                papertab[m[0]][m[1]]='x'
                indekstab.remove(m)
                indtemp.append(m)

            # obudowanaTablica[m[0]][m[1]]=='@', obudowanaTablica[m[0]+1][m[1]]=='@',obudowanaTablica[m[0]+2][m[1]]=='@':
            # obudowanaTablica[m[0]][m[1]+1]=='@':
            # obudowanaTablica[m[0]][m[1]+2]=='@':
            # obudowanaTablica[m[0]+2][m[1]+1]=='@':
            # obudowanaTablica[m[0]+2][m[1]+2]=='@', obudowanaTablica[m[0]+1][m[1]+2]=='@':


            # print(obudowanaTablica[m[0]][m[1]],obudowanaTablica[m[0]][m[1]+1], obudowanaTablica[m[0]][m[1]+2])
            # print(obudowanaTablica[m[0]+1][m[1]],' ',obudowanaTablica[m[0]+1][m[1]+2])
            # print(obudowanaTablica[m[0]+2][m[1]], obudowanaTablica[m[0]+2][m[1]+1], obudowanaTablica[m[0]+2][m[1]+2])
            # print(licznikalfa)
        for wiersz in papertab:
            for element in wiersz:
                print(element,end=" ")
            print()
        for wiersz in obudowanaTablica:
            print(wiersz)
        result=0
        secind=1
        for wiersz in papertab:
            # print(wiersz.count('x'))
            result+=wiersz.count('x')

        # print(papertab[2][4])
        print(result)
        finalresult += result
        print(finalresult)
        print(indtemp)
        for u in indtemp:
            papertab[u[0]][u[1]] = '.'
            obudowanaTablica[u[0]+1][u[1]+1] = '.'
    print(finalresult)
    print(time.perf_counter())


load_input_file(csv_file)