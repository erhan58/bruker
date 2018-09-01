# Patrick Höfner -- added basic "Listview" to save Datatable in Object
# Erhan Metin    -- added "search Bar" including "contains" lookuptype to Listview
# Patrick Höfner -- added second "collapsing search field" with "or" functionality
# Patrick Höfner -- added Dropdown selection for an "WHERE" clause according to the contains lookuptype




from django.shortcuts import render
from Frontend import models
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from .models import Speciesgenus
from .models import Msp
from .models import Strain
from .models import Customer
from .models import Dnasequence
from .models import Measurement
from .models import Measuringdevice
from .models import Synonym
from .models import Logcustomer

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q





# Create your views here.

def home(request):


    # return HttpResponse('<p>home view</p>')
    return render(request, 'home.html',)

class TemplateView(ListView):

    def get_queryset(self, *args, **kwargs):
        queryset_list = self.model.objects.all()                       # list for running queries
        queryset_result = self.model.objects.all()                     # Shown list in the template
        query_1 = self.request.GET.get("q_1", None)                    # user-input-field 1
        query_2 = self.request.GET.get("q_2", None)                    # user-input-field 2
        attribute = self.request.GET.get("dropdown", None)
        if attribute is None:
            attribute = ''                                             # None toString 
        filter = attribute + '__' + 'icontains'

        # attribute_model = getattr(self.model, attribute, None)

        if query_1 and query_2 is not None:
            queryset_list_1 = queryset_list.filter(**{filter:query_1}) # different writing to attribute__icontains = query
            queryset_list_2 = queryset_list.filter(**{filter:query_2})
            queryset_result = (queryset_list_1 | queryset_list_2)      # union of two querysets
        if query_1 is not None:
                if query_2 == '':
                   queryset_result = queryset_list.filter(**{filter:query_1})
        return queryset_result

def home(request):
    # return HttpResponse('<p>home view</p>')
    return render(request, 'home.html',)

class mspListView(TemplateView):
    model = Msp
    template_name = 'msp_list.html' # Default: <app_label>/<model_name>_list.html
    context_object_name = 'Msp'     # Default: object_list
    paginate_by = 200               # pagination
    queryset = model.objects.all()  # Default: Model.objects.all()

# def speciesgenus(request):    
#    Speciesgenuses = Speciesgenus.objects.all()
#    return render(request,'speciesgenus.html', {'Speciesgenuses': Speciesgenuses})

class speciesgenusListView(ListView):
    model = Speciesgenus
    paginate_by = 200

class strainListView(ListView):
    model = Strain
    queryset = Strain.objects.order_by('strain_id')
    paginate_by = 200

class customerListView(ListView):
    model = Customer
    queryset = Customer.objects.order_by('customer_id')
    paginate_by = 200

class dnasequenceListView(ListView):
    model = Dnasequence
    queryset = Dnasequence.objects.order_by('dna_id')
    paginate_by = 200

class measurementListView(ListView):
    model = Measurement
    queryset = Measurement.objects.order_by('measurement_id')
    paginate_by = 200

class measuringdeviceListView(ListView):
    model = Measuringdevice
    queryset = Measuringdevice.objects.order_by('md_id')
    paginate_by = 200

class synonymListView(ListView):
    model = Synonym
    queryset = Synonym.objects.order_by('synonym_id')
    paginate_by = 200

class logcustomerListView(ListView):
    model = Logcustomer
    queryset = Logcustomer.objects.order_by('log_id')
    paginate_by = 200