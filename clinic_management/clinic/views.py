from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Doctor, Patient, Appointment
from .forms import UserRegistrationForm, AppointmentForm
from django.http import HttpResponse

def test_template(request):
    return render(request, "your_video_template.html")

def video_call(request):
    return render(request, 'clinic/video_call.html')

def doctor_info(request):
    return render(request, 'clinic/doctor_info.html')

def prescription(request):
    return render(request, 'clinic/prescription.html')

def home(request):
    return render(request, 'clinic/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'clinic/register.html', {'form': form})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'clinic/book_appointment.html', {'form': form})
