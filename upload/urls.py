from django.conf.urls import url



from .import views 

app_name='upload'

urlpatterns = [

    url(r'^$', views.login,name='login'),
	url(r'^filled$', views.filled,name='filled'),
	
	# url(r'^uploaded$', views.uploaded,name='uploaded'),
	# url(r'^done$', views.done,name='done'),
    ]
