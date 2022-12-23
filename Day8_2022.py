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

def solve2(data):
    scenic_grid = [[0 for x in range(len(data[0]))] for y in range(len(data))]
    max_scenic = 0

    up_border_index = 0
    left_border_index = 0
    right_border_index = len(data[0])
    down_border_index = len(data)

    for i, row in enumerate(data):
        for j, num in enumerate(row):
            if i == up_border_index:
                continue
            elif i == down_border_index - 1:
                continue
            elif j == left_border_index:
                continue
            elif j == right_border_index - 1:
                continue
            else:

                scenic_up = get_visible_trees(num, reversed([data[x][j] for x in range(0, i)]))
                scenic_down = get_visible_trees(num, [data[x][j] for x in range(i+1, down_border_index)])
                scenic_left = get_visible_trees(num, reversed(row[0:j]))
                scenic_right = get_visible_trees(num, row[j+1:])
                
                scenic_score = scenic_up * scenic_down * scenic_left * scenic_right
                
                if scenic_score > max_scenic:
                    max_scenic = scenic_score
                
    return(max_scenic)

def get_visible_trees(num, row):
    for i, heigth in enumerate(row):
        if num <= heigth:
            return(i+1)
    return(i+1)

if __name__=="__main__":
    data = get_data()
    #print(data)
    print(solve1(data))
    print(solve2(data))