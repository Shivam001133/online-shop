from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    path('', views.ItemsViews.as_view(), name='items'),
    path('<int:pk>/', views.ItemsDetailsViews.as_view(), name='details'),
    path('add/', views.CreateItems.as_view(), name='create_items'),
    path('update/<int:item_id>/', views.update_items, name='update_items'),
    path('delete/<int:pk>/',
         views.DeleteItems.as_view(), name='delete_items'),
]
