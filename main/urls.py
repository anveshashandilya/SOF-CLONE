from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout_view,name="logout"),
    path('profile/', views.profile, name="profile"),
    path('count/like/<int:id>', views.upvote, name='like'),
    path('count/dislike/<int:id>', views.downvote, name='dislike'),
        # path('add-question/', views.add_question, name='add_question'),
    
]