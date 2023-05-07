from django.urls import path
from .views import PlanListAPIView, SubscriptionListCreateAPIView, SubscriptionRetrieveDestroyAPIView

urlpatterns = [
    path('plans/', PlanListAPIView.as_view(), name='plan-list'),
    path('subscriptions/', SubscriptionListCreateAPIView.as_view(), name='subscription-list-create'),
    path('subscriptions/<int:subscription_id>/', SubscriptionRetrieveDestroyAPIView.as_view(), name='subscription-retrieve-destroy'),
]
