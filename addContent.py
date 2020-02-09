'''
add content to PDF
@Leon Guo
'''
import fitz
import re 

pdf_path = 'book/alg.pdf' 
content_path = 'book/contentData.txt' 
offset = 8


'''
从文本中获取目录 
使用正则表达式获得 标题层级 标题 页码
如果需要用在其他目录上 需要改变正则规则 
'''
def readContentText():
    with open(content_path,'r') as f:
        lines = f.readlines() 
        for line in lines:
            line =line.strip() # 移除字符串头尾空格  
            if re.match('Chapter',line):# 通过chapter 字符判断是否为一级目录
               res = re.match('(Chapter.*)\s(\d*)',line) 
                
               global offset
               if int(res.group(2))==45:   
                   offset = 7 # 为什么会有一行这么奇怪的代码呢？ 
                   #因为你仔细查看会发现 这本书没有44页 从这里开始每个目录都少一页 手动补上
               if int(res.group(2))==87:    
                   offset = 6 # 是的 也没有86 写到这我已经开始后悔写这个代码了 不如手动
               if int(res.group(2))==137:    
                   offset = 5 
               if int(res.group(2))==157:
                   offset = 4 # 已自闭
                   
               level1 = [1,res.group(1),int(res.group(2))+ offset]
               content_list.append(level1)
               print(level1)
            else:
                res = re.match('(.*)\s(\d*)',line)
                level2 = [2,res.group(1),int(res.group(2))+ offset]
                content_list.append(level2)
                print(level2)



if __name__ == "__main__":
    pdf = fitz.open(pdf_path)
    content_list = pdf.getToC()
    print(f"Current Content:{content_list}")
    content_list.append([1,'Cover',1])
    content_list.append([1,'Contents',5])
    content_list.append([1,'Preface',7])
    readContentText()
    print(f"Current Content:{content_list}")
    pdf.setToC(content_list)
    pdf.save('book/Alg_content.pdf')