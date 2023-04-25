from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name ="home"),
   path('login', views.login_user, name ="login"),
   path('ork', views.ork, name="ork"),
   path('create', views.create, name="create"),
   path('logout_user', views.logout_user, name='logout'),
   path('saved', views.saved, name='saved'),
   path('xeno', views.xeno, name='xeno'),
   path('imperium', views.imperium, name='imperium'),
   path('chaos', views.chaos, name='chaos'),
   path('sister', views.sister, name='sister'),
   path('krieg', views.krieg, name='krieg'),
]