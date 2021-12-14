foward = 0
depth = 0
up = 0
down = 0
aim = 0

f = open('advent1.txt', 'r')

for x in f:
    x = x.strip()
    x = x.split()

    if x[0] == 'forward':
        foward += int(x[1])
        depth += aim * int(x[1])
    
    if x[0] == 'up':
        aim -= int(x[1])
    elif x[0] == 'down':
        aim += int(x[1])
    else:
        pass

print(foward*depth)