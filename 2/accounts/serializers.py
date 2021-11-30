from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'age', 'phone')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user_ser = UserSerializer(instance=instance.user, data=user_data)
        if user_ser.is_valid():
            user_ser.save()
        instance.bio = validated_data.get('bio', instance.bio)
        instance.age = validated_data.get('age', instance.age)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance

