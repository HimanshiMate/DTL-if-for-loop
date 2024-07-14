from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'himanshi',
                                       'city':'bhopal',
                                       'language':['python','java','c','kotlin','cobalt']})
