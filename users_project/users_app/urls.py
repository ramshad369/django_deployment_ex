from django.conf.urls import url
from users_app import views

app_name='users_app'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),

]
