from django.urls import path, include
from .views import *

app_name = 'GoodCook'

urlpatterns = [
    path('Korean/', KoreanListView.as_view(), name='Korean'),
    path('China/', ChinaListView.as_view(), name='China'),
    path('Western/', WesternListView.as_view(), name='Western')
]