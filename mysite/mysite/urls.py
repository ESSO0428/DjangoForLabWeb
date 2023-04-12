"""mysite URL Configuration

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
from django.urls    import path
# from app1.views     import homepage
# from app2.views     import pageApp2, ntab1, about, listing, bootstrap

import app1.views as views1
import app2.views as views2
"""
from django.contrib import admin
from django.urls    import path
from app1.views     import homepage
"""

# admin (帳/密) : root/KIKI12345
urlpatterns = [
    path('admin/'                                   , admin.site.urls)       ,

    # 各種測試頁
    path('test/', views2.App2TestPage)              ,
    # path('post/<slug:slug>/'                      , views2.showpost)       ,
    path('test/post/'                               , views2.showpost)       ,
    path('test/about/'                              , views2.about)          ,
    path('test/age/'                                , views2.age)            ,
    path('test/age_form/'                           , views2.age_form)       ,
    path('test/mail/'                               , views2.your_mail)      ,
    path('test/mail_form/'                          , views2.your_mail_form) ,
    path('test/list/'                               , views2.listing)        ,
    path('test/list/<int:yr>/<int:mon>/<int:day>/'  , views2.LISTING)        ,

    # 主要開發中的網頁
    path('DjangoForm/'                              , views2.djangoform)     ,
    path('OrchidLogin/'                             , views2.aiweblog)       ,
    path('OrchidMain/'                              , views2.orchidwebpage)  ,
    path('V3deg/'                                   , views2.degradome)      ,
    path('V3deg/detail/'                            , views2.degradome)      ,
    path('V3deg/detail/deg_miRNA_seq/'              , views2.degradome)      ,
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

