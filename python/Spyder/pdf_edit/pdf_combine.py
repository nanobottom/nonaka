# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 07:51:47 2020

@author: nonaka.ryo
"""
from pathlib import Path
import PyPDF2
import os

def merge_pdf_files(folder_path, file_path, is_reverse):
    # フォルダ内のPDFファイル一覧
    pdf_dir = Path(folder_path)
    pdf_files = sorted(pdf_dir.glob('*.pdf'), reverse=is_reverse)
    
    # 1つのPDFファイルにまとめる
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
        for num_page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(num_page))
    
    # 結合したPDFファイルを保存する
    with open(file_path, 'wb') as f:
        pdf_writer.write(f)
            

if __name__ == '__main__':
    merge_pdf_files(os.getcwd(), 'combine.pdf', False)
