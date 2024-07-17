from django.urls import path
from ss import views


urlpatterns = [
    path("",views.home,name ="home"),
    path("register/",views.register,name ="register"),
    path("login/",views.login_view,name ="login_view"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("add_item/",views.add_item,name="add_item"),
    path("add_distributor/",views.add_distributor,name="add_distributor"),
    path("logout/",views.logout,name="logout"),
    path('add_orders/',views.add_orders,name="add_orders"),
    path('fetch_details/',views.fetch_details,name="fetch_details"),
    path('edit-item/<int:item_id>/', views.edit_item, name='edit_item'),

    

]
