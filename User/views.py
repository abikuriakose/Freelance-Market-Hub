from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
# Create your views here.
def Home(request):
    return render(request,"User/Home.html ")

def Myprofile(request):
        client=tbl_client.objects.get(id=request.session['uid'])
        return render(request,"User/Myprofile.html",{'client':client})

def Editprofile(request):
      client=tbl_client.objects.get(id=request.session['uid'])
      if request.method=="POST":
            client.client_name=request.POST.get("client_name")
            client.client_email=request.POST.get("client_email")
            client.client_contact=request.POST.get("client_contact")
            client.client_address=request.POST.get("client_address")
            client.save()
            return redirect('User:Myprofile')
      else:
        return render(request,"User/Editprofile.html",{'client':client})
      
def Changepassword(request):
    client=tbl_client.objects.get(id=request.session['uid'])
    if request.method=="POST":
        oldpassword=request.POST.get("oldpassword")
        newpassword=request.POST.get("newpassword")
        cnewpassword=request.POST.get("cnewpassword")
        if client.client_password==oldpassword:
            if newpassword==cnewpassword:
                  client.client_password=newpassword
                  client.save()
                  return redirect('User:Myprofile')
            else:
                 alert="Password does not match!"
                 return render(request,"User/Changepassword.html",{'msg':alert})

        else:
             alert="Current password does not match!"
             return render(request,"User/Changepassword.html",{'msg':alert})
    else:
        return render(request,"User/Changepassword.html",)
    
def Complaint(request):
    client=tbl_client.objects.get(id=request.session['uid'])
    tblcomp=tbl_complaint.objects.all()
    if request.method=="POST":
        subject=request.POST.get("txt_subject")
        complaint=request.POST.get("txt_complaint")
       
        tbl_complaint.objects.create(comp_subject=subject,comp_details=complaint,client_id=client)
        return redirect('User:Myprofile')
    else:
        return render(request,"User/Complaint.html")