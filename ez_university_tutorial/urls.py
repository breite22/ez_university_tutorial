from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth import views as auth_views

from courseinfo import urls as courseinfo_urls

urlpatterns = [

    url(r'^$',
        RedirectView.as_view(
            pattern_name='about_urlpattern',
            permanent=False
        )
    ),

    url(r'^about/$',
        TemplateView.as_view(
            template_name='courseinfo/about.html'),
            name='about_urlpattern'
        ),

    url(r'^login/$',
        auth_views.login,
        {'template_name': 'courseinfo/login.html'},
        name='login_urlpattern'
        ),

    url(r'^logout/$',
        auth_views.logout,
        {'next_page': '/login/'},
        name='logout_urlpattern'
        ),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(courseinfo_urls)),

]
