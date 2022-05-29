from django.urls import path, include
from . import views

urlpatterns = [
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session')
   ]