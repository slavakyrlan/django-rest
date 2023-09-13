import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Film


# class FilmModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content



class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"




    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # cat_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Film.objects.create(**validated_data)
    #     # В нашем случае – это объект модели класса film. Причем коллекция validated_data – это словарь с проверенными данными, полученными в результате POST-запроса после выполнения метода serializer.is_valid().
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.is_published = validated_data.get("is_published", instance.is_published)
    #     instance.cat_id = validated_data.get("cat_id", instance.cat_id)
    #     instance.save()
    #     return instance





# def encode():
#     model = FilmModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = FilmSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = FilmSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)