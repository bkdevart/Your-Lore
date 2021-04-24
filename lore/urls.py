from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from lore import views

urlpatterns = [
    path('lore/', views.LoreList.as_view()),
    path('lore/<int:pk>/', views.LoreDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)