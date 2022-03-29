old_msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

x = 0
while x < len(old_msg):
    if old_msg[x].find('+') != -1 or old_msg[x].find('-') != -1:
        old_msg.insert(x, ' "')
        old_msg.insert(x + 1, old_msg[x + 1][0])
        old_msg.insert(x + 2, str(int(old_msg[x + 2][1:]) // 10))
        old_msg.insert(x + 3, str(int(old_msg[x + 3][1:]) % 10))
        old_msg.insert(x + 4, '" ')
        del old_msg[x + 5]
        x += 5
    elif old_msg[x].isdigit():
        old_msg.insert(x, ' "')
        old_msg.insert(x + 1, str(int(old_msg[x + 1]) // 10))
        old_msg.insert(x + 2, str(int(old_msg[x + 2]) % 10))
        old_msg.insert(x + 3, '" ')
        del old_msg[x + 4]
        x += 4
    else:
        old_msg[x] = ' ' + old_msg[x]
        x += 1

print(''.join(old_msg))
