old_msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_msg = []

for item in old_msg:
    if item[1:].isdigit() and (item[0] == '+' or item[0] == '-'):
        msg_part = ['"', item[0], str(int(item[1:]) // 10), str(int(item[1:]) % 10), '" ']
        new_msg.extend(msg_part)
    elif not item.isdigit():
        new_msg.append(item)
        new_msg.append(' ')
    else:
        msg_part = ['"', str(int(item) // 10), str(int(item) % 10), '" ']
        new_msg.extend(msg_part)

print(''.join(new_msg))
