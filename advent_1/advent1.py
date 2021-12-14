# List of sonar sweep report
sonar = []
first_reading = 0
current_reading = 0
last_reading = 0
next_reading = 0
increase_count = 0
decrease_count = 0

f = open('advent1.txt', 'r')

for x in f:
    sonar.append(x.strip())

for i in range(len(sonar)):
    if i == 0:
        first_reading = int(sonar[i])
        current_reading = int(sonar[i])
        next_reading = int(sonar[i + 1])

        if first_reading < next_reading:
            increase_count = increase_count + 1
        elif first_reading > next_reading:
            decrease_count = decrease_count + 1
        else:
            print("same")

    if i < len(sonar) - 1 and i >= 1:
        current_reading = int(sonar[i])
        next_reading = int(sonar[i + 1])

        if current_reading < next_reading:
            increase_count = increase_count + 1
        elif current_reading > next_reading:
            decrease_count = decrease_count + 1
        else:
            print("same") 
    
    if i == len(sonar) - 1:
        pass

print(increase_count)
print(decrease_count)

