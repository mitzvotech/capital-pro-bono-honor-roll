from .forms import HonoreeForm
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Honoree

class HonoreeView(FormView):
    template_name = 'honoree_form.html'
    form_class = HonoreeForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        
#		form.send_email()
		return super(HonoreeView, self).form_valid(form)

class HonoreeCreate(CreateView):
    model = Honoree
    fields = ['affiliation','first_name','middle_name','last_name','email','honor']
    
class HonoreeUpdate(UpdateView):
    model = Honoree
    fields = ['affiliation','first_name','middle_name','last_name','email','honor']

class HonoreeDelete(DeleteView):
    model = Honoree
    success_url = reverse_lazy('Honoree-list')