from django.shortcuts import render

def main(request):
    people = [
        {"name": "Ram", "age": 30, "address": "KTM"},
        {"name": "Shyam", "age": 23, "address": "PKR"},
        {"name": "Hari", "age": 45, "address": "BRT"},
        {"name": "Sita", "age": 26, "address": "BKT"}
    ]
    context = {"people": people}
    return render(request, template_name='temp_inheritance/home.html', context = context)

def features(request):
    items = [
        {"name": "Laptop", "feature": "A portable coputer that can be used anywhere"},
        {"name": "Mouse", "feature": "A clicking input device of a computer"},
        {"name": "Keyboard", "feature": "An input device with keys"}
    ]
    return render (request, template_name = 'temp_inheritance/features.html', context={"items": items})

def pricing(request):
    prices = [
        {"item": "Laptop", "price": "NPR. 18,999,9 Rs"},
        {"item": "Mobile", "price": "NPR. 25,000 Rs"},
        {"item": "Ipad", "price": "NPR. 78,000 Rs"}

    ]
    return render (request, template_name = 'temp_inheritance/pricing.html', context={"prices": prices})