from django.contrib import admin
from django.urls import path, include
from lesson_1.views import first_views, second_views, num, sum, db, add_product, selectFromAcademy

urlpatterns = [
   path('first/', first_views),
   path('second/<str:name>/', second_views),
   path('second/<int:num_>', num),
   path('summa/<int:a> <int:b>', sum),
   path('base/<str:name>', db),
   path('iserttobase/<str:name> <str:dean>', add_product),
   path('select/<str:name>', selectFromAcademy)
]
