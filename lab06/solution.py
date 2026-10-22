from collections import defaultdict
def count_by_extension(paths):
    ext_count = defaultdict(int)
    for path in paths:
        if '.' in path:
            ext = path.split('.')[-1].lower()
        else:
            ext = ""
        ext_count[ext] += 1
    return dict(ext_count)

def deepest_path(paths):
    return max(paths, key=lambda path: (path.count('/'), path), default="")

def human_size(n_bytes):
    list_1 = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    for i, unit in enumerate(list_1):
        if n_bytes < 1024:
            return f"{n_bytes:.1f} {unit}" if unit != 'Б' else f"{n_bytes} {unit}"
        n_bytes /= 1024
    return f"{n_bytes:.1f} ТБ"

paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]



    
