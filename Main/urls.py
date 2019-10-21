from django.urls import path
from Main.views import block_register
urlpatterns = [
    path('/dbpost', block_register, name="dbpost"),

]