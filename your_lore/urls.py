from django.urls import path, include

urlpatterns = [
    path('', include('lore.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]