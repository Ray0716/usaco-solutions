def remove_duplicates(lst):
    result = list(set(lst))
    return result


def teamUpOneCow(team, board):
    # team = ['A']
    result = []

    # Flatten the 2D array
    flat_list = [letter for sublist in board for letter in sublist]
    
    # Use a set to get unique letters
    letters = list(set(flat_list))
    print(letters)
    for l in letters:
        if l != team[0]:
            result.append("".join(sorted([team[0], l])))
    #print(result)
    return result




def checkSingleCowVictories(board):
    count = 0
    victoryCows = []
    for x in range(3):
        if all(i == board[x][0] for i in board[x]): # check horiz
            count += 1
            victoryCows.append(board[x][0])
        if all(i == board[0][x] for i in [board[0][x], board[1][x], board[2][x]]): # check vertic row
            count += 1
            victoryCows.append(board[0][x])
    if all(i == board[0][0] for i in [board[0][0], board[1][1], board[2][2]]): # down diagonal
        count += 1
        victoryCows.append(board[0][0])
    if all(i == board[0][2] for i in [board[0][2], board[1][1], board[2][0]]): # up diagonal
        count += 1
        victoryCows.append(board[0][2])

    victoryCows = list(set(victoryCows))

    return len(victoryCows) # number of single victories possible

def checkDoubleCowVictories(board):
    count = 0
    victoryTeams = []
    for x in range(3):
        teamHoriz = board[x]
        teamVert = [board[0][x], board[1][x], board[2][x]]
        teamHoriz = list(set(teamHoriz))
        teamVert = list(set(teamVert))

        # teamhoriz, vert, updiag and downdiag are lists of the unique elements in the 3inarow's
        # if there are 1 or 2 unique elements then we know it is a team win

        #print(f"tHorizontal {teamHoriz}")
        #print(f"teamVert {teamVert}")
        if len(teamHoriz) == 2: # check horiz
            count += 1
            victoryTeams.append("".join(sorted(teamHoriz)))
        if len(teamVert) == 2: # check vertic row
            count += 1
            victoryTeams.append("".join(sorted(teamVert)))

        if len(teamHoriz) == 1:
            for x in teamUpOneCow(teamHoriz, board):
                victoryTeams.append(x)

        if len(teamVert) == 1:
            for x in teamUpOneCow(teamVert, board):
                victoryTeams.append(x)
        

    teamDownDiag = [board[0][0], board[1][1], board[2][2]]
    teamUpDiag = [board[0][2], board[1][1], board[2][0]]
    teamDownDiag = list(set(teamDownDiag))
    teamUpDiag = list(set(teamUpDiag))
    if len(teamDownDiag) == 2: # down diagonal
        victoryTeams.append("".join(sorted(teamDownDiag)))
    if len(teamDownDiag) == 1:
        for x in teamUpOneCow(teamDownDiag, board):
            victoryTeams.append(x)
    if len(teamUpDiag) == 2: # up diagonal
        victoryTeams.append("".join(sorted(teamUpDiag)))
    if len(teamUpDiag) == 1:
        for x in teamUpOneCow(teamUpDiag, board):
            victoryTeams.append(x)

   # print(victoryTeams)
    victoryTeams = remove_duplicates(victoryTeams)
  #  print(" yay " , victoryTeams)
    return len(victoryTeams) # number of single victories possible





with open('tttt.in', 'r') as infile:
    data = []
    for _ in range(3):
        temp = [*infile.readline()]
        try:
            temp.remove("\n")
        except:
            pass
        data.append(temp)

with open('tttt.out', 'w') as outfile:
    outfile.writelines(str(checkSingleCowVictories(data)))
    outfile.write("\n")
    outfile.writelines(str(checkDoubleCowVictories(data)))


#print(checkSingleCowVictories(data))
#print(checkDoubleCowVictories(data))


