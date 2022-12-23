def get_data():
    with open("data.txt", "r") as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    data = preprocess(data)
    return(data)

def preprocess(data):
    for i in range(len(data)):
        data[i] = data[i].split(",")
        data[i] = [x.split("-") for x in data[i]]
        data[i] = [[int(x[0]), int(x[1])] for x in data[i]]
        
        '''
        for j, pair in enumerate(data[i]):
            minimum = pair[0]
            maximum = pair[1]
            data[i][j] = [x for x in range(minimum, maximum+1)]
        '''
    return(data)

def solve1(data):
    sum = 0

    for pair in data:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]: 
            sum += 1
        elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            sum += 1

    return(sum)

def solve2(data):
    sum = 0

    for pair in data:
        combined = {}
        for li in pair:
            for num in range(li[0],li[1]+1):
                if combined.get(num) == None:
                    combined[num] = 1
                else:
                    sum += 1
                    break
    return(sum)    

if __name__=="__main__":
    data = get_data()
    #print(data)
    #print(solve1(data))       
    print(solve2(data))