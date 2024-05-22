from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Si puede ver este texto el servicios está funcionando correctamente")
