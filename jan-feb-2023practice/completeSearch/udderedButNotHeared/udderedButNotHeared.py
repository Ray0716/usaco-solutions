cowphabet = [*input()]
heared = [*input()]
temp = heared.copy()
length = len(temp)

searchIndex = 0
timesEntire = 0
hearedLettersFound = 0

while hearedLettersFound != length:
    if searchIndex == 0:
        timesEntire += 1
    if cowphabet[searchIndex] == heared[0]:
        hearedLettersFound += 1
        heared.pop(0)
    if searchIndex == 25:
        searchIndex = 0
    else:
        searchIndex += 1
else:
    print(timesEntire)
    quit()