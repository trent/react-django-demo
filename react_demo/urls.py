from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework import routers
from books.viewsets import AuthorViewSet, BookViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'react_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^demo_1/', TemplateView.as_view(template_name='demo_1.html'), name='demo_1'),
    url(r'^demo_2/', TemplateView.as_view(template_name='demo_2.html'), name='demo_2'),
    url(r'^demo_3/', TemplateView.as_view(template_name='demo_3.html'), name='demo_3'),
    url(r'^demo_4/', TemplateView.as_view(template_name='demo_4.html'), name='demo_4'),
)
