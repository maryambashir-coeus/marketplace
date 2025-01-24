from django.urls import path
from . import views

# URL configuration
urlpatterns = [
    # Authentication
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # home page
    path('', views.home, name='home'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('profile/', views.profile, name='profile'),
    path('add-item/', views.add_item, name='add_item'),
    path('order-history/', views.order_history, name='order_history'),
    path('purchase/<int:item_id>/', views.purchase_item, name='purchase_item'),
    path('purchase_success/<int:item_id>/', views.purchase_success, name='purchase_success'),

]