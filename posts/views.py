from django.shortcuts import render, redirect

# Create your views here.
def feeds(request):
    if not request.user.is_authenticated: #로그인 상태가 아닐 경우
        return redirect("/users/login/")
    return render(request, "posts/feeds.html")