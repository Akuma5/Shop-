from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from magazine.views import MagazineLikeView, CommentView
from magazine.views import MagazineAPIList, MagazineAPIUpdate, MagazineAPIDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:product_pk>/comment/create/', CommentView.as_view({'post': 'create'})), # url comment
    path('<int:product_pk>/like/', MagazineLikeView.as_view()), # url like
    path('magazine/', MagazineAPIList.as_view()),
    path('magazine/<int:pk>/', MagazineAPIUpdate.as_view()),
    path('magazinedelete/<int:pk>/', MagazineAPIDetailView.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
