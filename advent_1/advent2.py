# List of sonar sweep report
sonar = []
list_total_3_element = []
first_reading = 0
current_reading = 0
last_reading = 0
next_reading = 0
increase_count = 0
decrease_count = 0
total_3_element = 0

f = open('advent1.txt', 'r')

for x in f:
    sonar.append(int(x.strip()))

for i in range(len(sonar)):
    # Check whether have complete 3 set if not then end
    if i + 2 < len(sonar):
        total_3_element = sonar[i] + sonar[i + 1] + sonar[i + 2]
        list_total_3_element.append(total_3_element)

for i in range(len(list_total_3_element)):
    if i == 0:
        first_reading = list_total_3_element[i]
        current_reading = list_total_3_element[i]
        next_reading = list_total_3_element[i + 1]

        if first_reading < next_reading:
            increase_count = increase_count + 1
        elif first_reading > next_reading:
            decrease_count = decrease_count + 1
        else:
            print("same")

    if i < len(list_total_3_element) - 1 and i >= 1:
        current_reading = list_total_3_element[i]
        next_reading = list_total_3_element[i + 1]

        if current_reading < next_reading:
            increase_count = increase_count + 1
        elif current_reading > next_reading:
            decrease_count = decrease_count + 1
        else:
            print("same") 
    
    if i == len(list_total_3_element) - 1:
        pass

print(increase_count)
print(decrease_count)

