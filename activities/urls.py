from django.conf.urls import url
from . import views
app_name = 'activities'
urlpatterns = [
    url(r'^$', views.activity_list, name='activity_list'),
    url(r'^get_drinki/json$', views.get_drinki, name='get_drinki'),
    url(r'^create_drink$', views.create_drink, name='create_drink'),
    url(r'^goals$', views.goals, name='goals')
]
