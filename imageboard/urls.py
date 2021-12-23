from django.urls import path
from . import views

urlpatterns = [
    # URL-привязки, то есть привязки URL к методу вида (контроллера)
    path('',             views.index,  name='index'),
    path('d/',           views.board,  name='board'),
    path('d/res/1.html', views.thread, name='thread'),
]
