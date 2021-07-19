from django.urls import path
from FixedMatch.views import home, blog, SignupView, game_predictions, PaymentCode, post_detail, blog_like

app_name = 'match'
urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('betting-tips/', game_predictions, name='predictions'),
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('how-to-pay/', PaymentCode.as_view(), name='pay'),
    path('blog/<slug>/', post_detail, name='post-detail'),
    path('like/<slug>/', blog_like, name='like-post')
]
 