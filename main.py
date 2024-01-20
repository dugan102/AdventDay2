with open("data.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

print(lines[0])

digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
#max red = 12, green = 13, blue = 14

def checkGame(s):
    i = s.index(':') + 2
    while i < len(s):
        num = ''
        if s[i] in digits:
            while s[i] in digits:
                num += s[i]
                i += 1
            if s[i+1:i+4] == 'red':
                if int(num) > 12:
                    return False
            elif s[i+1:i+5] == 'blue':
                if int(num) > 14:
                    return False
            elif s[i+1:i+6] == 'green':
                if int(num) > 13:
                    return False
        i += 1
    return True

total = 0

for i in range(len(lines)):
    if checkGame(lines[i]):
        total += i+1

print(total)

print(checkGame('Game 3: 8 green, 6 blue, 2 red; 5 blue, 4 red, 13 green; 5 green, 12 blue'))