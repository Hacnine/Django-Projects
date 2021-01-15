from django.contrib import admin
from django.urls import path
# from course import views as cv
# from fees import views as fv

from . import views


urlpatterns = [
    # path('course/', cv.course_description),
    # path('fees/', fv.fees_description)
    path('', views.course_description),

]