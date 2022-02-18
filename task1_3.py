numbers = []
end1 = 'а'
end2 = 'ов'
for i in range(1, 101):
    percent = 'процент'
    if i % 10 > 1 and i % 10 < 5 and i // 10 != 1:
        percent += end1
    elif i % 10 > 4 or i % 10 == 0 or i // 10 == 1:
        percent += end2
    numbers.append(str(i) + ' ' + percent)

for number in numbers:
    print(number)
