def get_data():
    with open("data.txt", "r") as f:
        d = f.readlines()
    data = [x for x in d[0]]
    return(data)

def solve1(data):

    base = []

    for i, char in enumerate(data):
        if len(base) < 4:
            base.append(char)
            continue
        else:
            base.pop(0)
            base.append(char)
        if len(set(base)) == len(base):
            return(i+1)

def solve2(data):

    base = []

    for i, char in enumerate(data):
        if len(base) < 14:
            base.append(char)
            continue
        else:
            base.pop(0)
            base.append(char)
        if len(set(base)) == len(base):
            return(i+1)         

if __name__=="__main__":
    data = get_data()
    #print(data)
    #print(solve1(data))
    print(solve2(data))