from django.urls import path
from . import views

urlpatterns = [
    # URL-привязки, то есть привязки URL к методу вида (контроллера)
    path('',                                          views.index,  name='index'),
    path('<str:board_name>/',                         views.board,  name='board'),
    path('<str:board_name>/res/<int:thread_id>.html', views.thread, name='thread'),
]
