def get_data():
    with open("data.txt", "r") as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    return(data)

def solve1(data):
    word = ""

    base = {"1": ["D", "B", "J", "V"],
            "2": ["P", "V", "B", "W", "R", "D", "F"],
            "3": ["R", "G", "F", "L", "D", "C", "W", "Q"],
            "4": ["W", "J", "P", "M", "L", "N", "D", "B"],
            "5": ["H", "N", "B", "P", "C", "S", "Q"],
            "6": ["R", "D", "B", "S", "N", "G"],
            "7": ["Z", "B", "P", "M", "Q", "F", "S", "H"],
            "8": ["W", "L", "F"],
            "9": ["S", "V", "F", "M", "R"]}
    
    for order in data:
        amount, start, end = order.replace("move", "").replace("from", "").replace("to", "").split()

        for _ in range(int(amount)):
            base[end].append(base[start].pop(-1))
    
    for key in base:
        word += base[key][-1]
    return(word) 

def solve2(data):
    word = ""

    base = {"1": ["D", "B", "J", "V"],
            "2": ["P", "V", "B", "W", "R", "D", "F"],
            "3": ["R", "G", "F", "L", "D", "C", "W", "Q"],
            "4": ["W", "J", "P", "M", "L", "N", "D", "B"],
            "5": ["H", "N", "B", "P", "C", "S", "Q"],
            "6": ["R", "D", "B", "S", "N", "G"],
            "7": ["Z", "B", "P", "M", "Q", "F", "S", "H"],
            "8": ["W", "L", "F"],
            "9": ["S", "V", "F", "M", "R"]}
    
    for order in data:
        amount, start, end = order.replace("move", "").replace("from", "").replace("to", "").split()

        for i in range(int(amount),0,-1):
            base[end].append(base[start].pop(-i))
    
    for key in base:
        word += base[key][-1]
    return(word) 

if __name__=="__main__":
    data = get_data()
    #print(data)
    #print(solve1(data))
    print(solve2(data))