from PyPDF2 import PdfFileWriter, PdfFileReader

class devidePdf:
    
    def __init__(self):
        self.src_filename = 'meetingminutes.pdf'
        #self.src
        #self.dst1
        #self.dst2
        self.dst1_filename = 'output1.pdf'
        self.dst2_filename = 'output2.pdf'
        self.devide_page = 2

    def read_pdf(self):
        pdf_file_obj = open(self.src_filename, 'rb')
        self.src = PdfFileReader(pdf_file_obj, strict=False)

    def devide_pdf(self):
        self.dst1 = PdfFileWriter()
        self.dst2 = PdfFileWriter()
        
        # 1つ目のファイルにPDFのページを追加する
        for page_num in range(self.devide_page):
            self.dst1.addPage(self.src.getPage(page_num))
        
        # 2つ目のファイルにPDFのページを追加する
        for page_num in range(self.devide_page, self.src.numPages):
            self.dst2.addPage(self.src.getPage(page_num))

    def save_pdfs(self):
        with open(self.dst1_filename, 'wb') as dst1_pdf:
            self.dst1.write(dst1_pdf)

        with open(self.dst2_filename, 'wb') as dst2_pdf:
            self.dst2.write(dst2_pdf)


if __name__ == '__main__':
    devide_pdf = devidePdf()
    devide_pdf.read_pdf()
    devide_pdf.devide_pdf()
    devide_pdf.save_pdfs()
        



