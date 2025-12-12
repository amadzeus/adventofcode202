csv_file = "input20258t"
import time


def load_input_file(path):
    wspolrzedne=''
    fulltab=[]
    with open(csv_file, 'r', encoding='utf-8') as f:
        linia = f.readline()
        while linia:
            wspolrzedne=linia[:-1].split(',')
            # print(wspolrzedne[0])
            fulltab.append([int(wspolrzedne[0]), int(wspolrzedne[1]),int(wspolrzedne[2])])
            linia = f.readline()

    # print(fulltab)
    slownik = {}
    squeretemp = [[0,0],[0,0],[0,0]]
    # print(fulltab[0])
    restemp=0
    for i in fulltab:
        # print(str(i))
        slownik[str(i)]=[]
    for i  in range(len(fulltab)):
        # print(fulltab[i])


        for punkt in fulltab[i:]:
            restemp= ((fulltab[i][0]-punkt[0])**2+(fulltab[i][1]-punkt[1])**2+(fulltab[i][2]-punkt[2])**2)**0.5
            # print(punkt,restemp)
            slownik[str(fulltab[i])].append(restemp)
            slownik[str(punkt)].append(restemp)
        slownik[str(fulltab[i])].remove(0.0)
    for klucz,wartosc in slownik.items():
        print(f"{klucz}:{wartosc}")


load_input_file(csv_file)

