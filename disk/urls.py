from django.conf.urls import include, url                                                                      
from disk.views import register

urlpatterns = [
# Examples:
# url(r'^$', 'mysite.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
   	url(r'^$',register),

