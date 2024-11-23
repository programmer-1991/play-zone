from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('add/product', views.add_product, name="add_product"),
    path('add/game', views.add_game, name="add_game"),
    path('add/console', views.add_console, name="add_console"),
    path('edit/product/<int:product_id>/', views.edit_product, name="edit_product"),
    path('edit/game/<int:game_id>/', views.edit_game, name="edit_game"),
    path('edit/console/<int:console_id>/', views.edit_console, name="edit_console"),
    path('delete/product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete/game/<int:game_id>/', views.delete_game, name='delete_game'),
    path('delete/console/<int:console_id>/', views.delete_console, name='delete_console'),
]
