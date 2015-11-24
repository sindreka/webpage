from django.shortcuts import render

from startpage.models import Startpage

# Create your views here.
def StartpageView(request):
    try:
        startpage_text = Startpage.objects.get(pk=1)
    except:
        startpage_text = Startpage.objects.all()
    context = {"startpage_text": startpage_text}
    return render(request, 'startpage.html', context=context)
