from django.shortcuts import render
from .analysis import analysis as a

def index(request):
    return render(request, "index.html")


def text_analysis(request):
    if "submit-button" in request.POST:
        user_input = str(request.POST.get("entered"))
        
        #minimum charcter limit BERT
        if len(user_input) < 3:
            return render(request, "text_analysis.html", {"error": "Please enter atleast 3 characters!"})
        
        result = a.calculating(user_input)
        sentence = "The sentiment is "
        return render(request, "text_analysis.html",{"result": result, "sentence": sentence})
    
    return render(request, "text_analysis.html")