def get_data():
    data = []
    while True:
        line = input()
        if line == "":
            if last is True:
                data.pop(-1)
                break
            else:
                last = True
        else:
            last = False
        data.append(line)
    return(data)

def priorities():
    # define score of eache letter
    relevance = dict()
    for i, x in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        relevance[x] = i+1
    return(relevance)

def solve1(data, relevance):
    

    sum = 0
    for items in data:
        length = len(items)
        backpack1 = {}
        for item in items[0:int(length/2)]:
            if backpack1.get(item) is None:
                backpack1[item] = 1
            else:
                backpack1[item] += 1
        
        backpack2 = {}
        for item in items[int(length/2):int(length)]:
            if backpack2.get(item) is None:
                backpack2[item] = 1
            else:
                backpack2[item] += 1

        #print(backpack1, backpack2)

        for key in backpack1:
            if backpack2.get(key) is not None:
                sum += relevance[key]
                #print(f"{key} : {relevance[key]}")
                break
    return(sum)

def solve2(data, priorities):
    sum = 0

    for i in range(0, len(data), 3):
        one, two, three = data[i:i+3]
        
        b1, b2, b3 = dict(), dict(), dict()

        for char in one:
            if b1.get(char) is None:
                b1[char] = 1
            else:
                b1[char] += 1

        for char in two:
            if b2.get(char) is None:
                b2[char] = 1
            else:
                b2[char] += 1

        for char in three:
            if b3.get(char) is None:
                b3[char] = 1
            else:
                b3[char] += 1
            
        for key in b1:
            if b2.get(key) is not None and b3.get(key) is not None:
                sum += priorities[key]
                break

    return(sum)
    
    

if __name__=="__main__":
    #data = get_data()
    #get data from data.txt as list
    with open("data.txt", "r") as f:
        data = f.readlines()
    data = [x.strip() for x in data]

    #get result 1
    #print(solve1(data, priorities()))

    #get result 2
    print(solve2(data, priorities()))       
    