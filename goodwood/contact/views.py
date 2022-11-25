from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic import View

# class ContactView(View):
#     def contact(self,request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print('123')
#         return redirect('adv.html')

# def success_message(request):
#     pass