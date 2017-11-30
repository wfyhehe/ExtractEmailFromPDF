#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import csv
from datetime import datetime
from utils.from_doc import extract_cellphone_from_doc, extract_email_from_doc
from utils.from_pdf import extract_cellphone_from_pdf, extract_email_from_pdf


pdf_list = []
doc_list = []
emails = []
phones = []

def process_directory(args, dir_name, file_names):
    for file_name in file_names:
        if file_name.endswith('.pdf'):
            pdf_list.append(file_name)
        elif file_name.endswith('.doc') or file_name.endswith('.docx'):
            doc_list.append(file_name)


os.path.walk('.', process_directory, None)

for pdf in pdf_list:
    emails.extend(extract_email_from_pdf(pdf))
    phones.extend(extract_cellphone_from_pdf(pdf))
for doc in doc_list:
    emails.extend(extract_email_from_doc(doc))
    phones.extend(extract_cellphone_from_doc(doc))

email_csv = ', '.join(set(emails))
phone_csv = ', '.join(set(phones))
now_str = datetime.now().strftime('%Y%m%d%H%M%S')

with open('emails-{datetime}.csv'.format(datetime=now_str), 'w') as f:
    f.write(email_csv)

with open('phones-{datetime}.csv'.format(datetime=now_str), 'w') as f:
    f.write(phone_csv)