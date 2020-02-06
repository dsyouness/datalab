from django.shortcuts import render, HttpResponse

# Create your views here.
def index_view(request):
    context = {'liste': [1, 2, 3],

               }
    return render(request, 'index.html', context)