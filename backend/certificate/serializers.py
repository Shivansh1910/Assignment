from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Manager
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Candidate
        fields = '__all__'


class ConcernSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Concern
        fields = '__all__'


class UserCertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserCertificate
        fields = '__all__'


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sample
        fields = '__all__'

# class RegistrationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.Candidate
#         fields = ('name', 'email')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)

#         instance.save()
#         return instance
