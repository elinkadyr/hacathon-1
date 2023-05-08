from rest_framework import serializers
from .models import Plan, Subscription

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields =  '__all__'

    def to_representation(self, instance: Plan):
        rep = super().to_representation(instance)
        rep["plan"] = {"id": instance.plan.id, "name": instance.plan.name}
        return rep

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
