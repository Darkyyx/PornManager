import os


def prt_dir(rootpath, symbol=''):
    for root, dirs, files in os.walk(rootpath):
        path = root.split('/')
        print((len(path) - 1) * symbol, os.path.basename(root))
        for file in files:
            print(len(path) * symbol, file)


if __name__ == '__main__':
    rootpath = input("请输入目录：")
    prt_dir(rootpath, '--')
