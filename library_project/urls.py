
from django.contrib import admin
from django.urls import path,include
from dj_rest_auth import urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1',include('books.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/',include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',include('dj_rest_auth.registration.urls')),
    

]
