from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "name": "双十一，点击有惊喜",
    }
    return render(request, "book/index.html", context)
