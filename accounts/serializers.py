from rest_framework import serializers
from .models import User

class UserSerializerAccount(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'full_name', 'email','phone_number', 'date_of_birth', 'CPF', 'wallet', 'password']

    # password = serialziers.Charfield(read_only=True)

        extra_kwargs = {'password':{'write_only':True}} 

        email = serializers.EmailField(required=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializerLogin(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()