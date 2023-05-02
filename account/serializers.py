from rest_framework import serializers  

from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4, required=True)

    class Meta:
        model = User
        fields = ('email', 'phone', 'password', 'password_confirm')

    def validate(self, attrs):
        print('attrs before', attrs)
        pass1 = attrs.get("password")
        pass2 = attrs.pop("password_confirm")
        print('attrs after', attrs)
        if pass1 != pass2:
            raise serializers.ValidationError("passwords do not match")
        return attrs
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('user with this email already exists')
        return email
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)