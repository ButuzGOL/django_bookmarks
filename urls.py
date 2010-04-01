import os
from django.conf.urls.defaults import *

from bookmarks.views import *
from bookmarks.feeds import *

from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)

# Make sure you add the feeds dict before
# the urlpatterns object.
feeds = {
    'recent': RecentBookmarks,
    'user': UserBookmarks
}

urlpatterns = patterns('',
    # Browsing
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^tag/([^\s]+)/$', tag_page),
    (r'^tag/$', tag_cloud_page),
    (r'^search/$', search_page),
    (r'^popular/$', popular_page),
    (r'^bookmark/(\d+)/$', bookmark_page),

    # Friends
    (r'^friends/(\w+)/$', friends_page),
    (r'^friend/add/$', friend_add),
    (r'^friend/invite/$', friend_invite),
    (r'^friend/accept/(\w+)/$', friend_accept),
    
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

    # Admin interface
    (r'^admin/(.*)', admin.site.root),

    # Feeds
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),

    # Site media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': site_media}),
)
