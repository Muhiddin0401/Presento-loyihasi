from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SmsForm, SignUpForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LogoutView
from django.utils import timezone
from .models import Sms
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SmsForm(request.POST)
        if form.is_valid():
            # Forma ma'lumotlarini saqlash
            Sms.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                text=form.cleaned_data['text']
            )
            messages.success(request, "Xabaringiz yuborildi. Rahmat!")
            return redirect('home')
        else:
            messages.error(request, "Xatolik yuz berdi. Iltimos, barcha maydonlarni to‘g‘ri to‘ldiring.")
    else:
        form = SmsForm()
    return render(request, 'index.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']

@login_required
def profile(request):
    return render(request, 'profile.html', {'user':request.user})

@login_required
def superuser_required(user):
    return user.is_superuser

@login_required
def admin_messages(request):
    if not request.user.is_superuser:
        messages.error(request, "Bu sahifaga faqat superuserlar kira oladi!")
        return redirect('home')
    messages_list = Sms.objects.all().order_by('-created_at')
    return render(request, 'messeges.html', {'messages': messages_list})

@login_required
def answer_message(request, message_id):
    if not request.user.is_superuser:
        messages.error(request, "Bu amalni faqat superuserlar bajarishi mumkin!")
        return redirect('admin_messages')
    message = get_object_or_404(Sms, id=message_id)
    if request.method == 'POST':
        answer_text = request.POST.get('answer')
        if answer_text:
            message.answer = answer_text
            message.is_answered = True
            message.answered_at = timezone.now()
            message.save()
            messages.success(request, "Javob muvaffaqiyatli yuborildi!")
            return redirect('admin_messages')
        else:
            messages.error(request, "Javob matni bo‘sh bo‘lmasligi kerak!")
    return render(request, 'answer_message.html', {'message': message})

def custom_logout(request):
    logout(request)
    messages.success(request, "Siz tizimdan muvaffaqiyatli chiqdingiz!")
    return redirect('home')
