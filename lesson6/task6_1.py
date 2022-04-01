with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        request_line = line.split(' ')
        remote_addr = request_line[0]
        request_type = request_line[5][1:]
        requested_resource = request_line[6]
        request_set = (remote_addr, request_type, requested_resource)
        print(request_set)


