in1 = open("C:/Users/earam/Desktop/adventofcode22/day3input.txt","r")

## PART 1
sum_priorities = 0

for line in in1:
    line = line.strip()
    n = int(len(line)/2)
    sac1 = line[0:n]
    sac2 = line[n:len(line)]
    for i in sac1:
        if i in sac2 and i.islower():
            priority = ord(i) - 96
            sum_priorities += priority
            #print(priority)
            break
        elif i in sac2 and i.isupper():
            priority = ord(i) - 38
            sum_priorities += priority
            #print(priority)
            break

print("The sum of priorities for items in both sacs is {}".format(sum_priorities))
in1.close()

in1 = open("C:/Users/earam/Desktop/adventofcode22/day3input.txt","r")
## PART 2
group_counter = 0
line_dict = dict()
sum_priorities = 0
for line in in1:
    line = line.strip()
    group_counter += 1
    line_dict[group_counter] = line

    if group_counter % 3 == 0:
        elf1 = line_dict[group_counter - 2]
        elf2 = line_dict[group_counter - 1]
        elf3 = line_dict[group_counter]
        for i in elf1:
            if i in elf2 and i in elf3:
                if i.islower():
                    priority = ord(i) - 96
                    sum_priorities += priority
                    #print(priority)
                    break
                elif i.isupper():
                    priority = ord(i) - 38
                    sum_priorities += priority
                    #print(priority)
                    break


print("The sum of priorities for badge items is {}".format(sum_priorities))
