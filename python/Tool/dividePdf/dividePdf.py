import configparser
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

# configparserの宣言とiniファイルの読み込み
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

# 出力ファイルを作成する
output_dirname = 'output'
try:
    os.mkdir(output_dirname)
except FileExistsError:
    pass

class dividePdf:
    
    def __init__(self):
        self.src_filename = config_ini.get('DEFAULT', 'target_filename')
        self.divide_page = config_ini.getint('DEFAULT', 'divide_page')

    def read_pdf(self):
        pdf_file_obj = open(self.src_filename, 'rb')
        self.src = PdfFileReader(pdf_file_obj, strict=False)

    def divide_pdf(self):
        self.dst1 = PdfFileWriter()
        self.dst2 = PdfFileWriter()
        
        # 1つ目のファイルにPDFのページを追加する
        for page_num in range(self.divide_page):
            self.dst1.addPage(self.src.getPage(page_num))
        
        # 2つ目のファイルにPDFのページを追加する
        for page_num in range(self.divide_page, self.src.numPages):
            self.dst2.addPage(self.src.getPage(page_num))

        # ファイル名を作成する
        basename = self.src_filename.split('.')[0]
        dst1_filename = basename + '_1.pdf'
        dst2_filename = basename + '_2.pdf'

        # outputディレクトリ内のパスを作成する
        dst1_filename = os.path.join(output_dirname, dst1_filename) 
        dst2_filename = os.path.join(output_dirname, dst2_filename) 

        with open(dst1_filename, 'wb') as dst1_pdf:
            self.dst1.write(dst1_pdf)

        with open(dst2_filename, 'wb') as dst2_pdf:
            self.dst2.write(dst2_pdf)

    def divide_each_pdf(self):
        basename = self.src_filename.split('.')[0]
        """対象のPDFを全ページ分割する"""
        for page_num in range(self.src.numPages):
            dst = PdfFileWriter()
            dst.addPage(self.src.getPage(page_num))
            save_filename = basename + '_p' + str(page_num + 1) + '.pdf'
            save_filename = os.path.join(output_dirname, save_filename)
            with open(save_filename, 'wb') as dst_pdf:
                dst.write(dst_pdf)


if __name__ == '__main__':
    divide_pdf = dividePdf()
    divide_pdf.read_pdf()
    if divide_pdf.divide_page != 0:
        divide_pdf.divide_pdf()
    else:
        divide_pdf.divide_each_pdf()
        
