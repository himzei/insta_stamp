from rest_framework.serializers import ModelSerializer 
from .models import User 


class TinyUserSerializer(ModelSerializer): 
    class Meta: 
        model = User 
        fields = (
            "name", 
            "email"
        )

class PrivateUserSerializer(ModelSerializer): 
    class Meta: 
        model = User 
        fields = (
           "email", 
           "name",
           "is_admin", 
           "is_staff", 
        )