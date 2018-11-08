import sys
from collections import Counter

def read_in():
    data = []

    while True:
        line = sys.stdin.readline().strip('\n')
        if not line:
            break
        tempdata = line.split(' ')
        data.append(tempdata)

    return data

def scanDB(min_sup, data, i):
    result = []
    combine_flat = []

    for row in data:
        for m in range(0, len(row)-i+1):
            temp = []
            for n in range(m,m+i):
                temp.append(row[n])
            combine_flat.append(tuple(temp))

    count = Counter(combine_flat)

    for x in count:
        if count[x] >= min_sup:
            temp = {'pattern': x, 'count': count[x]}
            result.append(temp)

    result = sorted(result, key=lambda x: (-x['count'], x['pattern']))
    max_idx = min(len(result), 20)
    if max_idx > 0:
        min_sup = max(min_sup, result[max_idx-1]['count'])

    return min_sup, result[0:max_idx]

if __name__ == "__main__":
    max_len = 0
    pattern = []

    dict = []
    result = []     # data after processed
    result1 = []    # result of all patterns meets min_sup

    min_sup = 2
    data = read_in()

    for x in data:
        if max_len < len(x):
            max_len = len(x)

    max_len = min(max_len, 5)

    # generate patterns meets min_sup
    for i in range(max_len, 1, -1):
        min_sup, temp = scanDB(min_sup, data, i)
        if temp:
            result2 = []
            for x in temp:
                str = x["pattern"][0]
                for i in range(1, len(x["pattern"])):
                    str = str + ' ' + x["pattern"][i]
                tempdict = {'pattern': str, 'count': x['count']}
                result1.append(tempdict)

    result1 = sorted(result1, key=lambda x:(-x['count'], x['pattern']))

    for i in range(min(20, len(result1))):
        print("[%d, '%s']" %(result1[i]['count'], result1[i]['pattern']))






