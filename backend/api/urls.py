from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api import views as api_views
# from .views import test_cloudinary, direct_upload_test, simple_upload_test    

urlpatterns = [

    # path('test-cloudinary/', test_cloudinary, name='test-cloudinary'),
    # path('upload-test/', direct_upload_test, name='upload-test'),
    # path('simple-upload-test/', simple_upload_test, name='simple-upload-test'),


    path("user/token/", api_views.MyTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/register/', api_views.RegisterView.as_view()),
    path('user/profile/<user_id>/', api_views.ProfileView.as_view()),

    # Posts
    path('post/category/list/', api_views.CategoryListAPIView.as_view()),
    path('post/category/posts/<category_slug>/', api_views.PostCategoryListAPIView.as_view()),
    path('post/lists/', api_views.PostListAPIView.as_view()),
    path('post/detail/<slug>/', api_views.PostDetailAPIView.as_view()),
    path('post/like-post/', api_views.LikePostAPIView.as_view()),
    path('post/comment-post/', api_views.PostCommentAPIView.as_view()),
    path('post/bookmark-post/', api_views.BookmarkPostAPIView.as_view()),

    # Author
    path('author/dashboard/stats/<user_id>/', api_views.DashboardStats.as_view()),
    path('author/dashboard/post-list/<user_id>/', api_views.DashboardPostLists.as_view()),
    path('author/dashboard/comment-list/<user_id>/', api_views.DashboardCommentLists.as_view()),
    path('author/dashboard/noti-list/<user_id>/', api_views.DashboardNotificationLists.as_view()),
    path('author/dashboard/noti-mark-seen/', api_views.DashboardMarkNotiSeenAPIView.as_view()),
    path('author/dashboard/reply-comment/', api_views.DashboardPostCommentAPIView.as_view()),
    path('author/dashboard/post-create/', api_views.DashboardPostCreateAPIView.as_view()),
    path('author/dashboard/post-detail/<user_id>/<post_id>/', api_views.DashboardPostEditAPIView.as_view()),


    


]
