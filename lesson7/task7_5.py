def get_file_stat(path):
    """function return the dictionary where key is the upper
    limit of file size (rounded to 1000) and
    value is amount of files with size under this limit and file's extensions"""
    file_size_dict = {0: [0, []]}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            key = ceil(file_size / 1000) * 1000
            file_mode = os.path.splitext(file)[1]
            if key in file_size_dict.keys():

                file_size_dict[key][0] += 1
                if file_mode not in file_size_dict[key][1]:
                    file_size_dict[key][1].append(file_mode)
            else:
                file_size_dict[key] = [1, []]
                file_size_dict[key][1].append(file_mode)

    for key, val in file_size_dict.items():
        file_size_dict[key] = tuple(val)

    return file_size_dict


def file_stat_to_File(any_dict, path):
    with open(os.path.join(path, 'file_stat.json'), 'w', encoding='utf-8') as f:
        json.dump(any_dict, f)


if __name__ == '__main__':
    import os
    from math import ceil
    import json

    # size_stat = get_file_stat(os.path.join(os.path.dirname(__file__), 'some_data'))
    size_stat = get_file_stat(r'C:\Users\tatya\OneDrive\Documents\GeekBrains\Основы')
    for key, val in size_stat.items():
        print(f'Размер {key} имеют {val[0]} файлов с расширениями {val[1]}')
    file_stat_to_File(size_stat, os.path.dirname(__file__))
