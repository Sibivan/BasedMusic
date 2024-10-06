from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from .models import Instrument
from .forms import InstrumentForm
def index(request):
     return render(request, 'basedapp/index.html')

def database_view(request):
     if request.method == "POST":
        instrument_type = request.POST.get('instrument_type')
        instrument_manufacturer = request.POST.get('instrument_manufacturer')
        cover = request.FILES.get('cover')  # Получаем файл изображения
        instock_value = request.POST.get('instock')
        is_instock = True if instock_value == 'yes' else False
        strings = request.POST.get('strings')
        strings_bool = True if strings == 'on' else False
        mediator = request.POST.get('mediator')
        mediator_bool = True if mediator == 'on' else False
        capidaster = request.POST.get('capidaster')
        capidaster_bool = True if capidaster == 'on' else False

        # Создаем новый объект Instrument и сохраняем его в базе данных
        new_instrument = Instrument(
            types=instrument_type,
            manufacturer=instrument_manufacturer,
            cover=cover,
            isonbase=is_instock,
            stronbox=strings_bool,
            medonbox=mediator_bool,
            caponbox=capidaster_bool

        )
        new_instrument.save()

        return redirect('database')
     data = Instrument.objects.all()
     return render(request, 'basedapp/database.html', {'data': data})

class deleteinstrument(DeleteView):
     model=Instrument
     success_url='/database_view'
     template_name='basedapp/delete.html'

class updateinstrument(UpdateView):
     model=Instrument
     template_name='basedapp/update.html'
     form_class=InstrumentForm
     def get_success_url(self):
           #data = Instrument.objects.all()
           return reverse('database')
           

