from rest_framework import serializers
import datetime
import short_url
from django.contrib.auth import get_user_model


from .models import URL
from .fields import ObjectIDField
from .value_error import FullURLDuble

def test_short_url(self):
    url_short = URL.objects.all().filter(full_url=self)
    for i in url_short:
        n = i.id
    return n


class URLSerializer(serializers.Serializer):

    url_duble = False
  

    id = serializers.IntegerField(read_only=True)
    full_url = serializers.URLField()
    short_url = serializers.SerializerMethodField('short_url_vievs')    
    created = serializers.DateTimeField(default=datetime.datetime.now(), read_only=True)    

    class Meta:
        model = URL
        fields = '__all__'

    
    def validate_full_url(self, value):
        if FullURLDuble(value) != 0:
            full_url = serializers.URLField()
            raise serializers.ValidationError('URL exists: {} {}'.format(value, full_url))
        return value

    def create(self, validated_data):       
        return URL.objects.create(**validated_data)    
    
    
    def short_url_vievs(self, obj):
        return 'http://example.com/{}'.format(short_url.encode_url(obj.id))