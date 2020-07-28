from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import StudentForm
from .models import Student
# Create your views here.

#def index(request):
    #words = 'World!'
    #students = Student.objects.all()
    #return render(request,'index.html',context={'words':words})
    #return render(request,'index.html',context={'students':students})

def index(request):
    #students = Student.objects.all()
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

            '''cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['sex']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']'''
    else:
        form = StudentForm()
    
    context = {
        'students':students,
        'form':form,
    }

    return render(request,'index.html',context=context)

class IndexView(View):
    template_name="index.html"

    def get_context(self):
        students = Student.get_all()
        context = {
            'students':students,
        }
        return context;
    
    def get(self,request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form':form
        })
        return render(request,self.template_name,context=context)
    
    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context=self.get_context()
        context.update({
            'form':form
        })
        return render(request,self.template_name,context=context)