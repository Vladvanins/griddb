import os
p_list = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp':[]}, {'autnapp':[]}]}

for key, value in p_list.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))


import yaml
import os

with open('config.yaml') as f:
    content = yaml.safe_load(f)

def create_path(values, prefix=''):
    for directory, paths in values.items():
        dir_path = os.path.join(prefix, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            create_path(paths, dir_path)
        else:
            for i in path:
                if isinstance(i, dict):
                    create_path(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'),  'w') as _:
                        pass

create_path(content)

from os import path, walk, listdir
import shutil

project_name = 'my_project_1'

try:
    for root, dirs, files in walk(project_name):
        if 'templates' in dirs and root != project_name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry),
                                path.join(project_name, 'templates', path.basement(root)))

except FileExistsError:
    print("Already worked with these templates!")