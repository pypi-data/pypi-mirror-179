import os
def mk_file(path: str):
		f = open(path, 'w')
		f.close()

def wr_file(path: str, text: str):
    f = open(path, 'w')
    f.write(text)
    f.close()

def rm_file(path: str, newname: str):
    os.rename(path, newname)

def rm_file(path: str):
    os.remove(path)

def mk_dir(path: str):
    os.mkdir(path)

def rm_dir(path: str):
    os.rmdir(path)

def rn_dir(path: str, newname: str):
    os.rename(path, newname)

def exists(path: str):
    if os.path.exists(path):
        return True
    else:
        return False

def filesize(path: str):
    return os.path.getsize(path)

def atime(path: str):
    return os.path.getatime(path)

def ctime(path: str):
    return os.path.getctime(path)

def mtime(path: str):
    return os.path.getmtime(path)