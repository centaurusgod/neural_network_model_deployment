from rest_framework import serializers
from .models import *

class BirdsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Birds
        fields = ['common_name', 'scientific_name', 'probable_age']
        extra_kwargs = {
            
            'common_name': {'required': False},
            'scientific_name': {'required': False},
            'probable_age': {'required': False},
            
        }
        
    def validate(self, data):
        if data['common_name']:
            for character in data['common_name']:
                if character.isdigit():
                    raise serializers.ValidationError({'status':201, 'error':'Numeric Value Provided In CommonName String Field'})
        return data
    

class BirdsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdsStatus
        fields = '__all__'
        
    def validate(self, data):
     #write validation logic here, like checking integers in status_code and name fields etc.
      return data
            
            
class BirdsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdsDetail
        fields = '__all__'
        
    def validate(self, data):
        #Write validation logic here
        return data
            
class NodeDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeDevice
        fields = '__all__'
    def validate(self, data):
        return data