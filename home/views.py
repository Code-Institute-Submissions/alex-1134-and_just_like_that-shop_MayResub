from django.shortcuts import render


def index(request):
    """ Return index  """

    return render(request, 'home/index.html')
