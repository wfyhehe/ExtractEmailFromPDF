#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.from_docx import extract_cellphone_from_docx, extract_email_from_docx
from utils.from_pdf import extract_cellphone_from_pdf, extract_email_from_pdf

emails1 = extract_email_from_docx('email.docx')  # [u'123456@qq.com',...]
emails2 = extract_email_from_pdf('email.pdf')  # ['123456@qq.com',...]

phones1 = extract_cellphone_from_docx('phone.docx')  # [u'1333333333',...]
phones2 = extract_cellphone_from_pdf('phone.pdf')  # ['1333333333',...]

print emails1
print emails2
print phones1
print phones2
