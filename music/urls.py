from django.conf.urls import urls
from music import views
utlpatters=[
url(r'^$',views.index,name='index')
]
