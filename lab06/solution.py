from collections import defaultdict
def count_by_extension(paths):
    ext_count = defaultdict(int)
    for path in paths:
        if '.' in path and path[0] != '.':
            ext = path.rsplit('.')[-1].lower()
            print(ext)
        else:
            ext = ""
        ext_count[ext] += 1
    return dict(ext_count)
print(count_by_extension(["archive.tar.gz", ".gitig"]))

def deepest_path(paths):
    l = sorted([t for t in paths], key = lambda x: -(x.count('/')))
    if len(l)!=0:
        return l[0]
    else:
        return ""

def human_size(n_bytes):
    list_1 = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    for i, unit in enumerate(list_1):
        if n_bytes < 1024:
            return f"{n_bytes:.1f} {unit}" if unit != 'Б' else f"{n_bytes} {unit}"
        n_bytes /= 1024
    return f"{n_bytes:.1f} ТБ"

paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]



    
