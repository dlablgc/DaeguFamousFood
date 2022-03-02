from re import template
from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class KoreanListView(ListView):
    model = Korean
    template_name = 'GoodCook/Korean.html'
    context_object_name = 'Korean_list'

class ChinaListView(ListView):
    model = China
    template_name = 'GoodCook/China.html'
    context_object_name = 'China_list'

    
class WesternListView(ListView):
    model = Western
    template_name = 'GoodCook/Western.html'
    context_object_name = 'Western_list'
 
        