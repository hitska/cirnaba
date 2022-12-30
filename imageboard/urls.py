from django.urls import path
from . import views

urlpatterns = [
    # URL-привязки, то есть привязки URL к методу вида (контроллера)
    path('',                                             views.index,    name='index'),
    path('<str:board_address>/',                         views.board,    name='board'),
    path('<str:board_address>/res/<int:thread_id>.html', views.thread,   name='thread'),
    path('cgi-bin/wakaba.pl/<str:board_address>/',       views.add_post, name='add_post'),
]
