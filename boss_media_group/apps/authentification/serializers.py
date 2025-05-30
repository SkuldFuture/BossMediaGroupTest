from django.contrib.auth import get_user_model, authenticate
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


User = get_user_model()


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get("request"), email=email, password=password)

        if not user:
            raise serializers.ValidationError("Неверный email или пароль")

        data = super().validate(attrs)
        data['user_id'] = user.id
        data['email'] = user.email
        return data

    def get_fields(self):
        fields = super().get_fields()
        fields['email'] = serializers.EmailField()
        if 'username' in fields:
            del fields['username']
        return fields

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
