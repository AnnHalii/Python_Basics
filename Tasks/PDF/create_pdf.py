
from reportlab.pdfgen import canvas
from reportlab.lib import colors


def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')


fileName = 'Pivo.pdf'
documentTitle = 'Trek pososi'
title = 'Pivo'
subTitle = 'Love pivo!!!'
textLines = [
'Hello, my name is Ann and I very like',
'drink pivo with my friends, alone etc.',
'If you like pivo like me call me please!!!'
]
image = 'pivo.jpg'

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)
# drawMyRuler(pdf)
pdf.setFont('Times-Roman', 36)
pdf.drawCentredString(290, 770, title)
pdf.setFillColor(colors.black)
pdf.setFont("Times-Roman", 24)
pdf.drawCentredString(300,720, subTitle)
pdf.line(30, 710, 550, 710)
text = pdf.beginText(140, 680)
text.setFont("Times-Roman", 18)
text.setFillColor(colors.deepskyblue)
for line in textLines:
    text.textLine(line)

pdf.drawText(text)
pdf.drawInlineImage(image, 0, 0)
pdf.save()