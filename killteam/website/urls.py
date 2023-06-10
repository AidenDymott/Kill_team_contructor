from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name ="home"),
   path('login', views.login_user, name ="login"),
   path('create', views.create, name="create"),
   path('logout_user', views.logout_user, name='logout'),
   path('saved', views.saved, name='saved'),
   path('xeno', views.xeno, name='xeno'),
   path('guardian', views.guardian, name='guardian'),
   path('swarm', views.swarm, name='swarm'),
   path('imperium', views.imperium, name='imperium'),
   path('sister', views.sister, name='sister'),
   path('update_sister/<list_id>', views.update_sister, name='update-sister'), 
   path('krieg', views.krieg, name='krieg'),
   path('pm', views.pm, name='pm'),
   path('chaos', views.chaos, name='chaos'),
   path('ork', views.ork, name='ork'),
   path('ork_update/<list_id>', views.update_ork, name="update-ork"),
   path('delete_ork/<list_id>', views.delete_ork, name="delete-ork"),
   path('cm', views.cm, name='cm'),
   path('dg', views.dg, name='dg'),
   path('bloodied', views.bloodied, name='bloodied'),
]