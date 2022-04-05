import os

ROOT = os.path.dirname(__file__)
dir_names = ['settings', 'mainapp', 'adminapp', 'authapp']
main_dir = 'my_project2'
main_dir_path = os.path.join(ROOT, main_dir)
dir_paths = [os.path.join(main_dir, item) for item in dir_names]
if os.path.exists(main_dir_path):
    for item in dir_names:
        if item not in os.listdir(main_dir_path):
            os.makedirs(os.path.join(main_dir, item))
else:
    for item in dir_paths:
        os.makedirs(item)
