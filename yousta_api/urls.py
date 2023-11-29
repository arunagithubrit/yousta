from django.urls import path
from yousta_api import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("cloths",views.ClothsView,basename='cloths')
router.register("carts",views.CartsView,basename="carts")
router.register("orders",views.OrderView,basename="orders")
router.register("reviews",views.ReviewView,basename="reviews")

urlpatterns=[
    path('register/',views.UserCreationView.as_view()),
    path('token/',ObtainAuthToken.as_view()),
]+router.urls