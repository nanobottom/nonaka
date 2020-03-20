import os
import zipfile
from datetime import date
class Tree():

    def __init__(self):
        self.search_path = '/home/nanob/git/nonaka/python/WebServer'
        self.tree = dict()
        self.tree_str = str()
        # 保存するファイル名を作成する
        pc_name = os.uname().nodename
        name = '野中'
        today = date.today().strftime('%Y%m%d')
        self.filename = today + name + '_' + pc_name + '_tree.txt'

    def walk_dir(self):
        for dirpath, dirs, files in os.walk(self.search_path):
            self.tree[dirpath] = (files, dirs)

    def mktree_str(self):
        self.mktree(self.search_path, self.tree)

    def disp_tree(self):
        print(self.tree_str)

    def write(self):
        with open(self.filename, 'w') as f:
            f.write(self.tree_str)
    
    def zip_comress(self):
        with zipfile.ZipFile(self.filename.rsplit('.')[0] + '.zip',\
                 'w', compression=zipfile.ZIP_DEFLATED) as f:
            f.write(self.filename)
        os.remove(self.filename)

    def mktree(self, path, tree, current_depth=0, tab=''):
        files = tree[path][0]
        dirs = tree[path][1]
        if current_depth == 0:
            # ルートを表示する
            self.tree_str += path.rsplit(os.sep, 1)[-1]
            self.tree_str += '\n'
        # ファイルを表示する
        if len(files) != 0:
            for i in range(len(files)):
                if i != len(files) - 1:
                    self.tree_str += tab
                    self.tree_str += '┣━'
                    self.tree_str += files[i]
                    self.tree_str += '\n'
                # 現在のファイルが最後の場合
                else:
                    if len(dirs) == 0:
                        self.tree_str += tab
                        self.tree_str += '┗━'
                        self.tree_str += files[i]
                        self.tree_str += '\n'
                    else:
                        self.tree_str += tab
                        self.tree_str += '┣━'
                        self.tree_str += files[i]
                        self.tree_str += '\n'

        # ディレクトリを表示する
        if len(dirs) != 0:
            for i in range(len(dirs)):
                if i != len(dirs) - 1:
                    self.tree_str += tab
                    self.tree_str += '┣━'
                    self.tree_str += dirs[i]
                    self.tree_str += '\n'
                    self.mktree(os.path.join(path, dirs[i]),\
                        tree, current_depth=current_depth+1, tab=tab+'┃\t')
                else:
                    self.tree_str += tab
                    self.tree_str += '┗━'
                    self.tree_str += dirs[i]
                    self.tree_str += '\n'
                    self.mktree(os.path.join(path, dirs[i]),\
                       tree, current_depth=current_depth+1, tab=tab+' \t')

if __name__ == '__main__':
    tree = Tree()
    tree.walk_dir()
    tree.mktree_str()
    tree.disp_tree()
    tree.write()
    tree.zip_comress()

