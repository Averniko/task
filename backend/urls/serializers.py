import random
import string

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from urls.models import Url


def generate_unique_subpart():
    while True:
        subpart = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(6)
        )
        try:
            Url.objects.get(subpart=subpart)
        except Url.DoesNotExist:
            return subpart


class UrlSerializer(serializers.ModelSerializer):
    session_key = serializers.CharField(write_only=True)
    subpart = serializers.CharField(allow_blank=True, validators=[UniqueValidator(queryset=Url.objects.all())])

    class Meta:
        model = Url
        fields = ["subpart", "redirect", "session_key"]

    def create(self, validated_data):
        if "subpart" not in validated_data or not validated_data["subpart"]:
            validated_data["subpart"] = generate_unique_subpart()

        return super().create(validated_data)
