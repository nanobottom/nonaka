#! python3
# combinePdfs.py - カレントディレクトリの全PDFをひとつのPDFに結合する

import csv
import PyPDF2
import itertools
import os

class combinePdfs:
    """
    カレントディレクトリの全PDFを
    ひとつのPDFに結合する
    """
    def __init__(self):
        self.pdf_files = []
        self.combined_filename = 'combine.pdf'
        self.pdf_writer = PyPDF2.PdfFileWriter()
        self.csv_filename = 'file_list.csv'

    def get_pdf_filename(self):
        """すべてのPDFファイル名を取得する"""
        for filename in os.listdir('.'):
            if filename.endswith('.pdf'):
                self.pdf_files.append(filename)  # ❷
        self.pdf_files.sort(key=str.lower)  # ❸

    def get_pdf_filename_from_csv(self):
        """すべてのPDFファイル名をCSVファイルから取得する"""
        with open(self.csv_filename, 'r', encoding='cp932') as f:
            reader = csv.reader(f)
            self.pdf_files = [e for e in reader]
            self.pdf_files = list(itertools.chain.from_iterable(self.pdf_files))

    def combine_pdf_files(self):
        """リスト化されたファイルを結合する"""
        # すべてのPDFファイルをループする
        for filename in self.pdf_files:
            pdf_file_obj = open(filename, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            # すべてのページをループして追加する
            for page_num in range(pdf_reader.numPages):  # ❶
                page_obj = pdf_reader.getPage(page_num)
                self.pdf_writer.addPage(page_obj)

    def save_combined_pdf_file(self):
        """結合したPDFをファイルに保存する"""
        pdf_output = open(self.combined_filename, 'wb')
        self.pdf_writer.write(pdf_output)
        pdf_output.close()

if __name__ == '__main__':
    combine_pdfs = combinePdfs()
    #combine_pdfs.get_pdf_filename()
    combine_pdfs.get_pdf_filename_from_csv()
    combine_pdfs.combine_pdf_files()
    combine_pdfs.save_combined_pdf_file()

