from django.urls import path
from .views import PlanListAPIView, SubscriptionView


urlpatterns = [
    path('plans/', PlanListAPIView.as_view(), name='plan-list'),
    path('subscriptions/', SubscriptionView, name='subscription-list-create'),
]
