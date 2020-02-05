from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
'''
将多张图片按照顺序合并成pdf
@Leon Guo 
'''
def convert_images_to_pdf(img_path, pdf_path,page_wdith,page_height):
    pages = 0
    c = canvas.Canvas(pdf_path, pagesize = (page_wdith,page_height))
    for i in range(1,180):
        pic = img_path+str(i)+'.png'
        print('processing page: ',pic)
        c.drawImage(pic, 0, 0, page_wdith, page_height)
        c.showPage()
        pages = pages + 1
    c.save()
    print('done!')

if __name__ == "__main__":
    # paras： 图片位置，pdf 位置，图片宽，高
    convert_images_to_pdf('book/', 'book/algBook.pdf',1324, 1658)