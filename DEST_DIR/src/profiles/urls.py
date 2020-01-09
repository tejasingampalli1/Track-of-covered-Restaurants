
from django.conf.urls import url

from .views import ProfileDetailView

# the below is not needed as everything is done in class based views and for that there is a separate url file.
#from restaurants.views import restaurant_listview ,RestaurantListView, RestaurantDetailView,RestaurantCreateView,restaurant_createview

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
  
]