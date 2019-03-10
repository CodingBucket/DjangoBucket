from django.conf.urls import url
from blog import views

#app_name = 'blog'
urlpatterns = [
    url('', views.PostListView.as_view(), name='post_list'),
    url('about/', views.AboutView.as_view(), name='about'),
    url('post/<int:id>', views.PostDetailView.as_view(), name='post_detail'),
    url('post/new', views.CreatePostView.as_view(), name='post_new'),
    url('post/<int:id>/edit', views.UpdatePostView.as_view(), name='post_edit'),
    url('post/<int:id>/remove', views.DeletePostView.as_view(), name='post_remove'),
    url('drafts', views.DraftListView.as_view(), name='post_draft_list'),
    url('post/<int:id>/comment', views.add_comment_to_post , name='add_comment_to_post'),
    url('comment/<int:id>/approve', views.comment_approve , name='comment_approve'),
    url('comment/<int:id>/remove', views.comment_remove , name='comment_remove'),
    url('post/<int:id>/publish', views.post_publish , name='post_publish'),
    url('demo', views.demo , name='demo'),
]