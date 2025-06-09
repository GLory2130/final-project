
from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('myapp.urls')),
    # path('chatbot/', include('chatbot.urls')),
    path('admin/', admin.site.urls),
    path('myproject/ml/', include('machine_learning.urls')),
    path('myproject/rag/', include('generate_rag.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

