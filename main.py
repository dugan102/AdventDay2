with open("data.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

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
                #find minimum amount of reds needed
                if int(num) > minRed:
                    minRed = int(num)
            elif s[i+1:i+5] == 'blue':
                # find minimum amount of blues needed
                if int(num) > minBlue:
                    minBlue = int(num)
            elif s[i+1:i+6] == 'green':
                # find minimum amount of greens needed
                if int(num) > minGreen:
                    minGreen = int(num)
        i += 1
    # return product of minimum necessary of greens, blues, and reds
    return minBlue * minGreen * minRed

total = 0

for i in range(len(lines)):
    total += checkGame(lines[i])

print(total)