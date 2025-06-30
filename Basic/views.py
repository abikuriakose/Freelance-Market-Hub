from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=="POST":
        num1=int(request.POST.get('txt_number1'))
        num2=int(request.POST.get('txt_number2'))
        result=num1+num2
        return render(request,"Basic/Sum.html",{'result':result})
    else:
        return render(request,"Basic/Sum.html")   
    
def Calculator(request):
    if request.method=="POST":
       num1=int(request.POST.get('num1'))
       num2=int(request.POST.get('num2'))
       btn=request.POST.get("btn")
       if btn=="+":
           result=num1+num2
       elif btn=="-":
           result=num1-num2
       elif btn=="*":
           result=num1*num2
       elif btn=="/":
           result=num1/num2
       return render(request,"Basic/Calculator.html",{'result':result})
    else:
        return render(request,"Basic/Calculator.html") 
    
def LandS(request)  :
    if request.method=='POST':
        num1=int(request.POST.get('txt_number1'))
        num2=int(request.POST.get('txt_number2'))
        num3=int(request.POST.get('txt_number3'))

        if num1>num2 and num1>num3:
            l=num1
            if num2<num3:
                s=num2
            else:
                s=num3
        elif num2>num3:
            l=num2
            if num1<num3:
                s=num1
            else:
                s=num3
        else:
            l=num3
            if num1<num2:
                s=num1
            else:
                s=num2
            

        return render(request,"Basic/LandS.html",{'large':l,'small':s})
    else:
        return render(request,"Basic/LandS.html")
    
def Rank(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        gm="Mr."
        gf="Ms."
        space=" "
        if gender=="Male":
            fullname=gm+fname+space+lname
        else:
            fullname=gf+fname+space+lname
        dept=request.POST.get('dept')
        m1=int(request.POST.get('mark1'))
        m2=int(request.POST.get('mark2'))
        m3=int(request.POST.get('mark3'))
        tmark=m1+m2+m3
        
        p=round((tmark/300)*100,2)
        if(p>=90):
            grade="O"
        elif(p>80):
            grade="A"
        elif(p>70):
            grade="B"
        elif(p>60):
            grade="C"
        elif(p>50):
            grade="P"
        else:
            grade="F"
        
        return render(request,"Basic/Rank.html",{'fullname':fullname,'gender':gender,'department':dept,"tmark":tmark,'percentage':p,'grade':grade})
    else:
        return render(request,"Basic/Rank.html")