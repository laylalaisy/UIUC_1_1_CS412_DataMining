import sys

def readInput():
    input = []
    input_set = set()
    is_first = True
    for line in sys.stdin:
        if is_first:
            min_sup = int(line)
            is_first = False
            continue
        input.append(line.rstrip().split(' '))
        input_set.update(line.rstrip().split(' '))
    return min_sup, input, input_set

# def getFrequent(min_sup, input):
#     k = 1


if __name__ == "__main__":
    min_sup, input, input_set = readInput()
    # min_sup = 2
    # input = [['B', 'A', 'C', 'E', 'D'], ['A', 'C'], ['C', 'B', 'D']]
    # input_set = {'D', 'E', 'B', 'C', 'A'}
    print(input)
    print(min_sup)
    print(input_set)


