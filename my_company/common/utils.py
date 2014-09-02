# -*- coding: utf-8 -*-

import locale

from my_company.my_app.core.models import HouseType, ImageType
from django.conf import settings


locale.setlocale(locale.LC_ALL, '')

def format_vn_currency(number):
    try:
        temp = locale.format("%d", int(number), grouping=True)
        temp = temp.replace(',', '.') + u'đ'
        return temp
    except:
        return str(number)
    
def type_to_image_link(type):
    image_link = '<img src="/static/assets/img/icons/house/%s.png" alt="">'
    if type == HouseType.CHUNG_CU:
        image_link = image_link % 'chungcu'
    elif type == HouseType.NHA_NGUYEN_CAN:
        image_link = image_link % 'nhanguyencan'
    elif type == HouseType.NHA_TRO:
        image_link = image_link % 'nhatro'
    return image_link

def get_image_path(file_name, _type=ImageType.ORIGINAL):
    path = ''
    if _type == ImageType.ORIGINAL:
        path = settings.UPLOADED_FILES + file_name
    elif _type == ImageType.LARGE:
        path = settings.UPLOADED_FILES + 'large/' + file_name
    elif _type == ImageType.MEDIUM:
        path = settings.UPLOADED_FILES + 'medium/' + file_name
    elif _type == ImageType.SMALL:
        path = settings.UPLOADED_FILES + 'small/' + file_name
    return path

def get_image_url(file_name, _type=ImageType.ORIGINAL):
    url = ''
    if _type == ImageType.ORIGINAL:
        url = settings.IMAGE_PATH + file_name
    elif _type == ImageType.LARGE:
        url = settings.IMAGE_PATH + 'large/' + file_name
    elif _type == ImageType.MEDIUM:
        url = settings.IMAGE_PATH + 'medium/' + file_name
    elif _type == ImageType.SMALL:
        url = settings.IMAGE_PATH + 'small/' + file_name
    return url