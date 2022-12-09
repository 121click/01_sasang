from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from member.forms import UserForm
from .models import Member
from django.utils import timezone
from django.http import HttpResponse
import datetime

# def signup(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user_pw = request.POST.get('user_pw')
#         user_name = request.POST.get('user_name')
#         user_birth = request.POST.get('user_birth')
#         if datetime.date.today().year - int(datetime.datetime.strptime(user_birth, "%Y-%m-%d").year) < 19:
#             return HttpResponse(
#         "<script>alert('나이가 너무 어립니다.\\n\\n메인페이지로 돌아갑니다.');location.href='/sstest/main';</script>")
#         user_gender = request.POST.get('user_gender')

#         m = Member(
#             user_id=user_id, user_pw=user_pw, user_name=user_name, user_birth=user_birth, user_gender=user_gender
#         )
#         m.date_joined = timezone.now()
#         m.save()
#         return HttpResponse(
#             '가입 완료<br>%s %s %s %s %s' % (user_id, user_pw, user_name, user_birth, user_gender))
#     else:
#       return render(request, 'member/signup.html')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/member/login')
    else:
        form = UserForm()
    return render(request, 'member/signup.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user_pw = request.POST.get('user_pw')
#         try:
#             m = Member.objects.get(user_id=user_id, user_pw=user_pw)
#         except Member.DoesNotExist as e:
#             return HttpResponse('로그인 실패')
#     else:
#         return render(request, 'member/login.html')
