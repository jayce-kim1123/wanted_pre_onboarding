from django.urls import path, include

urlpatterns = [
    path('recruitment', include('products.urls')),
]
