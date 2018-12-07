from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from .models import Receipt
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'receipts/index.html'
    context_object_name = 'receipts_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Receipt.objects.order_by('-purchase_date')

class DetailView(generic.DetailView):
    model = Receipt
    template_name = 'receipts/detail.html'


class ResultsView(generic.DetailView):
    model = Receipt
    template_name = 'receipts/results.html'
