"""
GAVIP Example AVIS: Alerts AVI
"""
from avi import views, views_api
from plugins.urls import job_list_urls
from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns(
    '',
    url(r'^$',
        views_api.AlertsJobList.as_view(),
        name='index'),

    url(r'^(?P<pk>[0-9]+)/$',
        views_api.AlertsJobDetail.as_view(),
        name='alertsjob-detail'),

    url(r'^job_data/(?P<job_id>[0-9]+)/$',
        views_api.JobData.as_view(),
        name='api-job-data'),

    url(r'^view_jobs/$',
        views_api.ViewJobsList.as_view(),
        name='api-view-jobs'),

    url(r'^view_jobs/(?P<pk>[0-9]+)/$',
        views_api.ViewJobsListDetail.as_view(),
        name='api-view-jobs-detail'),

    url(r'^result/(?P<job_id>[0-9]+)/$',
        views.job_result,
        name='job_result'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

# plugin urls have already run 'format_suffix_patterns'
# So add them after
urlpatterns += patterns(
    url(r'^job_list/', include(job_list_urls, namespace='plugins')), 
)
