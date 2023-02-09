from django.db.models import fields
from rest_framework import serializers
from .models import ApiUser

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model=ApiUser
        fields=('apiname','apiemail')