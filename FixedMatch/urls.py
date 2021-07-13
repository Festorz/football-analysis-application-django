from django.urls import path
from FixedMatch.views import home, blog, SignupView, game_predictions, PaymentCode, post_detail

app_name = 'match'
urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('betting-tips/', game_predictions, name='predictions'),
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('how-to-pay/', PaymentCode.as_view(), name='pay'),
    path('<slug>/', post_detail, name='post-detail'),
]
 