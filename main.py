#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator

blockText = ''
fp = open('email.pdf', 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    pdfResourceManager = PDFResourceManager()
    laParams = LAParams()
    device = PDFPageAggregator(pdfResourceManager, laparams=laParams)
    interpreter = PDFPageInterpreter(pdfResourceManager, device)
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        layout = device.get_result()
        for x in layout:
            if isinstance(x, LTTextBoxHorizontal):
                blockText += x.get_text().encode('utf-8')

print blockText
