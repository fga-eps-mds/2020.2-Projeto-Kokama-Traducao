from django.http import HttpResponse
from django.shortcuts import render

def add_translate(request):
    if(request.user.is_superuser):
        if(request.method == 'GET'):
            return render(request, 'add_translation.html')
        elif(request.method == 'POST'):
            print(request.POST.get('kokama_word'))

    else:
        return HttpResponse('APENAS ADMINISTRADORES')
