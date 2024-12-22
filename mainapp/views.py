from django.shortcuts import render

def home_view(request):
    import os
    print("TEMPLATE DIRS:", os.getcwd())
    context = {'message': "Hi, this is Jack"}
    return render(request, 'mainapp/home.html', context)  # Use full path to ensure it's picked up
