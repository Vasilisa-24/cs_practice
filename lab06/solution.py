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


    
