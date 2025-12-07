
csv_file = "input20253"
import time


def load_input_file(path):
    result = []
    control=0
    finalanswer=0
    for line in open(csv_file):
        result = []

        testtab=list(line[:-12])
        # print(testtab)
        print(line[:-1])
        # print(line.index(line[-13]))
        while len(testtab)>0 and len(result)<13:
            # print(testtab)
            # print(max(testtab))
            result.append(max(testtab))
            # print(line.index(max(testtab)))
            testtab=testtab[testtab.index(max(testtab))+1 :  ]+[line[-13+len(result)]]

        print(result)

        if len(result)<12:
            result+=list(line[-13+len(result):])
        # # print(result)
        while len(result)>12:
            result.remove(min(result))
        print(result)
        control = int(''.join(result))
        # print(control)
        # print(len(str(control)))
        finalanswer+=control
        print(finalanswer)
    print(time.perf_counter())


load_input_file(csv_file)

