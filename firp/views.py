from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from .models import *
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
class HomeView(View):
    template_name ='firp/index.html'
    def get(self,request):
        return render(request,self.template_name)


class LoginView(View):
    template_name="firp/login.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        try:
            user =User.objects.get(email=request.POST.get('email'))
                
        except:
            return render(request, self.template_name,{'error':True})
           
        else:
            user = authenticate(request, 
            username=user.username, 
            password=request.POST.get('password')
            )
            if user is None:
                return render(request,self.template_name,{'error':True})
            login(request,user)
            response= redirect('home')
            response.set_cookie('role','user')
            return response
        
        return render(request,self.template_name)

class AddFIRView(LoginRequiredMixin,View):
    template_name ='firp/addfir.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        fir =FIR()
        fir.unique_id=uuid.uuid4()
        fir.accused_name = request.POST.get('accused_name')
        fir.location =request.POST.get('location')
        fir.name = request.POST.get('name')
        fir.description =request.POST.get('description')
        fir.image =request.FILES.get('image')
        fir.save()
        return render(request,self.template_name)

class FirView(View):
    template_name = 'firp/firs.html'
    def get(self,request):
        firs= FIR.objects.all()
        return render(request,self.template_name,{'firs':firs})

class LogoutView(View,LoginRequiredMixin):
    def get(self,request):  
        logout(request)
        response=redirect('home')
        response.delete_cookie('role')
        return response