import os
import platform
import zipfile
from datetime import date
class Tree():

    def __init__(self):
        #self.search_path = 'C:/cygwin64/home'
        self.search_path = 'C:/'
        self.tree = dict()
        self.tree_str = str()
        # 保存するファイル名を作成する
        pc_name = platform.uname().node
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
        # ゴミ箱を除く
        #if path != os.path.join(self.search_path, '$RECYCLE.BIN'):
        if path != os.path.join(self.search_path, '$Recycle.Bin'):
            files = list()
            dirs = list()
            dir_list = os.listdir(path)
            for current_dir in dir_list:
                # 隠しフォルダを除く
                if not current_dir.startswith('.'):
                    # ディレクトリか確認する
                    if os.path.isdir(os.path.join(path, current_dir)):
                        dirs.append(current_dir)
                    # ファイルか確認する
                    elif os.path.isfile(os.path.join(path, current_dir)):
                        files.append(current_dir)

            #files = tree[path][0]
            #dirs = tree[path][1]
            if current_depth == 0:
                # ルートを表示する
                self.tree_str += path.rsplit(os.sep, 1)[-1]
                self.tree_str += '\n'
            # ファイルを表示する
            if len(files) != 0:
                for i in range(len(files)):
                    if i != len(files) - 1:
                        self.tree_str += '{0}┣━{1}\n'.format(tab, files[i])
                        #self.tree_str += tab
                        #self.tree_str += '┣━'
                        #self.tree_str += files[i]
                        #self.tree_str += '\n'
                    # 現在のファイルが最後の場合
                    else:
                        if len(dirs) == 0:
                            self.tree_str += '{0}┗━{1}\n'.format(tab, files[i])
                            #self.tree_str += tab
                            #self.tree_str += '┗━'
                            #self.tree_str += files[i]
                            #self.tree_str += '\n'
                        else:
                            self.tree_str += '{0}┣━{1}\n'.format(tab, files[i])
                            #self.tree_str += tab
                            #self.tree_str += '┣━'
                            #self.tree_str += files[i]
                            #self.tree_str += '\n'

            # ディレクトリを表示する
            if len(dirs) != 0:
                for i in range(len(dirs)):
                    if i != len(dirs) - 1:
                        self.tree_str += '{0}┣━{1}\n'.format(tab, dirs[i])
                        #self.tree_str += tab
                        #self.tree_str += '┣━'
                        #self.tree_str += dirs[i]
                        #self.tree_str += '\n'
                        self.mktree(os.path.join(path, dirs[i]),\
                            tree, current_depth=current_depth+1, tab=tab+'┃\t')
                    else:
                        self.tree_str += '{0}┗━{1}\n'.format(tab, dirs[i])
                        #self.tree_str += tab
                        #self.tree_str += '┗━'
                        #self.tree_str += dirs[i]
                        #self.tree_str += '\n'
                        self.mktree(os.path.join(path, dirs[i]),\
                           tree, current_depth=current_depth+1, tab=tab+' \t')

if __name__ == '__main__':
    tree = Tree()
    #tree.walk_dir()
    tree.mktree_str()
    tree.disp_tree()
    tree.write()
    tree.zip_comress()

