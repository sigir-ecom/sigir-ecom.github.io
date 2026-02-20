with open('acceptedPapersOrdered.tsv', 'r') as fip:
    lines=fip.readlines()

print lines[1].split('\t')


#<li><strong style="color:rgb(141, 36, 36)"><font color=#194B7>1. Did We Get It Right? Predicting Query Performance in E-commerce Search</font><font color="#8d2424"> &nbsp;</font><font color="#2a2a2a">[<a href="./ecom18Papers/paper23.pdf">PDF</a>]</font></strong></li><font color="#ee0979">
#                      <b>Rohan Kumar, Mohit Kumar, Neil Shah and Christos Faloutsos</b>
#                      </b></font>
num=1
with open('op.txt','w') as fop:
    for submission in lines[1:]:
        try:
            splits=submission.split('\t')
            paperid=splits[0]
            authors=splits[1]
            title=splits[2]
            line1= '<li><strong style="color:rgb(141, 36, 36)"><font color=#194B7>'+'&nbsp;&nbsp;&nbsp;'*(2-len(str(num)))+str(num)+'. '+title+'</font><font color="#8d2424"> &nbsp;</font><font color="#2a2a2a">[<a href="./ecom19Papers/paper'+paperid+'.pdf"" target="_blank">PDF</a>]</font></strong></li><font color="#ee0979">'
            line2= '<b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+authors+'</b>'
            line3= '</b></font>'
            fop.write(line1+'\n'+line2+'\n'+line3+'\n')
            num+=1
        except:
            print submission