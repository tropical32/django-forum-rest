from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from forumapp import views

router = DefaultRouter()
router.register('forums', views.ForumViewSet)
router.register('threads', views.ThreadViewSet)

urlpatterns = [
    # Router path
    path('rest/', include(router.urls)),

    # Authentication
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),

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
    path(
        'user/<int:pk>',
        views.user_view,
        name='user-view'
    ),
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
