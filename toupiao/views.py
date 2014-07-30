# -*-coding: utf-8 -*-

'''
Created on 2014年7月25日

@author: ABDL
'''

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")