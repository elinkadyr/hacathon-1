from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Plan, Subscription
from .serializers import PlanSerializer, SubscriptionSerializer
from .utils import validate_card, generate_transaction_id


class PlanListAPIView(APIView):
    def get(self, request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            plan = Plan.objects.get(pk=pk)
        except Plan.DoesNotExist:
            return Response(status=404)

        plan.delete()
        return Response(status=204)



@csrf_exempt
class SubscriptionView(APIView):
    def post(self, request, format=None):
        card_number = request.data.get('card_number')
        cardholder_name = request.data.get('cardholder_name')
        card_exp_month = request.data.get('card_exp_month')
        card_exp_year = request.data.get('card_exp_year')
        card_cvv = request.data.get('card_cvv')
        price = request.data.get('amount')
        plan = request.data.get('plan')

        # Проверяем данные карты
        if not validate_card(card_number, card_exp_month, card_exp_year, card_cvv):
            return Response({'success': False, 'message': 'Invalid card data.'}, status=400)

        # Проводим оплату и получаем ответ
        response = {
            'success': True,
            'message': 'Payment successful!',
            'transaction_id': generate_transaction_id(),
            'plan': plan
        }

        # Возвращаем ответ
        return Response(response, status=200)
