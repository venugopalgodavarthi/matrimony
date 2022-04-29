from django.urls import path
from prodetail import views
app_name="prodetail"
urlpatterns=[
    path('profile/',views.profilehomeview.as_view(),name='profile'),
    path('detail/',views.detailview.as_view(),name='detail'),
    path('education/',views.educationview.as_view(),name='education'),
    path('occupation/',views.occupationview.as_view(),name='occupation'),
    path('family/',views.familyview.as_view(),name='family'),
    path('siblings/',views.siblingsview.as_view(),name='siblings'),
    path('address/',views.addressview.as_view(),name='address'),
    path('profilelink/',views.profilelinkview.as_view(),name='profilelink'),

    path('udetail/<pk>/',views.udetailview.as_view(),name='udetail'),
    path('ueducation/<pk>',views.ueducationview.as_view(),name='ueducation'),
    path('uoccupation/<pk>',views.uoccupationview.as_view(),name='uoccupation'),
    path('ufamily/<pk>',views.ufamilyview.as_view(),name='ufamily'),
    path('usiblings/<pk>',views.usiblingsview.as_view(),name='usiblings'),
    path('uaddress/<pk>',views.uaddressview.as_view(),name='uaddress'),
    path('uprofilelink/<pk>',views.uprofilelinkview.as_view(),name='uprofilelink'),
   
    ]