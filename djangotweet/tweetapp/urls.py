from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('',views.listtweet,name='listtweet'), #alarech.com/tweetapp/
    path('addtweet/',views.addtweet,name='addtweet'), #alarech.com/tweetapp/addtweet
    path('addtweetbyform',views.addtweetbyform,name='addtweetbyform'),#alarech.com/tweetapp/addtweetbyform
    path('addtweetbymodelform',views.addtweetbymodelform,name='addtweetbymodelform'),
    path('signup/',views.SignUp.as_view(),name="signup"),
    path("deletetweet/<int:id>",views.deletetweet, name="deletetweet")
]

