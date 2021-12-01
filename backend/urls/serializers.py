from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from urls.models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["subpart", "redirect", "session_key"]

        validators = [UniqueTogetherValidator(
            queryset=Url.objects.all(),
            fields=['session_key', 'subpart']
        )]
