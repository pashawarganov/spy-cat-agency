from rest_framework import serializers

from agency.models import Cat, Target, Mission


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ("id", "name", "experience", "breed", "salary")


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ("id", "name", "country", "notes", "complete")


class MissionSerializer(serializers.ModelSerializer):
    cat = CatSerializer()
    target = TargetSerializer(many=True, read_only=False, allow_null=False)

    class Meta:
        model = Mission
        fields = ("id", "cat", "target", "complete")
