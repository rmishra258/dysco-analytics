from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views






admin.autodiscover()



import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url('^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/login'}, name='auth_logout'),
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', hello.views.test, name='test'),
    url(r'^base/$', hello.views.base, name='base'),
    url(r'blog/$', hello.views.blog, name='blog'),
    url(r'app/$', hello.views.app, name='app'),


    #BLOG DATA


    #Gender

    url(r'blog/gender/$', hello.views.bloggender, name='blog-gender'),


    #Age-Group

    url('blog/age-group/$', hello.views.blogagegroup, name='blog-age-group'),


    #Location

    url(r'blog/location/$', hello.views.bloglocation, name='blog-location'),


    #International

    url(r'blog/international/$', hello.views.international, name='blog-international'),


    #Operating Systems

    url(r'blog/os/$', hello.views.operatingsystem, name='blog-os'),

    #Interest groups

    url(r'blog/interest/$', hello.views.bloginterest , name='blog-interest'),

    #Article Based

    url(r'blog/articles/$', hello.views.articles, name='blog-articles'),


    #MOBILE APP DATA

    #Screens

    url(r'app/screens/$', hello.views.screens , name='app-screens'),

    # App users

    url(r'app/app-users/$', hello.views.appusers, name='app-users'),

    # App location

    url(r'app/location/$', hello.views.applocation, name='app-location'),

    #App interest groups

    url(r'app/interest/$', hello.views.appinterest, name='app-interest'),

    # App trending profiles

    url(r'app/trending/$', hello.views.trendingProfiles, name='app-trending'),

    # App top posts

    url(r'app/top-posts/$', hello.views.topPosts, name='app-topposts'),



]
