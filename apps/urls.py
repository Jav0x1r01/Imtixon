from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import UserModelView,RegisterView,CustomLoginView,LogoutPageView,delete_product,ProductUpdateView
urlpatterns = [
    path('', UserModelView.as_view(), name='index'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutPageView.as_view(), name='logout_'),
    path('delete/<int:pk>',delete_product,name='delete_product'),
    path('update/<int:id>',ProductUpdateView.as_view(), name='update_product')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
