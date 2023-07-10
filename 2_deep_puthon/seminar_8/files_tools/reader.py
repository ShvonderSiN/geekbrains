import os


def dirs_walker(dir_):
    dir_ = os.path.abspath(dir_)
    all_path = []
    for root, dirs, files in os.walk(dir_):

        #  считаю размер всей папки
        size_dir = 0
        for ele in os.scandir(root):
            size_dir += os.path.getsize(ele)

        all_path.append({
            "Name": os.path.basename(root),
            "Type": 'Директория',
            "Size": size_dir,
            "Parent Directory": os.path.normpath(os.path.dirname(root))
        })
        #  считаю размер файла
        for file in files:
            type_ = 'Файл'
            size = os.path.getsize(os.path.join(root, file))
            all_path.append({
                "Name": file,
                "Type": type_,
                "Size": size,
                "Parent Directory": os.path.normpath(root)
            })
    return all_path
