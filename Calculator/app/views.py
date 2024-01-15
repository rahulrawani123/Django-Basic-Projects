from django.shortcuts import render

# Create your views here.

def Calculator(request):
    Output=""
    try:
        if request.method=="POST":
            value1=eval(request.POST.get('value1'))
            value2=eval(request.POST.get('value2'))
            operator=request.POST.get('operator')
            if operator=="+":
                Output=value1+value2
            elif operator=="-":
                Output=value1-value2
            elif operator=="*":
                Output=value1*value2
            elif operator=="/":
                Output=value1/value2
    except:
        Output="Invalid Value Entered value should be integer or float"
         
    return render(request,'Home.html',{'Output':Output,})
