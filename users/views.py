from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid(): # Data가 유효할 경우
            username = form.cleaned_data['username']
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user) #로그인 진행
                return redirect("/posts/feeds/") #게시물로 이동
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")

        #로그인 실패(재입력 필요, 유저정보 없음 등)일 경우 다시 로그인 페이지로.
        context = {"form" : form }

        return render(request, "users/login.html", context)
    else:
        form = LoginForm()
        context = {"form" : form }
        return render(request, "users/login.html", context)

def logout_view(request):
    logout(request)

    return redirect("/users/login")