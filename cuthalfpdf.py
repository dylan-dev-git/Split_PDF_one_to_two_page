import sys, os, pdfrw
writer = pdfrw.PdfWriter()
for page in pdfrw.PdfReader('aaa.pdf').pages:
    for y in [0, 0.5]:
        newpage = pdfrw.PageMerge()    
        newpage.add(page, viewrect=(y, 0, 0.5, 1))
        writer.addpages([newpage.render()])
writer.write('output.pdf')

# x1 y1 x2 y2
# 0  0   1 0.5  // 첫반
# 0  0.5 1 0.5  // 뒷반

# 0  0   1 1

# 0   0  0.5  1
# 0.5 0  0.5  1