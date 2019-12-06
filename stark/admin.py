from django.contrib import admin

# Register your models here.
from app01.models import *
admin.site.register(Book)
admin.site.register(AuthorDetail)
admin.site.register(Author)
admin.site.register(Publish)
