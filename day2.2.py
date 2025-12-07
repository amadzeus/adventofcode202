csv_file = "input20252"



def load_input_file(path):
    badid = []
    for line in open(csv_file):
        for i in line.split(','):
            print(i)
            if i[0] == str(0):
                print('to nie jest identyfikator')
            else:
                for j in range(int(i.split('-')[0]), int(i.split('-')[1]) + 1):
                    
                    if str(j).count(str(j)[0])==len(str(j)):
                        badid.append(j)
                    for k in range(2, (int(len(str(j))+1)//2)+1):
                        print(str(j))
                        print(str(j)[0:k]*((int(len(str(j))+1)//2)))

                        if str(j)[0:k]*((int(len(str(j))+1)//2)+1)==str(j):
                            print (str(j)[0:k])
                            print(str(j).count(str(j)[0:k]))
                            print (k)




    print(badid)
    print(sum(badid))
load_input_file(csv_file)