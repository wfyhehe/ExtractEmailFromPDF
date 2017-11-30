#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os

from datetime import datetime
from utils.from_docx import extract_cellphone_from_docx, extract_email_from_docx
from utils.from_pdf import extract_cellphone_from_pdf, extract_email_from_pdf
from utils.from_txt import extract_cellphone_from_txt, extract_email_from_txt

now_str = datetime.now().strftime('%Y%m%d%H%M%S')
OUTPUT_CSV = 'output_csv'
pdf_list = []
docx_list = []
txt_list = []
emails = []
phones = []


def process_directory(args, dir_name, file_names):
    for file_name in file_names:
        if file_name.endswith(u'.pdf'):
            pdf_list.append(u'{dir}/{file}'.format(dir=dir_name, file=file_name))
        elif file_name.endswith(u'.docx') or file_name.endswith(u'.zip'):
            docx_list.append(u'{dir}/{file}'.format(dir=dir_name, file=file_name))
        elif file_name.endswith(u'.txt'):
            txt_list.append(u'{dir}/{file}'.format(dir=dir_name, file=file_name))
        elif file_name.endswith(u'.doc'):
            logging.error('can\'t process "%s", please convert to .docx or .pdf or .txt' % file_name)


os.path.walk(u'.', process_directory, None)

for pdf in pdf_list:
    try:
        emails.extend(extract_email_from_pdf(pdf))
    except:
        pass
    try:
        phones.extend(extract_cellphone_from_pdf(pdf))
    except:
        pass
for docx in docx_list:
    try:
        emails.extend(extract_email_from_docx(docx))
    except:
        pass
    try:
        phones.extend(extract_cellphone_from_docx(docx))
    except:
        pass
        
for txt in txt_list:
    try:
        emails.extend(extract_email_from_txt(txt))
    except:
        pass
    try:
        phones.extend(extract_cellphone_from_txt(txt))
    except:
        pass
    

email_csv = ','.join(set(emails))
phone_csv = ','.join(set(phones))

try:
    os.mkdir(OUTPUT_CSV)
except:
    pass

with open('{dir}/emails-{datetime}.csv'.format(dir=OUTPUT_CSV, datetime=now_str), 'w') as f:
    f.write(email_csv)

with open('{dir}/phones-{datetime}.csv'.format(dir=OUTPUT_CSV, datetime=now_str), 'w') as f:
    f.write(phone_csv)
