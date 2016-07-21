import os


def prt_dir(path, indent_symbol='', level=0):
    print(indent_symbol*level, os.path.basename(path))

    if os.path.isdir(path):
        for f in os.listdir(path):
            fpath = os.path.join(path, f)
            prt_dir(fpath, indent_symbol, level+1)

if __name__ == '__main__':
    rootpath = input("请输入目录：")
    prt_dir(rootpath, '--', 0)
