def solve(data):
    calories_sum = 0
    calories = {}
    for x in data:
        if x != "":
            calories_sum += int(x)
        else:
            if calories.get(calories_sum) is None:
                calories[calories_sum] = 1
            else:
                calories[calories_sum] += 1
            calories_sum = 0

    length = 0
    solution = 0
    for key in sorted(calories.keys(), reverse = True):
        if length < 3:
            add_length = calories[key]
            if (add_length + length) > 3:
                solution += (3 - length) * key
            else:
                length += calories[key]
                solution += calories[key] * key
        solution
    return(solution)

if __name__=="__main__":
    data = []
    while True:
        line = input()
        if line == "":
            if last is True:
                break
            else:
                last = True
        else:
            last = False
        data.append(line)
    print(solve(data))
            
    