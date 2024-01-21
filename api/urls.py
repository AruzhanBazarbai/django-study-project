from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

# routing
api=Api(api_name="v1")
api.register(CourseResource())
api.register(CategoryResource())

# api/v1/courses/        GET POST
# api/v1/courses/1/      GET DELETE
# api/v1/categories/     GET
# api/v1/categories/1/   GET

# for POST, DELETE add Header
# Key: Authorization
# value: ApiKey aruzhan:qwerty123456789

urlpatterns = [
    path('', include(api.urls), name="index")
]