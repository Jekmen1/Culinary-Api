from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include, re_path
from restapi_app import views

router = DefaultRouter()
router.register(r'dishes', views.DishesViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'chefs', views.ChefsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path('^auth/', include('djoser.urls')),
]
