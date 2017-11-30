#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator


def extract_email_from_pdf(pdf):
    """
    pdf='xxx.pdf'
    return a list of emails
    :param pdf:
    :return list['xxx@xxx.xxx'...]:
    """
    block_text = ''
    fp = open(pdf, 'rb')
    try:
        parser = PDFParser(fp)
    except:
        return ''
    document = PDFDocument(parser)
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        pdf_resource_manager = PDFResourceManager()
        la_params = LAParams()
        device = PDFPageAggregator(pdf_resource_manager, laparams=la_params)
        interpreter = PDFPageInterpreter(pdf_resource_manager, device)
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    block_text += x.get_text().encode('utf-8')

    email_regex = u'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    return re.findall(email_regex, block_text)


def extract_cellphone_from_pdf(pdf):
    """
    pdf='xxx.pdf'
    return a list of cellphone numbers
    :param pdf:
    :return list['xxxxxxxxxx'...]:
    """
    block_text = ''
    fp = open(pdf, 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        pdf_resource_manager = PDFResourceManager()
        la_params = LAParams()
        device = PDFPageAggregator(pdf_resource_manager, laparams=la_params)
        interpreter = PDFPageInterpreter(pdf_resource_manager, device)
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    block_text += x.get_text().encode('utf-8')

    phone_regex = u'\D([1][3,4,5,7,8][0-9]{9})\D'
    return re.findall(phone_regex, block_text)

