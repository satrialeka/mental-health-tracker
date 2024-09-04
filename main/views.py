from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245094',
        'name': 'Muhammad Satria Aleka Ramadhan',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
