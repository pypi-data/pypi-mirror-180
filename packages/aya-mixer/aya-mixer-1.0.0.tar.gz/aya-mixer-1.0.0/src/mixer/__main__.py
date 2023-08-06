from bs4 import BeautifulSoup
import random
import functools
import re
from datetime import datetime
import copy
import unittest
import sys



# python3 test_many.py de_chua_tron_091122.html 4
# n = len(sys.argv)
# INPUTFILE = sys.argv[1] or 'de_chua_tron_091122.html'
# N = int(sys.argv[2]) or 4
# INPUTFILE = 'de_chua_tron_091122.html'
# N = 4

# the file path depends on the config
# pytest runs from the main dir, so "./mixer2/de_chua_tron_091122.html"
# if you run `python3 test_many.py` the path might just be 'de_chua_tron_091122.html'
def main():
    INPUTFILE = sys.argv[1] or 'de_chua_tron_091122.html'
    N = int(sys.argv[2]) or 4

    htmlfile = open(INPUTFILE)
    index = htmlfile.read()

    # S0 = BeautifulSoup(index, 'lxml')
    S0 = BeautifulSoup(index, 'html.parser')

    body0 = S0.find('body')

    header = []
    for i in body0:
        if str(i).find('Câu') < 0:
            header.append([i])
        else:
            break

    footer = []
    fp = 0
    for i,e in enumerate(body0):
        if str(e).find('ẾT') >= 0:
            fp = i
            break
    for i,e in enumerate(body0):
        if i >= fp:
            footer.append(e)

    def test_file():
        assert len(S0) > 0
        assert len(body0) > 0
        assert len(header) > 0
        assert len(footer) > 0

    def shuffle_qs_array(body):
        qs = []
        for i in body:
            if str(i).find('ẾT') >= 0:
                break
            elif str(i).find('Câu') >= 0:
                qs.append([i])
            else:
                if len(qs) < 1:
                    continue
                else:
                    qs[-1].append(i)
        random.shuffle(qs)
        return qs

    def test_qs_array():
        assert len(shuffle_qs_array(body0)) > 0

    qss = []
    for i in range (N):
        qss.append(shuffle_qs_array(body0))

    def test_N():
        assert len(qss) == N

    mixeds = []
    testIDs = []

    for i in range(N):

        mixed = []
        correctAns = []

        ANS = ['A', 'B', 'C', 'D']

        def add_bold():
            b = S0.new_tag('b')
            b.string = f'Câu {i+1}:'
            newq = S0.new_tag('p')
            newq.insert(0, b)
            return newq

        qs = qss[i]
        for i, q in enumerate(qs):
            newq = add_bold()

            imgp = S0.new_tag('p')
            imgs = q[2].find_all('img')
            gs = []
            for img in imgs:
                if 'height' in img.attrs:
                    if int(img.attrs['height']) >= 40:
                        gs.append(img)
            if len(gs) >= 1:
                for g in gs:
                    lp = len(imgp)
                    imgp.insert(lp, g)


            newq.insert(len(newq), imgp)

            newq.insert(len(newq), q[2])

            if len(q) >= 12:
                ans = [q[4], q[6], q[8], q[10]]
                random.shuffle(ans)

                for i in range(len(ans)):
                    a = ans[i]

                    s = str(a)

                    u1 = s.find('<u>')
                    u2 = s.find('</u>')

                    if u1 >= 0 and u2 >= 0:
                        correctAns.append(ANS[i])
                        s = s[:u1]+ s[u1+3:u2] + s[u2+4:]

                    dots = [dot.start() for dot in re.finditer('\.', s)]
                    if len(dots) == 0:
                        continue
                    dot1 = dots[0]
                    dot2 = dots[-1]

                    position = s.find(s[dot1-1:dot1])

                    newan = s[:position] + ANS[i] + s[position+1:]



                    newantag = S0.new_tag('p')
                    newantag.insert(0, BeautifulSoup(newan, 'html.parser'))
                    
                    newq.insert(len(newq), newantag)
            else:
                table = q[4]
                tds = table.find_all('td')
                random.shuffle(tds)

                newans = []
                for i, td in enumerate(tds):
                    s = str(td)
                    if s.find('<u>') >= 0 and s.find('</u>') >= 0:
                        correctAns.append(ANS[i])
                    dots = [dot.start() for dot in re.finditer('\.', s)]
                    dot1 = dots[0]
                    dot2 = dots[-1]

                    newan = ANS[i] + s[dot1:dot2]
                    newantag = S0.new_tag('td', attrs={"style":"border: none; padding: 0in", "width":"25%"})
                    newantag.insert(0, BeautifulSoup(newan, 'html.parser'))
                    newans.append(newantag)
                newtable = S0.new_tag('table', attrs={"cellpadding":"0", "cellspacing":"0", "width":"100%"})
                newcol1 = S0.new_tag('col', attrs={"width":"64"})
                newcol2 = S0.new_tag('col', attrs={"width":"64"})
                newcol3 = S0.new_tag('col', attrs={"width":"64"})
                newcol4 = S0.new_tag('col', attrs={"width":"64"})
                newtr = S0.new_tag('tr', attrs={"valign":"top"})

                newtable.insert(0, newcol1)
                newtable.insert(1, newcol2)
                newtable.insert(2, newcol3)
                newtable.insert(3, newcol4)
                newtable.insert(4, newtr)


                for an in newans:
                    newtable.insert(len(newtable), an)
                
                newq.insert(len(newq), newtable)

            mixed.append(newq)
        mixeds.append(mixed)

        testID = random.randint(0,99)
        if testID <10:
            id = '00' + str(testID)
        else:
            id = '0' + str(testID)

        testIDs.append(id)

        with open(f'de_da_tron_{id}.html', 'w') as f:
            f.write("<!DOCTYPE html><head></head><body>")
            for i in header:
                f.write(str(i[0]))

            for e in mixed:
                f.write(str(e))

            for i in footer:
                f.write(str(i))

            f.write("</body></html>")


    with open('cau_tra_loi.docx', 'a') as f:
        utc_now = datetime.now()
        f.write(utc_now.strftime("%m/%d/%Y, %H:%M:%S"))
        f.write('\n')
        for id in testIDs:
            f.write(f'MÃ ĐỀ: {id}\n')
            for i, an in enumerate(correctAns):
                f.write(f'Câu {i+1}: {an}\n')
            f.write('\n')
        f.write('---\n')    

if __name__ == "__main__":
    main()