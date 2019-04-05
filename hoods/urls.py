from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.neighbor,name = 'neighbor'),
    url('^today/$',views.hoods_of_day,name='hoodsToday'),
]