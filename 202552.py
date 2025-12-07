from os import remove

csv_file = "input20255t"
import time



def load_input_file(path):
    tabrange = []
    tabid=[]
    result=0
    tempnr=0
    for line in open(csv_file):
        for i in line.split():
            # print(i)
            if '-' in i:
                tempi=i.index('-')
                # print(i)
                # print(tempi)
                tabrange.append([int(i[:tempi]), int(i[tempi+1:])])
            # elif i!='\n':
            #     tabid.append(int(i))
    # for j in tabid:
    #     for k in tabrange:
    #         if j>=k[0] and j<=k[1]:
    #             print(j)
    #             print(k[0], k[1])
    #             result+=1
    #             break
    # fajne rozwiązanie, proste ale za dużo czasu wymaga
    # for j in tabrange:
    #     print(j)
    #     tempnr = j[0]
    #     while tempnr < j[1]+1:
    #         if tempnr not in tabid:
    #             tabid.append(tempnr)
    #         tempnr+=1

    temptab=[]
    # print(sorted(tabrange))


    tabrange=sorted(tabrange)
    temptest=tabrange
    for i in range(len(temptest)-1):

        if temptest[i][1]>temptest[i+1][0]:
            # print('stara wartosć')
            # print(temptest[i], temptest[i + 1])
            if temptest[i][1] >= temptest[i + 1][1]:
                temptest[i+1][1] = temptest[i][1]
            temptest[i][1]=temptest[i+1][0]
            print('nowa wartosc')
            print(temptest[i], temptest[i + 1])
    print('kasujemy pojedyncze')


    for j in reversed(range(len(temptest)-1)):

        if temptest[j][0]==temptest[j][1] and (temptest[j+1][0]==temptest[j][1]):
            print(temptest[j])
            temptest.remove(temptest[j])

    print('-------------------------')
    for j in reversed(range(len(temptest)-1)):
        # print('przed zmianami')
        # print(temptest[j])
        if temptest[j][1]==temptest[j+1][0]:
            temptest[j][1]=temptest[j+1][1]
            temptest.remove(temptest[j+1])

    for j in temptest:
        # print('po zmianach')
        print(j)
        result+=j[1]-j[0]+1

        #     temptest[i+1]=max(temptest[i+1][1],temptest[i][1])
        #     temptest[i][1]=temptest[i+1][0]
    # for j in range(len(temptest)):
    #     print(tabrange[j],temptest[j])













    # for abc in sorted(tabrange):
    #     print(abc)
    # print(tabrange[-1][1])
    # lastnr=tabrange[-1][1]
    # arghb=1
    # while arghb>0:
    #     arghb=0
    #     temptab=[]
    #     for i in range(len(tabrange)-1) :
    #
    #         if tabrange[i+1][1]<lastnr:
    #             # print(sorted(tabrange[i]))
    #             if tabrange[i][1]>=tabrange[i+1][0]:
    #                 if  tabrange[i+1][0]>tabrange[i][0]:
    #                     tabrange[i][1]=tabrange[i+1][1]
    #                     tabrange.remove(tabrange[i+1])
    #                 else:
    #                 # print(tabrange[i])
    #                     temptab.append(i+1)
    #                 arghb+=1
    #     # print('tsagsgg')
    #     print(tabrange)
    #     for bca in tabrange:
    #         print(bca)
    #     for j in reversed(temptab):
    #         print(j)
    #         tabrange.remove(tabrange[j])
    # print(tabrange)
    # for gra in tabrange:
    #     print(gra)
    # # result=len(tabid)
    # for i in tabrange:
    #     result+=i[1]-i[0]

    print(result)
            # if i[0] == str(0):
            #     print('to nie jest identyfikator')
            # else:
            #     for j in range(int(i.split('-')[0]), int(i.split('-')[1]) + 1):
            #         # print(j)
            #         # print(len(str(j)))
            #         if str(j).count(str(j)[0])==len(str(j)):
            #             badid.append(j)
            #         for k in range(2, (int(len(str(j))+1)//2)+1):
            #             print(str(j))
            #             print(str(j)[0:k]*((int(len(str(j))+1)//2)))
            #
            #             if str(j)[0:k]*((int(len(str(j))+1)//2)+1)==str(j):
            #                 print (str(j)[0:k])
            #                 print(str(j).count(str(j)[0:k]))
            #                 print (k)




    # print(badid)
    # print(sum(badid))
    print(time.perf_counter())
load_input_file(csv_file)


