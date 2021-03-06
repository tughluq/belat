# -*-coding: utf-8 -*-

'''
Created on 2014年7月25日

@author: ABDL
'''

from django.contrib import admin

from polls.models import Poll, Choice


#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        #('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    #list_display = ('question', 'pub_date')
    #list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    


admin.site.register(Poll, PollAdmin)
#admin.site.register(Poll)
admin.site.register(Choice)


