life_support = 0
oxygen_rate = []
co2_rate = []
most_bin = [0] * 12
least_bin = [0] * 12
total_per_position = [0] * 12

most_common = [0] * 12
least_common = [0] * 12

#f = open('advent1.txt', 'r')

with open('advent1.txt', 'r') as file:
    data = file.readlines()

# Get total per position for most common
for row in data:
    row = row.strip()
    oxygen_rate.append(row)

    for i in range(len(row)):
        if i < len(row):
            total_per_position[i] += int(row[i]) # row[i] = 1 or zero

for a in range(len(total_per_position)):
    #(len(f)/2)
    if total_per_position[a] > (len(data)/2):
        most_bin[a] = 1
    else:
        least_bin[a] = 1

for row in oxygen_rate:
    row = row.strip()
    # print("row[0] " + row[0])
    # print("most_bin[0] " + str(most_bin[0]))
    if row[0] != str(most_bin[0]):
        oxygen_rate.remove(str(row))

total_per_position[1] = 0

for row in oxygen_rate:

    total_per_position[1] += int(row[1])
    if total_per_position[1] > (len(data)/2):
        most_common[1] = 1
    else:
        least_common[1] = 1

    print("row[0] " + row[1])
    print("most_common[1] " + str(most_common[1]))
    print(row[1] != str(most_common[1]))
        
    if row[1] != str(most_common[1]):
        oxygen_rate.remove(str(row))


#print(total_per_position[1])

print(oxygen_rate)
exit()

for a in range(len(total_per_position)):
    #(len(f)/2)
    if total_per_position[a] > (len(data)/2):
        most_bin[a] = 1
    else:
        least_bin[a] = 1

# Check row by row for bin that has same as most common
#for a in range(len(most_bin)):
print(most_bin)
print(least_bin)
for row in data:
    row = row.strip()
    if row[0] == str(most_bin[0]):
        oxygen_rate.append(row)

    if row[0] == str(least_bin[0]):
        co2_rate.append(row)

for i in range(len(most_bin)):
    for item in oxygen_rate:
        if item[i] != str(most_bin[i]):
            oxygen_rate.remove(item)

for i in range(len(least_bin)):
    for item in co2_rate:
        if item[i] != str(least_bin[i]):
            co2_rate.remove(item)

    # for j in range(len(row)):
    #     if row[j] == str(most_bin[j]):
    #         oxygen_rate[j] = row
            
    #         # if most_bin[j] - 1 != 0:
    #         #     co2_rate[j] = "1"
    #         # else:
    #         #     co2_rate[j] = "0"
    #     else:
    #         pass


#oxygen_rate = "".join(str(int) for int in oxygen_rate)
#co2_rate = "".join(str(int) for int in co2_rate)
print(oxygen_rate) # 100110010100
print(co2_rate)
#print(co2_rate)
# life_support = oxygen_rate * co2_rate

# print(life_support)
