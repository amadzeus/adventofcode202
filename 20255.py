csv_file = "input20255"
import time



def load_input_file(path):
    tabrange = []
    tabid=[]
    result=0
    for line in open(csv_file):

        for i in line.split():
            # print(i)
            if '-' in i:
                tempi=i.index('-')
                # print(i)
                # print(tempi)
                tabrange.append([int(i[:tempi]), int(i[tempi+1:])])
            elif i!='\n':
                tabid.append(int(i))
    for j in tabid:
        for k in tabrange:
            if j>=k[0] and j<=k[1]:
                print(j)
                print(k[0], k[1])
                result+=1
                break

    print(tabid)
    print(tabrange)
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