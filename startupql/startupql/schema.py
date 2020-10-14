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

class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = [
              ‘employee_name’,
              ‘employee_city__city_name’,
              ‘employee_title__title_name’
               ]
        interfaces = (graphene.relay.Node,

