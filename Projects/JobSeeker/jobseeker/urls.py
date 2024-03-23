"""jobseeker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from job import views as job_views
from jobseeker.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^index/$', job_views.index, name='index'),
    url(r'^findjob/$', job_views.findjob, name='findjob'),
    url(r'^about/$', job_views.about, name='about'),
    url(r'^hrlogin/$', job_views.hrlogin, name='hrlogin'),
    url(r'^jslogin/$', job_views.jslogin, name='jslogin'),
    url(r'^ttlogin/$', job_views.ttlogin, name='ttlogin'),
    url(r'^contact/$', job_views.contact, name='contact'),
    url(r'^techregister',job_views.techregister,name='techregister'),
    url(r'^jsregister',job_views.jsregister,name='jsregister'),
    url(r'^TechHome',job_views.TechHome,name='TechHome'),
    url(r'^JobHome',job_views.JobHome,name='JobHome'),
    url(r'^HrHome',job_views.HrHome,name='HrHome'),
    url(r'^DisplayProfile',job_views.DisplayProfile,name='DisplayProfile'),
    url(r'^Profil',job_views.Profil,name='Profil'),
    url(r'^UserRegister1/$', job_views.UserRegister1, name='UserRegister1'),
    url(r'^PostJob',job_views.PostJob,name='PostJob'),
    url(r'^ViewPostJob',job_views.ViewPostJob,name='ViewPostJob'),
    url(r'^ViewJobs',job_views.ViewJobs,name='ViewJobs'),
    url(r'^ViewHrJobs',job_views.ViewHrJobs,name='ViewHrJobs'),
    url(r'^UpdateJob/(?P<r_id>\w+)',job_views.UpdateJob),
    url(r'^ApplyJob/(?P<r_id>\w+)',job_views.ApplyJob),
    url(r'^JobApplicants/(?P<r_id>\w+)',job_views.JobApplicants),
    url(r'^UserDetailsHr/(?P<u_na>\w+)',job_views.UserDetailsHr),
    url(r'^DeleteJob/(?P<d_id>\w+)',job_views.DeleteJob),

]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)