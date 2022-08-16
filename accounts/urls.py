from django.urls import path
from accounts.views import SignUpFormView


app_name = 'accounts'

urlpatterns = [
    path('sign-up/', SignUpFormView.as_view(), name='sign-up')
]
