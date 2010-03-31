import os
from django.conf.urls.defaults import *
from bookmarks.views import *
from django.views.generic.simple import direct_to_template

site_media = os.path.join(
  os.path.dirname(__file__), 'site_media'
)


urlpatterns = patterns('',
    # Browsing
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^tag/([^\s]+)/$', tag_page),
    (r'^tag/$', tag_cloud_page),
    (r'^search/$', search_page),
    (r'^popular/$', popular_page),
    (r'^bookmark/(\d+)/$', bookmark_page),

    # Ajax
    (r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),

    # Comments
    (r'^comments/',
        include('django.contrib.comments.urls')),

    # Session management
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', direct_to_template,
        {'template': 'registration/register_success.html'}),

    # Account management
    (r'^save/$', bookmark_save_page),
    (r'^vote/$', bookmark_vote_page),

    # Site media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': site_media}),
)
