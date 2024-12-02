from django.urls import path
from.views import *
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define the schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Description of your API",
        # terms_of_service="https://www.example.com/terms/",
        # contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,  # Change to False to restrict access
    permission_classes=(permissions.AllowAny,),  # Control who can access the documentation
)



urlpatterns = [
    path('question',QuestionView.as_view()),
    path('signup',SignupView.as_view()),
    path('login',LoginView.as_view()),
    path('answer<int:id>',AnswerView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
