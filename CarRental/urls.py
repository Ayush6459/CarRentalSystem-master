
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('login/', include("login.urls")),
    url('booking/', include("booking.urls")),
    url('home/', include("home.urls")),
    url('about/', include("about.urls")),
    url('contactUs/', include("contactUs.urls")),
]
