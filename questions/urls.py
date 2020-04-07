from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Questions_List.as_view(), name='questions_list_url'),
    url(r'^settings$', Profile_Settings.as_view(), name='profile_settings_url'),
    url(r'^ask$', Ask_Page.as_view(), name='ask_page_url'),
    url(r'^hot$', Questions_List_Hot.as_view(), name='questions_list_hot_url'),
    url(r'^newest$', Questions_List_Newest.as_view(), name='questions_list_newest_url'),
    url(r'^question/(?P<id>[0-9]+)$', Question_Details.as_view(), name='question_details_url'),
    url(r'^tags/$', Tags_List.as_view(), name='tags_list_url'),
    url(r'^tag/(?P<slug>[\w-]+)$', Tag_Details.as_view(), name='tag_details_url'),
    url(r'^register/$', Register.as_view(), name='register_url'),
    url(r'^signin/$', Sign_In.as_view(), name='sign_in_url'),
]

