from cgitb import lookup
from codecs import lookup_error
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,UpdateView
from prodetail.models import details,education,occupation,family,siblings,address,profilelink
from prodetail.forms import detailsform,educationform,occupationform,familyform,sibilingsform,addressform,profilelinkform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

class profilehomeview(TemplateView):
    template_name="profilehome.html"

class detailview(LoginRequiredMixin,CreateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=details
    form_class=detailsform
    context_object_name='form'
    success_url="/pro/education/"
    def form_valid(self, form):
        form=super(detailview,self).form_valid(form)
        messages.success(self.request,'details is submitted!')
        return form

class educationview(LoginRequiredMixin,CreateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=education
    form_class=educationform
    context_object_name='form'
    success_url="/pro/occupation/"

    def form_valid(self, form):
        super(educationview,self).form_valid(form)
        messages.success(self.request,'education details is submitted!')
        return HttpResponseRedirect(self.get_success_url())

class occupationview(LoginRequiredMixin,CreateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=occupation
    form_class=occupationform
    context_object_name='form'
    success_url="/pro/family/"

    def form_valid(self, form):
        super(occupationview,self).form_valid(form)
        messages.success(self.request,'occupation details is submitted!')
        return HttpResponseRedirect(self.get_success_url())

class familyview(LoginRequiredMixin,CreateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=family
    form_class=familyform
    context_object_name='form'
    success_url='/pro/siblings/'

    def form_valid(self, form):
        super(familyview,self).form_valid(form)
        messages.success(self.request,'family details is submitted!')
        return HttpResponseRedirect(self.get_success_url())

class siblingsview(LoginRequiredMixin,CreateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=siblings
    form_class=sibilingsform
    context_object_name='form'
    success_url="/pro/address/"

    def form_valid(self, form):
        super(siblingsview,self).form_valid(form)
        messages.success(self.request,'siblings details is submitted!')
        return HttpResponseRedirect(self.get_success_url())
    
class addressview(LoginRequiredMixin,CreateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=address
    form_class=addressform
    context_object_name='form'
    success_url="/pro/profilelink/"

    def form_valid(self, form):
        super(addressview,self).form_valid(form)
        messages.success(self.request,'address details is submitted!')
        return HttpResponseRedirect(self.get_success_url())

class profilelinkview(LoginRequiredMixin,CreateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=profilelink
    form_class=profilelinkform
    context_object_name='form'
    success_url="/authe/home/"

    def form_valid(self, form):
        super(profilelinkview,self).form_valid(form)
        messages.success(self.request,'profilelink details is submitted!')
        return HttpResponseRedirect(self.get_success_url())


class udetailview(LoginRequiredMixin,UpdateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=details
    form_class=detailsform
    context_object_name='form'
    success_url="/pro/ueducation/"
    lookup_field='userid'
    def form_valid(self, form):
        form=super(detailview,self).form_valid(form)
        messages.success(self.request,'details is submitted!')
        return form

class ueducationview(LoginRequiredMixin,UpdateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=education
    form_class=educationform
    context_object_name='form'
    success_url="/pro/uoccupation/"

    def form_valid(self, form):
        super(educationview,self).form_valid(form)
        messages.success(self.request,'education details is submitted!')
        return HttpResponseRedirect(self.get_success_url())

class uoccupationview(LoginRequiredMixin,UpdateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=occupation
    form_class=occupationform
    context_object_name='form'
    success_url="/pro/ufamily/"

    def form_valid(self, form):
        super(occupationview,self).form_valid(form)
        messages.success(self.request,'occupation details is submitted!')
        return HttpResponseRedirect(self.get_success_url())

class ufamilyview(LoginRequiredMixin,UpdateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=family
    form_class=familyform
    context_object_name='form'
    success_url='/pro/usiblings/'

    def form_valid(self, form):
        super(familyview,self).form_valid(form)
        messages.success(self.request,'family details is submitted!')
        return HttpResponseRedirect(self.get_success_url())

class usiblingsview(LoginRequiredMixin,UpdateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=siblings
    form_class=sibilingsform
    context_object_name='form'
    success_url="/pro/uaddress/"

    def form_valid(self, form):
        super(siblingsview,self).form_valid(form)
        messages.success(self.request,'siblings details is submitted!')
        return HttpResponseRedirect(self.get_success_url())
    
class uaddressview(LoginRequiredMixin,UpdateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=address
    form_class=addressform
    context_object_name='form'
    success_url="/pro/uprofilelink/"

    def form_valid(self, form):
        super(addressview,self).form_valid(form)
        messages.success(self.request,'address details is submitted!')
        return HttpResponseRedirect(self.get_success_url())

class uprofilelinkview(LoginRequiredMixin,UpdateView):
    login_url='/authe/login/'
    template_name='details.html'
    model=profilelink
    form_class=profilelinkform
    context_object_name='form'
    success_url="/authe/home/"
    def form_valid(self, form):
        super(profilelinkview,self).form_valid(form)
        messages.success(self.request,'profilelink details is submitted!')
        return HttpResponseRedirect(self.get_success_url())