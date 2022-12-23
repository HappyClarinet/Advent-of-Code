def solve1(data):
    # rock: A, X
    # paper: B, Y
    # scicor: C, Z
    
    choice = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    win = ["A Y", "B Z", "C X"]
    loss = ["A Z", "B X", "C Y"]
    tie = ["A X", "B Y", "C Z"]

    score = 0

    for game in data:
        score += choice[game[2:3]]
        if game in win:
            score += 6
        elif game in tie:
            score += 3

    return(score)

def solve2(data):
    # rock: A
    # paper: B
    # scicor: C
    # X: loss
    # Y: tie
    # Z: win

    what_to_do = {
        # lose
        "X": {
            # how much points would i get if opp plays A, B or C
            "A": 3, # as opp plays rock, i need to play scicor to lose, scicors equals 3 points
            "B": 1, # as opp plays paper, i need to play rock to lose, rock equals 1 points
            "C": 2 # as opp plays scicor, i need to play paper to lose, paper equals 2 points
        },
        # tie
        "Y": {
            "A": 4,
            "B": 5,
            "C": 6
        },
        # win
        "Z": {
            "A": 8,
            "B": 9,
            "C": 7
        }
    }

    score = 0
    for game in data:
        score += what_to_do[game[2:3]][game[0:1]]
    
    return(score)

if __name__=="__main__":
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
    #print(solve1(data))
    print(solve2(data))
            
    