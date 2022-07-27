from django.urls import path
from .views import *
from . import views
app_name = "shop"
urlpatterns = [
    path("", BaseView.as_view(), name="base"),
    path("index/", HomeView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),

    path('proddetail/<slug:slug>/',
         ProductDetailView.as_view(), name="productdetail"),
    path('add-to-cart-<int:prod_id>/',
         AddToCartView.as_view(), name="addtocartview"),
    path('my-cart/', MyCartView.as_view(), name="mycart"),
    path('manage-cart/<int:cp_id>/', ManageCartView.as_view(), name="managecart"),
    path('empty-cart/', EmptyCartView.as_view(), name="emptycart"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    #     path("register/", views.CustomerRegistrationView, name="register"),
    path("register/", CustomerRegistrationView.as_view(), name="register"),
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order-<int:pk>/", CustomerOrderDetail.as_view(),
         name="customerorderdetail"),
    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/",
         AdminOrderDetailView.as_view(), name="adminorderdetail"),
    path("admin-all-orders/",
         AdminOrderListView.as_view(), name="adminorderlist"),
    path("admin-order-<int:pk>-change/",
         AdminOrderStatusChangeView.as_view(), name="adminorderstatuschange"),

    #  path('proddetail/<slug:pk>/',
    #  ProductDetailView.as_view(), name="productdetail") to send value as pk and above is slug strng value

]
