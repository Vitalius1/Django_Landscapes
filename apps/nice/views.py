from django.shortcuts import render, redirect

def index(request):
    return render(request, "nice/index.html")

def error(request):
    context = {
        'error': "Please follow the directions :)"
    }
    return render(request, "nice/index.html", context)

def show(request, number):
    try:
        int(number)
    except:
        return redirect('/error')
    print (number)
    if int(number) not in range(1, 51):
        return redirect('/error')
    else:
        num = int(number)
        if num in range(1, 11):
            picture = "snow"
        elif num in range(11, 21):
            picture = "desert"
        elif num in range(20, 31):
            picture = "forest"
        elif num in range(30, 41):
            picture = "vineyard"
        elif num in range(40, 51):
            picture = "tropical"
        context = {
            "landscape": picture
        }
        print (picture)
        print ('*'* 50)
        return render(request, "nice/landscape.html", context)
# Create your views here.
