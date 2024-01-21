from django.db import models
from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentification import CustomAuthentication

class CategoryResource(ModelResource):
    class Meta:
        queryset=Category.objects.all()
        resource_name="categories"
        allowed_methods=['get']

class CourseResource(ModelResource):
    class Meta:
        queryset=Course.objects.all()
        resource_name="courses"
        allowed_methods=['get', 'post', 'delete']
        authentication=CustomAuthentication() # custom auth system
        authorization=Authorization() #authorization system from tastypie
        excludes=['reviews_qty', 'created_at'] 

    def hydrate(self, bundle): #serialization
        bundle.obj.category_id=bundle.data["category_id"]
        return bundle
    
    def dehydrate(self, bundle): #deserialization
        bundle.data['category_id']=bundle.obj.category_id
        return bundle
    
    def dehydrate_title(self, bundle): #deserialization title
        return bundle.data['title'].upper()
