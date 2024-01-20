with open("data.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

print(lines[0])

digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
#max red = 12, green = 13, blue = 14

def checkGame(s):
    i = s.index(':') + 2
    minGreen, minRed, minBlue = 0, 0, 0
    while i < len(s):
        num = ''
        if s[i] in digits:
            while s[i] in digits:
                num += s[i]
                i += 1
            if s[i+1:i+4] == 'red':
                if int(num) > minRed:
                    minRed = int(num)
            elif s[i+1:i+5] == 'blue':
                if int(num) > minBlue:
                    minBlue = int(num)
            elif s[i+1:i+6] == 'green':
                if int(num) > minGreen:
                    minGreen = int(num)
        i += 1
    return minBlue * minGreen * minRed

total = 0

for i in range(len(lines)):
    total += checkGame(lines[i])

print(total)

print(checkGame('Game 3: 8 green, 6 blue, 2 red; 5 blue, 4 red, 13 green; 5 green, 12 blue'))