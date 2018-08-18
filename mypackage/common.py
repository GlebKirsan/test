import os


def get_prefix(name):
    end_of_prefix = 4
    return '.'.join(name.split('.')[:end_of_prefix])


def build_dirs(directory):
    path_to = {
        file_name: os.path.join(directory, file_name) for file_name in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, file_name))
    }
    for i in ['opt', 'jsn', 'png']:
        if i not in path_to:
            new_dir = os.path.join(directory, i)
            os.mkdir(new_dir)
            path_to[i] = new_dir
    path_to['parent'] = directory
    return path_to