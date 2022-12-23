class folder:
    def __init__(self, name, parent):
        self.name = name
        self.filespace = 0
        self.parent = parent
        self.children = {}
        self.files = {}

def get_data():
    with open("data.txt", "r") as f:
        d = f.readlines()
    data = [x.strip() for x in d]
    return(data)

def preprocess(data):
    home = folder("/", None)
    current = home
    dirs = [home]

    for arg in data:
        if arg[0:4] == "$ cd":
            dir = arg[5:]
            if dir == "..":
                current = current.parent
                continue
            elif dir == "/":
                current = home
                continue
            else:
                if current.children.get(dir) is None:
                    current.children[dir] = folder(dir, current)
                current = current.children[dir]
                continue
        elif arg[0:4] == "$ ls":
            continue
        elif arg[0:3] == "dir":
            dir = arg[4:]
            if current.children.get(dir) is None:
                current.children[dir] = folder(dir, current)
                dirs.append(current.children[dir])
            continue
        else:
            size, name = arg.split(" ")
            current.files[name] = size
            current.filespace += int(size)
            
            rec_cur = current
            while rec_cur.parent is not None:
                rec_cur.parent.filespace += int(size)
                rec_cur = rec_cur.parent
    return(home, dirs)

def solve1(data):
    _, dirs = preprocess(data)

    sum = 0
    for d in dirs:
        if d.filespace <= 100000:
            sum += d.filespace
    return(sum)

def solve2(data):
    home, dirs = preprocess(data)

    diff = home.filespace - 40000000
    smallest = home

    for d in dirs:
        if d.filespace < smallest.filespace and d.filespace > diff:
            smallest = d

    return(smallest)

if __name__=="__main__":
    data = get_data()
    #print(data)
    #print(solve1(data))
    print(solve2(data).filespace)