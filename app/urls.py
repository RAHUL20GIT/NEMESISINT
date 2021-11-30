from django.conf.urls import url
from django.urls import path
from django.urls import path,include,re_path
from . import views


urlpatterns=[
    path('lgn',views.loginuser,name='lgn'),
    path('lgt',views.logoutuser,name='lgt'),
    path('rgstr',views.register,name='rgstr'),
    path('home',views.home,name='home'),
    path('edit',views.edit,name='edit'),
    path('dltusr',views.deleteuser,name='dltusr'),
    #path('%s?next=%s',views.sessionexpired,name='expr'),
    re_path(r'^accounts/login',views.sessionexpired,name='expr'),
]