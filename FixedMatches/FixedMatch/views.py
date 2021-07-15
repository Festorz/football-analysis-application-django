import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from allauth.account.views import SignupView, View
from FixedMatch.forms import CommentForm, RegistrationForm, CodeForm
from .models import Match, Post, Prediction, MatchDescription
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from django.core.paginator import Paginator
from urllib.parse import quote 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
 




# Create your views here.

class UserSignUp(SignupView):
    template_name = 'account/signup.html'
    form_class = RegistrationForm
    redirect_field_name = 'next'
    view_name = 'account_signup'

    def get_context_data(self, **kwargs):
        ret = super(UserSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


def get_predictions(jsonfile):
    # data = open(str(jsonfile))
    data_dict = json.load(jsonfile)

    return data_dict


def home(request):
    games = Match.objects.all().order_by('-pk')
    blog = Post.objects.all().order_by('-pk')[:3]

    data = {
        'game': games,
        'blog_post':blog
    }
    description = MatchDescription.objects.filter(category='MT')
    if description.exists():
        content = description[0]
        desc = content.description_file
        text = desc.read().decode('utf8')
        data.update({
            'desc': text
        })

    return render(request, 'home-page.html', data)


@login_required
def game_predictions(request):
    item = Prediction.objects.all().order_by('-pk')
    data = {
        'game': item,
    }
    description = MatchDescription.objects.filter(category='PR')
    if description.exists():
        content = description[0]
        des = content.description_file
        text = des.read().decode('utf8')
        data.update({
            'desc': text
        })

    return render(request, 'betting-tips.html', data)



def is_valid(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class PaymentCode(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        form = CodeForm()
        data = {
            'form': form
        }
        return render(self.request, 'how-to-pay.html', data)

    def post(self, *args, **kwargs):
        form = CodeForm(self.request.POST or None)
        user = self.request.user
        if form.is_valid():
            code = form.cleaned_data.get('payment_code')
            if is_valid(code):
                code = code
                print(code)
                if user.payment_code == '':
                    user.payment_code = code
                    user.save()
                else:
                    User.objects.filter(username=user).update(
                        payment_code=code
                    )
            messages.info(self.request, 'code submission was successful')
            return redirect('/')
        else:
            messages.warning(self.request, 'Please fill in your transaction code')
            return redirect('match:pay')


def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    recent_posts = Post.objects.all().order_by('pk')[:4]


    data = {
        'posts':page_obj,
        'recent_post':recent_posts,
    }
    query = request.GET.get('q', None)
    if query is not None:
        search = Post.objects.filter(title__icontains=query)
        paginator = Paginator(search, 10)
        page_obj = paginator.get_page(page_number)
        print(search)
        data.update({
            'posts':page_obj
        })


    return render(request, 'blog.html', data)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    share_string = quote(post.intro)
    recent_posts = Post.objects.all().order_by('-pk')[:4]
    data = {
        'post': post,
        'recent':recent_posts,
        'share_string': share_string
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('match:post-detail', slug=post.slug)
    else: 
        form = CommentForm()
        data.update({
            'form':form
        })

    return render(request, 'blog-details.html', data)
@login_required
def blog_like(request, slug):
    post = Post.objects.get(slug=slug)
    post.likes.add(request.user)
    post.save()
    
    return HttpResponseRedirect(reverse('match:post-detail', args=[str(slug)]))