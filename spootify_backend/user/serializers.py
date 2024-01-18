from rest_framework import serializers
from django.contrib.auth.models import User
from .models import GENDER_CHOICE,Customer
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password',write_only=True )
    birth_date = serializers.DateField(input_formats=['%Y.%m.%d'])
    gender = serializers.ChoiceField(choices=GENDER_CHOICE)
    token = serializers.SerializerMethodField(read_only=True)

    def create(self,validated_data):
        user_info = validated_data.pop('user')
        user = User.objects.create_user(**user_info)

        customer = Customer.objects.create(user = user, **validated_data)

        return customer
    
    def get_token(self,customer):
        token,created = Token.objects.get_or_create(user=customer.user)
        return token.key
    

class CustomerInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    birth_date = serializers.DateField(input_formats=['%Y.%m.%d'])
    gender = serializers.ChoiceField(choices=GENDER_CHOICE)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id','first_name','last_name','username','email','birth_date','gender','token']

    def get_token(self,customer):
        token,created = Token.objects.get_or_create(user=customer.user)
        return token.key   

  

    
