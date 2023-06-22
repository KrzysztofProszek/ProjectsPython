from django.shortcuts import render, HttpResponse


# model Django == Python class
# QuerySet Django == obiekt klasy Pythona
# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
