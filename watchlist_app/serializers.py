from rest_framework import serializers
from .models import WatchList, StreamPlatform



class WatchListSerializer(serializers.ModelSerializer):
    #len_name=serializers.SerializerMethodField()
    
    class Meta:
        model=WatchList
        #fields=['id','name','description','active']
        fields='__all__'
        #exclude=['active']  
    # def get_len_name(self,obj):
    #     return len(obj.title) 
        #return obj.description



class StreamPlatformSerializer(serializers.ModelSerializer):
    #watchlist=WatchListSerializer(many=True, read_only=True)
    #watchlist=serializers.StringRelatedField(many=True, read_only=True)
    #watchlist=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #watchlist=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watch-details')
    #link=serializers.HyperlinkedIdentityField(view_name='StreamPlatform-Details')
    
    
    price=serializers.SerializerMethodField()
    class Meta:
        model=StreamPlatform
        fields='__all__'
        
    def get_price(self,obj):
        return 1





# def name_len(value):
#     if len(value) <2:
#         raise serializers.ValidationError('Name should be of two character')
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_len])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         print('validated_data :',validated_data)
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    # def validate_name(self,value):
    #     if len(value) <2:
    #         raise serializers.ValidationError('Name is too short!')
    #     else:
    #         return value
        
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name and Description should not be same')
    #     return data
        
    
