from django.urls import path

from . import views




urlpatterns = [
    
    path("<int:pk>/", views.product_alt_view),
     path("", views.product_alt_view),
    #path("create/", views.ProductDetailCreateApiView.as_view()),
    #path("", views.ProductListApiView.as_view()),
]