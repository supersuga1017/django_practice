from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import  messages
from .forms import InquiryForm

import logging

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"

# class InquiryView((generic.TemplateView):):
class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('inquiry sent by {}'.format(form.cleaned_data['name']) )
        messages.success(self.request,'お問い合わせが完了しました。')
        return super().form_valid(form)

class SugaView(generic.TemplateView):
    template_name = "suga.html"

class DiaryListView(generic.TemplateView):
    # model = Diary
    template_name = "diary_list.html"
    # paginnate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user = self.request.user).order_by('created_at')
        return diaries




