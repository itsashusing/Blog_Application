
from django.contrib import admin
from django.urls import path, include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('post/<int:id>', views.detail, name='detail'),
    path('like/<int:id>', views.LikeView, name='like'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpUser),
    path('userprofile/', views.ProfileView),
    path('editpost/<int:id>', views.EditPostView),
    path('addpost/', views.AddPostView),
    path('delete/<int:id>/', views.DeletePost, name='delete_post'),
    path('updateuser/<int:id>', views.UpdateProfile),
    path('updateuserprofile/<int:id>', views.UpdateProfile1),
    path('mypost/',views.MyPostView)
]
