from django.contrib import admin
from django.conf.urls import url,include
from music import views
urlpatterns = [
        url(r'^admin/',admin.site.urls),
        url(r'^$,views.index,name='index'),
        url(r'music/',include('music.urls')),

]
