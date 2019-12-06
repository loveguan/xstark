#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: stark.py

@time: 2019-12-06 8:09

@desc:

'''
from stark.service.stark import site, ModelStark

from .models import *
from django.forms import ModelForm
from django.forms import widgets as wid

class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        labels = {
            "title": "书籍名称",
            "price": "价格"
        }
class AuthorModelForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class BookConfig(ModelStark):

    list_display = ["title", "price", "publishDate"]
    list_display_links = ["price"]
    modelform_class = BookModelForm

class AuthorConfig(ModelStark):
    list_display = ['name','age']
    # 使用默认的modelform，注释掉自己写的
    # modelform_class = AuthorModelForm

site.rigister(Book, BookConfig)
site.rigister(Publish)
site.rigister(Author,AuthorConfig)
site.rigister(AuthorDetail)
