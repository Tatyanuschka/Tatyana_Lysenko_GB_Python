import os
from shutil import copy

main_path = os.path.join(os.path.dirname(__file__), 'my_project')
templ_path = os.path.join(main_path, 'templates')

os.makedirs(templ_path, exist_ok=True)

for root, dirs, files in os.walk(main_path):

    for file in files:
        if file.endswith('html') and root != templ_path:
            sub_dir_name = os.path.split(os.path.abspath(root))[1]
            if sub_dir_name not in os.listdir(templ_path):
                os.makedirs(os.path.join(templ_path, sub_dir_name))

            try:
                copy(os.path.join(root, file),
                     os.path.join(os.path.join(templ_path, sub_dir_name), f'{file[:-5]}.html'))
            except Exception as e:
                pass
