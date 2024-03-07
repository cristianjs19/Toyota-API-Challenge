from rest_framework import serializers

from .models import Characteristic, Vehicle

class VehicleListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    type = serializers.CharField(source='get_type_display')

    def get_image(self, obj):
        result = ""
        if obj.image:
            result = obj.image.url
        return result

    class Meta:
        model = Vehicle
        fields = ['id', 'model_name', 'year', 'type', 'price', 'image']


class CharacteristicSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        result = ""
        print(obj)
        if obj.image:
            result = obj.image.url
        return result

    class Meta:
        model = Characteristic
        fields = ['title', 'image', 'description']        


class VehicleDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    type = serializers.CharField(source='get_type_display')
    characteristics = CharacteristicSerializer(many=True)

    def get_image(self, obj):
        result = ""
        if obj.image:
            result = obj.image.url
        return result

    class Meta:
        model = Vehicle
        fields = ['id', 'model_name', 'year', 'type', 'price', 'image', 'subtitle', 'description', 'characteristics']
