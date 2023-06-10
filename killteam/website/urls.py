from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name ="home"),
   
   #FUNCTION PATHS
   path('login', views.login_user, name ="login"),
   path('create', views.create, name="create"),
   path('logout_user', views.logout_user, name='logout'),
   path('saved', views.saved, name='saved'),
   
   #XENOS PATHS
   path('xeno', views.xeno, name='xeno'),
   
   #ORKS
   path('ork', views.ork, name='ork'),
   path('ork_update/<list_id>', views.update_ork, name="update-ork"),
   path('delete_ork/<list_id>', views.delete_ork, name="delete-ork"),
   
   #ELDAR
   path('guardian', views.guardian, name='guardian'),
   path('update_guardian/<list_id>', views.update_guardian, name='update-guardian'),
   
   #NIDS
   path('swarm', views.swarm, name='swarm'),
   path('update_swarm/<list_id>', views.update_swarm, name='update-swarm'),
   
   #TAU
   path('ptau', views.ptau, name='ptau'),
   path('update_tau/<list_id>', views.update_tau, name='update-tau'),
   
   #IMPERIUM PATHS
   path('imperium', views.imperium, name='imperium'),
   
   #SOB
   path('sister', views.sister, name='sister'),
   path('update_sister/<list_id>', views.update_sister, name='update-sister'),
   
   #VETERAN GUARDSMAN 
   path('krieg', views.krieg, name='krieg'),
   path('update_krieg/<list_id>', views.update_krieg, name='update-krieg'),
   
   #SPACE MARINES
   path('pm', views.pm, name='pm'),
   path('update_pm/<list_id>', views.update_pm, name='update-pm'),
   
   #CHAOS PATHS
   path('chaos', views.chaos, name='chaos'),
   
   #CHAOS MARINES
   path('cm', views.cm, name='cm'),
   path('update_cm/<list_id>', views.update_cm, name='update-cm'),
   
   # DEATH GUARD
   path('dg', views.dg, name='dg'),
   path('update_dg/<list_id>', views.update_dg, name='update-dg'),
   
   # BLOODIED
   path('bloodied', views.bloodied, name='bloodied'),
   path('update_bloodied/<list_id>', views.update_bloodied, name='update-bloodied'),
]