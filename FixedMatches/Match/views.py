from django.shortcuts import redirect


# Create your views here.
def login_redirect(request):
    return redirect('/match')
