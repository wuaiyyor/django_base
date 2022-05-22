from django.shortcuts import render


# Create your views here.
def index(request):
    content = {
        "name": "马上双十一，点击有惊喜"
    }
    return render(request=request, template_name="book/index.html", context=content)
