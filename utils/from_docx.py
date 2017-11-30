#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import zipfile

def extract_email_from_docx(docx_name):
    """
    doc_name='xxx.doc(x)'
    return a list of emails
    :param doc_name:
    :return list['xxx@xxx.xxx'...]:
    """
    block_text = ''
    if zipfile.is_zipfile(docx_name):
        fz = zipfile.ZipFile(docx_name, 'r')
        for f in fz.namelist():
            if f.endswith('document.xml'):
                block_text += fz.read(f)

    email_regex = u'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    return re.findall(email_regex, block_text)


def extract_cellphone_from_docx(docx_name):
    """
    doc_name='xxx.doc(x)'
    return a list of cellphone numbers
    :param doc_name:
    :return list['xxxxxxxxxx'...]:
    """
    block_text = ''
    if zipfile.is_zipfile(docx_name):
        fz = zipfile.ZipFile(docx_name, 'r')
        for f in fz.namelist():
            if f.endswith('document.xml'):
                block_text += fz.read(f)

    phone_regex = u'\D([1][3,4,5,7,8][0-9]{9})\D'
    return re.findall(phone_regex, block_text)
