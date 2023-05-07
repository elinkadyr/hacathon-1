from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Plan, Subscription
from .serializers import PlanSerializer, SubscriptionSerializer

class PlanListAPIView(APIView):
    def get(self, request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)

class SubscriptionListCreateAPIView(APIView):
    def get(self, request):
        subscriptions = Subscription.objects.filter(user=request.user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionRetrieveDestroyAPIView(APIView):
    def get(self, request, subscription_id):
        subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def delete(self, request, subscription_id):
        subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)