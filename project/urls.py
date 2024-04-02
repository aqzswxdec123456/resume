from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('resume/', include('resume.urls')),
    path('admin/', admin.site.urls),
]

