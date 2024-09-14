from django.urls import path
from .views import fetch_form_data

urlpatterns = [
    # URL pattern for fetching form data by form_id
    path('form/<int:form_id>/', fetch_form_data, name='fetch_form_data'),
]
