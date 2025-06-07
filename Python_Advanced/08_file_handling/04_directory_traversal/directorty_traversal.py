import os

def collect_files(directory, files_by_ext, level=0, max_level=1):
    if level > max_level:
        return
    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)
        if os.path.isfile(path):
            ext = os.path.splitext(entry)[1][1:] or 'no_extension'
            files_by_ext.setdefault(ext, []).append(entry)
        elif os.path.isdir(path) and level < max_level:
            collect_files(path, files_by_ext, level + 1, max_level)

directory = "../"
files_by_ext = {}
collect_files(directory, files_by_ext)

with open(os.path.join(directory, 'report.txt'), 'w') as report:
    for ext in sorted(files_by_ext):
        report.write(f'.{ext}\n')
        for file in sorted(files_by_ext[ext]):
            report.write(f'- - - {file}\n')