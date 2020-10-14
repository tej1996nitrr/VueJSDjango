import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import  DjangoFilterConnectionField

class CityNode(DjangoObjectType):
    class Meta:
        model = City 
        filter_fields = [‘city_name’]
        interfaces = (graphene.relay.Node,)


class TitleNode(DjangoObjectType):
    class Meta:
        model = Title
        filter_fields = ['title_name']
        interfaces = (graphene.relay.Node,)

