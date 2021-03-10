from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from main.views import FeedbackView


router = DefaultRouter()
router.register('main/feedback', FeedbackView, basename="feed-view")


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("api/blog/", include("blog.urls")),
    # path("api/feedback/", include("main.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name="index.html"))]

