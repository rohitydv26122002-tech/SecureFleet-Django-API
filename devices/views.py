from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Device
from .serializers import DeviceSerializer
from django.contrib.auth.decorators import login_required


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

@login_required
def device_dashboard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        Device.objects.create(name=name, status=status)
        return redirect('device_dashboard')


    devices = Device.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})

@login_required
def delete_device(request, device_id):
    device = Device.objects.get(id=device_id)
    device.delete()
    return redirect('device_dashboard')

@login_required
def edit_device(request, device_id):
    device = Device.objects.get(id=device_id)

    if request.method == 'POST':
        device.name = request.POST.get('name')
        device.status = request.POST.get('status')
        device.save()
        return redirect('device_dashboard')

    return render(request, 'devices/edit_device.html', {'device': device})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('device_dashboard')
        else:
            return render(request, 'devices/login.html', {'error': 'Invalid credentials'})

    return render(request, 'devices/login.html')