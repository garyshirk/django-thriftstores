from rest_framework import serializers
from thriftstores.models import ThriftStore

class ThriftStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThriftStore
        fields = ('bizID', 'bizName', 'bizCat', 'bizCatSub', 'bizAddr', 'bizCity', 'bizState', 
            'bizZip', 'bizPhone', 'bizEmail', 'bizURL', 'locLat', 'locLong')


# class ThriftStoreSerializer(serializers.Serializer):
#     bizID = serializers.IntegerField()
#     bizName = serializers.CharField(max_length=50)
#     bizCat = serializers.CharField(required=False, allow_blank=True, max_length=50)
#     bizCatSub = serializers.CharField(required=False, allow_blank=True, max_length=50)
#     bizAddr = serializers.CharField(max_length=100)
#     bizCity = serializers.CharField(max_length=50)
#     bizState = serializers.CharField(max_length=50)
#     bizZip = serializers.CharField(max_length=20)
#     bizPhone = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     bizEmail = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     bizURL = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     locLat = serializers.FloatField()
#     locLong = serializers.FloatField()

#     def create(self, validated_data):
#         """
#         Create and return a new `ThriftStore` instance, given the validated data.
#         """
#         return ThriftStore.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `ThriftStore` instance, given the validated data.
#         """
#         instance.bizID = validated_data.get('bizID', instance.bizID)
#         instance.bizName = validated_data.get('bizName', instance.bizName)
#         instance.bizCat = validated_data.get('bizCat', instance.bizCat)
#         instance.bizCatSub = validated_data.get('bizCatSub', instance.bizCatSub)
#         instance.bizAddr = validated_data.get('bizAddr', instance.bizAddr)
#         instance.bizCity = validated_data.get('bizCity', instance.bizCity)
#         instance.bizState = validated_data.get('bizState', instance.bizState)
#         instance.bizZip = validated_data.get('bizZip', instance.bizZip)
#         instance.bizPhone = validated_data.get('bizPhone', instance.bizPhone)
#         instance.bizEmail = validated_data.get('bizEmail', instance.bizEmail)
#         instance.bizURL = validated_data.get('bizURL', instance.bizURL)
#         instance.locLat = validated_data.get('locLat', instance.locLat)
#         instance.locLong = validated_data.get('locLong', instance.locLong)
#         instance.save()
#         return instance