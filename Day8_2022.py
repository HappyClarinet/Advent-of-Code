def get_data():
    with open("data.txt", "r") as f:
        d = f.readlines()
    data = [[int(y) for y in x.strip()] for x in d]
    return(data)

def solve1(data):
    is_visible_grid = [[0 for x in range(len(data[0]))] for y in range(len(data))]
    visible = 0

    up_border_index = 0
    left_border_index = 0
    right_border_index = len(data[0])
    down_border_index = len(data)

    for i, row in enumerate(data):
        for j, num in enumerate(row):
            if i == up_border_index:
                is_visible_grid[i][j] = 1
                visible += 1
            elif i == down_border_index - 1:
                is_visible_grid[i][j] = 1
                visible += 1
            elif j == left_border_index:
                is_visible_grid[i][j] = 1
                visible += 1
            elif j == right_border_index - 1:
                is_visible_grid[i][j] = 1
                visible += 1
            else:
                highest_up = max([data[x][j] for x in range(0, i)])
                highest_down = max([data[x][j] for x in range(i+1, down_border_index)])
                highest_left = max(row[0:j])
                highest_right = max(row[j+1:])
                if num > highest_up or num > highest_down or num > highest_left or num > highest_right:
                    is_visible_grid[i][j] = 1
                    visible += 1
    return(visible)

def pprint(data):
    for x in data:
        print(x)

if __name__=="__main__":
    data = get_data()
    #pprint(data)
    print(solve1(data))
    #print(solve2(data).filespace)