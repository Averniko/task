from rest_framework import serializers

from urls.models import Url


class UrlSerializer(serializers.ModelSerializer):
    session_key = serializers.CharField(write_only=True)

    class Meta:
        model = Url
        fields = ["subpart", "redirect", "session_key"]
