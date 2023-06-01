from django.shortcuts import render

# Create your views here.
def chatbot(request):
    if request.method =='POST':
        
    return render(request, 'chatbot.html')
