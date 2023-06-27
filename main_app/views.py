from django.shortcuts import render

finches = [
    {'name': 'Zebra Finch', 'species': 'Taeniopygia guttata', 'description': 'Small, gray and white finch with a distinctive red beak', 'age': 1},
    {'name': 'Gouldian Finch', 'species': 'Erythrura gouldiae', 'description': 'Colorful finch with a purple chest, yellow belly, and green back', 'age': 2},
    {'name': 'Society Finch', 'species': 'Lonchura domestica', 'description': 'Small, brown and white finch with a pleasant song', 'age': 3},
    {'name': 'Java Sparrow', 'species': 'Lonchura oryzivora', 'description': 'Large, gray and white finch with a distinctive pink beak', 'age': 1},
    {'name': 'Canary', 'species': 'Serinus canaria', 'description': 'Small, yellow finch with a beautiful song', 'age': 2},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finch/index.html')