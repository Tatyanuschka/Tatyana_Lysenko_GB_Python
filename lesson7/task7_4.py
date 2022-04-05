def get_file_size_stat(path):
    """function return the dictionary where key is the upper
    limit of file size (rounded to 1000) and
    value is amount of files with size under this limit"""
    file_size_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            key = ceil(file_size / 1000) * 1000
            if key in file_size_dict.keys():
                file_size_dict[key] += 1
            else:
                file_size_dict[key] = 1

    return file_size_dict


if __name__ == '__main__':
    import os
    from math import ceil

    size_stat = get_file_size_stat(r'C:\Program Files\GIMP 2')
    for key, val in size_stat.items():
        print(f'Размер {key} имеют {val} файлов')
