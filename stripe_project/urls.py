from django.contrib import admin
from django.urls import path, include

import items_app, checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("items_app.urls")),
    path('buy/', include("checkout.urls"))
]
