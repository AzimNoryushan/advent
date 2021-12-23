life_support = 0
oxygen_rate = 0
co2_rate = 0
total_per_position = [0] * 12

with open('advent1.txt', 'r') as file:
    data = file.readlines()

dataLen = len(data)
currentIndex = 0
chunk = data

while currentIndex < dataLen:
    rows = len(chunk)
    ones = 0
    for row in chunk:
        total_per_position[currentIndex] += int(row[currentIndex])

    chunk = [x for x in chunk if x[currentIndex] == ('1' if total_per_position[currentIndex] >= rows/2 else '0')]

    currentIndex += 1
    if len(chunk) == 1:
        break

oxygen_rate = int(chunk[0],2)

dataLen = len(data)
currentIndex = 0
chunk = data

while currentIndex < dataLen:
    rows = len(chunk)
    total_per_position[currentIndex] = 0 # reset value of total per position
    for row in chunk:
        total_per_position[currentIndex] += int(row[currentIndex])

    chunk = [x for x in chunk if x[currentIndex] == ('1' if total_per_position[currentIndex] < rows/2 else '0')]

    currentIndex += 1
    if len(chunk) == 1:
        break

co2_rate = int(chunk[0], 2)

print("Oxygen", oxygen_rate)
print("CO2", co2_rate)
print(oxygen_rate * co2_rate)