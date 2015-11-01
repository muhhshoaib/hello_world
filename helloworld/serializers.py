from rest_framework import serializers
from helloworld.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserInfo Model.
    """
    class Meta:
        """
        Meta Class
        """
        model = UserInfo