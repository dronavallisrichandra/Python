from django.shortcuts import render, redirect
from .models import TechUser,JobUser, JobPost, Profile,JobApply,HrUser
from .forms import TechUserCreate, JobUserCreate, JobPostCreate, ProfileCreate, JobApplyCreate, HrUserCreate
import sys
from django.http import HttpResponse

def index(request):

    if request.method == "POST":
        title = request.POST.get('job')
        r_sel= JobPost.objects.filter(JobTitle__contains=title)
        if r_sel is not None:
            return render(request, 'index.html',{'shelf':r_sel})
      
    return render(request, 'index.html')


def findjob(request):
    return render(request,'findjob.html')

def about(request):
    return render(request,'about.html')

def hrlogin(request):

    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            
            print("Hello world",username,password)
            #print("retive from database",Adminlogin.objects.get(username))
            enter=HrUser.objects.get(username=username,password=password)

            print(enter.username)

            #creating the session id
            request.session["name"]=enter.username 

            return redirect('HrHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass
    return render(request,'hrlogin.html')

def jslogin(request):
    if request.method == "POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            
            print("Hello world",username,password)
            #print("retive from database",Adminlogin.objects.get(username))
            enter=JobUser.objects.get(username=username,password=password)

            print(enter.username)

            #creating the session id
            request.session["name"]=enter.username 

            return redirect('JobHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass
    return render(request,'jslogin.html')

def ttlogin(request):

    if request.method == "POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            
            print("Hello world",username,password)
            #print("retive from database",Adminlogin.objects.get(username))
            enter=TechUser.objects.get(username=username,password=password)

            print(enter.username)

            #creating the session id
            request.session["name"]=enter.username 

            return redirect('TechHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass
    return render(request,'ttlogin.html')
def TechHome(request):

    df=[]

    username=request.session["name"]

    tesing="welcome"
    return render(request,'TechHome.html',{'uname':username,'testing':tesing})

def JobHome(request):

    df=[]

    username=request.session["name"]

    tesing="welcome"
    return render(request,'JobHome.html',{'uname':username,'testing':tesing})

def HrHome(request):

    df=[]

    username=request.session["name"]

    tesing="welcome"
    return render(request,'HrHome.html',{'uname':username,'testing':tesing})

def contact(request):
    return render(request,'contact.html')


def techregister(request):

   upload = TechUserCreate()

   if request.method == 'POST':
       upload = TechUserCreate(request.POST,request.FILES)
       if upload.is_valid():
           upload.save()
           return redirect('UserRegister1')
        
       else:
            return HttpResponse("your form is wrong")
   else:
       return render(request,'techregister.html',{'upload_form':upload})
    

def UserRegister1(request):
    return render(request,"UserSuccess.html")


def jsregister(request):

   upload = JobUserCreate()
   if request.method == 'POST':
       upload = JobUserCreate(request.POST,request.FILES)
       if upload.is_valid():
           upload.save()
           return redirect('UserRegister1')
        
       else:
            return HttpResponse("your form is wrong")
   else:
       return render(request,'jsregister.html',{'upload_form':upload})



def PostJob(request):
    
    upload = JobPostCreate()

    if request.method == 'POST':
        upload = JobPostCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('ViewPostJob')
        else:
            return HttpResponse("your form is wrong")
    else:
        return render(request,'PostJob.html',{'upload_form':upload})

def ViewPostJob(request):

    shelf = JobPost.objects.all()

    return render(request,"ViewPostJob.html",{'shelf':shelf})

def ViewJobs(request):

    shelf = JobPost.objects.all()

    return render(request,"ViewJobs.html",{'shelf':shelf})

def ViewHrJobs(request):

    shelf = JobPost.objects.all()

    return render(request,"ViewHrJobs.html",{'shelf':shelf})

def UpdateJob(request,r_id):

    r_id=int(r_id)

    print("The rid is ",r_id)

    try:
        r_sel=JobPost.objects.get(id=r_id)
    
    except JobPost.DoesNotExist:
        return redirect('index')

    r_form=JobPostCreate(request.POST or None, instance=r_sel)

    if r_form.is_valid():

        r_form.save()

        return redirect('ViewPostJob')
    
    return render(request,'UpdateJob.html',{'upload_form':r_form})

def ApplyJob(request,r_id):

    r_id=int(r_id)

    username = request.session["name"]

    r_sel= JobApply.objects.filter(username=request.session["name"],job_id=r_id).first()
    msg = "no work"
    if r_sel is not None:
       msg = "You alread applied for the Job"
    else:
        aj = JobApply(job_id = r_id, username = username)
        aj.save()
        msg = "Your Application Sent Sucessfully"
        
    return render(request,'Mymessage.html',{'msg':msg})

        
def JobApplicants(request,r_id):

    r_id=int(r_id)

    username = request.session["name"]

    r_sel= JobApply.objects.filter(job_id=r_id)

    return render(request,'JobApplicants.html',{'shelf':r_sel})

def UserDetailsHr(request,u_na):

    username = request.session["name"]

    r_sel= Profile.objects.filter(username_id=u_na)

    return render(request,'UserDetails.html',{'shelf':r_sel})





def DeleteJob(request, d_id):
	d_id = int(d_id)
	try:
		Job_sel = JobPost.objects.get(id = d_id)
	except JobPost.DoesNotExist:
		return redirect('index')
	Job_sel.delete()
	return redirect('ViewPostJob')


def Profil(request):
    
   #r_sel=Profile.objects.get(username=request.session["name"])
   r_sel= Profile.objects.filter(username=request.session["name"]).first()

   if r_sel is not None:
       return redirect("DisplayProfile")

   elif request.method == 'POST':
       upload = ProfileCreate(request.POST,request.FILES)
       #upload.fields['username']=request.session["name"]
       if upload.is_valid():
           upload.save()
           return redirect('Profil')
       else:
            error_message = "\n".join(["{}: {}".format(field, ", ".join(errors)) for field, errors in upload.errors.items()])
            return HttpResponse(f"Form errors:\n{error_message}", status=400)
            return HttpResponse("your form is wrong")
   else:
       #initial_data = {'experience': 1,'username':'vinay'}
       initial_data = {'username':request.session["name"]}
       upload = ProfileCreate(initial_data)
       #upload.fields['username'].widget.attrs['disabled'] = True
        #upload.experience=1

       return render(request,'Profile.html',{'upload_form':upload})

def DisplayProfile(request):

    r_sel= Profile.objects.filter(username=request.session["name"]).first()

    return render(request,'DisplayProfile.html',{'upload_form':r_sel})     
