from django.conf.urls import url, patterns
from users import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='user'),
                       url(r'^reg/$', views.reg, name='reg'),
                       url(r'^login/$', views.login_user, name='login'),
                       url(r'^logout/$', views.logout_user, name='logout')
                       )
