from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('diet',views.T,name ='T'),
    url('signup',views.signup,name='signup'),
    path('user_login',views.user_login,name='user_login'),
    url('aboutus',views.aboutus,name='aboutus'),
    url('edit_profile',views.edit_profile,name='edit_profile'),
    url('save_edit',views.save_edit,name='save_edit'),
    url('undefine',views.undefine,name='undefine'),
    url('adddata',views.adddata,name='adddata'),
    url('checkout',views.checkout,name="checkout"),
    url('cushome',views.cushome,name="cushome"),
    url('logmeout',views.logmeout,name="logmeout"),
    url('exerscise',views.exerscise,name="exerscise"),
    url('dietplan',views.dietplan,name="dietplan"),
    url('showpackage',views.showpackage,name="showpackage"),
    url('exec',views.exec,name="exec"),
    url('axect',views.axect,name="axect"),
    url('wed',views.wed,name="wed"),
    url('thus',views.thus,name="thus"),
    url('fri',views.fri,name="fri"),
    url('sat',views.sat,name="sat"),
    url('sun',views.sun,name="sun"),
    
]
 