from rest_framework import serializers
from .models import tasks

# class LoginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         style={"input_type": "password"}, write_only=True)
#     class Meta:
#         model = User
#         fields = ("username", "password",)
        

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         style={"input_type": "password"}, write_only=True)
    
#     confirm_password = serializers.CharField(
#         style={"input_type": "password"}, write_only=True)
#     class Meta:
#         model = User
#         fields =  ('id', 'username', 'email', 'password','confirm_password')

#     def create(self, validated_data):
#         if validated_data["password"] != validated_data["confirm_password"]:
#             raise serializers.ValidationError(
#                 {"password": "passwords don't match!"})

#         user = User.objects.create_user(
#             validated_data["username"], validated_data["email"], validated_data["password"])
        
#         return user
        

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = ['id','task']

    