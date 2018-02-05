from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from forumapp import views

router = DefaultRouter()
router.register('forums', views.ForumViewSet)
router.register('threads', views.ThreadViewSet)
router.register('sections', views.ForumSectionViewSet)
router.register('users', views.ForumUserViewSet)
router.register('threadresponses', views.ThreadResponseViewSet)
# router.register('likesdislikes', views.LikeDislikeViewSet)

urlpatterns = [
    # Router path
    path('rest/', include(router.urls)),

    # Class based paths
    path(
        'rest/rest_ban_user/<int:pk>/',
        views.BanUser.as_view(),
        name='rest-ban-user'
    ),

    path(
        'rest/pin_thread/<int:pk>/',
        views.PinThread.as_view(),
        name='pin-thread'
    ),

    path('rest/signup/', views.signup_rest, name='rest-signup'),

    path('rest/likedislike/<int:pk>/',
         views.like_dislike_post,
         name='rest-likedislike'
         ),

    path(
        'rest/validate_username/',
        views.validate_username,
        name='validate-username'
    ),

    path('rest/user_view/<int:pk>/', views.user_view, name='user-view'),
    path(
        'rest/forum_latest/',
        views.forum_latest_thread,
        name='rest-latest-thread'
    ),

    path(
        'rest/forum_threads/<int:pk>/',
        views.forum_threads,
        name='rest-forum-threads'
    ),
    path('rest/threads_bulk/', views.threads_bulk, name='rest-threads-bulk'),
    path(
        'rest/responses_bulk/',
        views.responses_bulk,
        name='rest-responses-bulk'
    ),

    path(
        'rest/thread_responses/<int:pk>/',
        views.thread_responses,
        name='rest-thread-responses'
    ),

    path('rest/logout/', views.logout, name='rest-logout'),

    # path(
    #     'rest/signup/',
    #     views.SignUp,
    #     name='rest-signup'
    # ),

    # Authentication
    path('rest/api-token-auth/', obtain_auth_token, name='rest-api-token-auth'),
    # path('api-token-verify/', verify_jwt_token),

    # Regular patterns
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'forums',
        views.forums,
        name='forums'
    ),
    path(
        'forum/<int:pk>',
        views.forum,
        name='forum'
    ),
    # path(
    #     'user/<int:pk>',
    #     views.user_view,
    #     name='user-view'
    # ),
    path(
        'user/<int:pk>/ban',
        views.ban_user,
        name='ban-user'
    ),
    path(
        'forum/<int:pk>/new-thread',
        views.new_thread,
        name='new-thread'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>/pin',
        views.pin_thread,
        name='pin-thread'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>',
        views.thread_view,
        name='thread-view'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>/respond',
        views.respond,
        name='respond-thread'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>/delete',
        views.delete_thread,
        name='thread-delete'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>/post/<int:ppk>/edit',
        views.edit_post,
        name='edit-post'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>/post/<int:ppk>/delete',
        views.delete_post,
        name='delete-post'
    ),
    path(
        'forum/<int:fpk>/thread/<int:tpk>/post/<int:ppk>/like/<int:upvote>',
        views.like_dislike_post,
        name='like-dislike-post'
    ),
    # AJAX #
    path(
        'ajax/validate_username/',
        views.validate_username,
        name='validate-username'
    ),
]
