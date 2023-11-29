from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path(r'^admin/', include(admin.site.urls)),
    path(r'', include('blog.urls')),
]
