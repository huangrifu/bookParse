from book.RequestBookPage import RequestBookPage
import time
from bs4 import BeautifulSoup
import xlsxwriter
from book.TextPosition import TextPosition

request = RequestBookPage()
workbook = xlsxwriter.Workbook('d:\\book3.xlsx')
xlsSheet = workbook.add_worksheet('sheet1')

request.requestCatalog()
index = 1100
while index < 1300:
    div = request.requestElement(index)
    if div is None or len(div) == 0:
        index = index + 1
        time.sleep(1)
        continue
    # print(div)
    soup = BeautifulSoup(div, 'html')
    imgs = soup.find_all("img")
    imgUrls = ''
    for img in imgs:
        imgUrls = imgUrls + imgs[0].attrs['src'] + "\n"
    xlsSheet.write(index, 1, imgUrls)

    spans = soup.find_all("span")
    texts = {}
    for span in spans:
        styles = span.attrs['style'].split(';')
        txt = TextPosition()
        txt.text = span.contents
        txt.bottom = int(styles[1][8:-2])
        txt.left = int(styles[0][5:-2])
        dic = texts.get(txt.bottom)
        if dic is None:
            dic = []
            texts[txt.bottom] = dic
        dic.append(txt)

    for key in texts:
        texts[key].sort(key=lambda x: x.left)

    rowsKey = sorted(texts.keys(), reverse=True)
    lineText = ''
    for row in rowsKey:
        list = texts.get(row)
        for l in list:
            lineText = lineText + l.text[0]
        lineText = lineText + "\n"
    xlsSheet.write(index, 0, lineText)
    index = index + 1
    # time.sleep(1)
workbook.close()
