from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)
from . import models

# Create your views here
class IndexView(TemplateView):
    template_name='index.html'

class schoollistview(ListView):
    context_object_name = 'schools'
    model =  models.school 


class schooldetailview(DetailView):
    context_object_name = 'school_detail'
    model = models.school
    template_name = 'cbvapp/school_detail.html'
    
class schoolcreateview(CreateView):
    fields = ('name','principal','location')
    model = models.school

class schoolupdateview(UpdateView):
    fields = ('name','principal')
    model = models.school

class schooldeleteview(DeleteView):
    model = models.school
    success_url = reverse_lazy("cbvapp:list")