power_consumption = 0
gamma_rate = 0
epsilon_rate = 0
gamma_bin = [0] * 12
epsilon_bin = [0] * 12
total_per_position = [0] * 12

f = open('advent1.txt', 'r')

for x in f:
    x = x.strip()
    for i in range(len(x)):
        if i < len(x):
            total_per_position[i] += int(x[i])

for a in range(len(total_per_position)):
    #(len(f)/2)
    if total_per_position[a] > 500:
        gamma_bin[a] = 1
    else:
        epsilon_bin[a] = 1

gamma_rate = int("".join(str(int) for int in gamma_bin), 2)
epsilon_rate = int("".join(str(epsilon) for epsilon in epsilon_bin), 2)

power_consumption = gamma_rate * epsilon_rate

print(power_consumption)
