from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     content = """
#     <h1>Hello World</h1>
#     <h2>I'm learning Python</h2>
#     <p>Python is awesome !! </p>
#     """
#     return HttpResponse(content)

def home(request):
    people_info = [
      {"first" : "Jon", "last": "haris", "address": "KTM"},
      {"first" : "Jane", "last": "aris", "address": "BTM"},
      {"first" : "Fon", "last": "nais", "address": "BKT"},
      {"first" : "Kon", "last": "pariss", "address": "LTP"}
   ]
    return render(request, template_name="myapp/test.html", 
                  context={"heading" : "People Information", "infos" : people_info})


def python(request):
    name = request.GET.get("name")
    print(name)
    return render(request, template_name= "myapp/test1.html")


def test(request):
    # We can send query strings / query parameters in the urls
    # Everything sent after "?" in the url is querystring
    # Query strings can be multiple and are separated by ampersand (&).
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(f"<h1>Hello my name is {name}. I'm {age}</h1>")

def portfolio(request):
    return render (request,template_name = "myapp/portfolio.html")