def ip_count_dict(file):
    """function to create a dict, where keys are IP addresses from the file
       and values - their counts in file"""
    with open(file, 'r', encoding='utf-8') as f:
        ip_dict = {}
        for line in f:
            remote_addr = line.split(' ')[0]
            if remote_addr in ip_dict:
                ip_dict[remote_addr] += 1
            else:
                ip_dict[remote_addr] = 1
    return ip_dict


def ip_max_count(any_dict):
    """this function to define the max value in dict"""
    max_count = 1
    for key, val in any_dict.items():
        if val > max_count:
            max_count = val
    return max_count


def dict_key_found(any_dict, val):
    """function return the key of dictionary with certain value"""
    for key, value in any_dict.items():
        if val == value:
            return key


ip_dict = ip_count_dict('nginx_logs.txt')
print(f'IP спамер - {dict_key_found(ip_dict, ip_max_count(ip_dict))}, кол-во запросов - {ip_max_count(ip_dict)}')
