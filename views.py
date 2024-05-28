from django.shortcuts import render,redirect
from . models import oreg_tbl
from . models import renewal_tbl
from . models import emergency_tbl
# from . views import redirect
# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def onlinereg(request):
    if request.method=="POST":
        fnm = request.POST.get('fst')
        lnm = request.POST.get('lst')
        dob = request.POST.get('dob')
        eml = request.POST.get('em')
        cdept = request.POST.get('cdpt')
        cltm = request.POST.get('ctime')
        obj = oreg_tbl.objects.create(fn=fnm,ln=lnm,db=dob,email=eml,cltdp=cdept,cltme=cltm)
        obj.save()
        if obj:
            return render(request,"onlinereg1.html")
        else:
            return render(request,"onlinereg.html")
    else:
        return render(request,"onlinereg.html")     
    
# def log(request):
#     if request.method=='POST':
#         eml = request.POST.get('em')
#         psw = request.POST.get('ps')
#         obj = oreg_tbl.objects.filter(email=eml,ps=psw)
#         if obj:
#            request.session['ema']=eml
#            request.session['psa']=psw
#            for ls in obj:
#                idno=ls.id
#                request.session['idn']=idno
#                return render(request,"home.html") 
#            else:
#                msg="Invalid Email id & password"
#                request.session['ema']=''
#                request.session['psa']=''  
#                return render(request,"login.html",{'error:msg'})
#         else:
#             return render(request,"login.html")   
             


def renewal(request):
    if request.method=="POST":
        fnme = request.POST.get('flnm')
        ads = request.POST.get('adrs')
        dob = request.POST.get('dob')
        email = request.POST.get('eml')
        phne = request.POST.get('ph')
        ipr = request.POST.get('ip')
        ipnmr = request.POST.get('ipn')
        obj = renewal_tbl.objects.create(fnm=fnme,adr=ads,db=dob,em=email,phn=phne,ipdr=ipr,ipnm=ipnmr)
        obj.save()   
        if obj:
            return render(request,"renewal1.html") 
        else:
            return render(request,"renewal.html")
    else:
        return render(request,"renewal.html")   

def renewal2(request):
    obj=renewal_tbl.objects.all()
    return render(request,"renewal2.html",{"data":obj})
def edit(request):
    idno=request.GET.get('idn')
    obj=renewal_tbl.objects.get(id=idno)
    return render(request,"renewal3.html",{"data":obj})

def update(request):
    if request.method=="POST":
        idn=request.POST.get('idno')
        fname=request.POST.get('flnm')
        addrs=request.POST.get('adrs')
        dbth=request.POST.get('dob')
        email=request.POST.get('eml')
        phon=request.POST.get('ph')
        insp=request.POST.get('ip')
        inpn=request.POST.get('ipn')
        obj=renewal_tbl.objects.get(id=idn)
        obj.fnm=fname
        obj.adr=addrs
        obj.db=dbth
        obj.em=email
        obj.phn=phon
        obj.ipdr=insp
        obj.ipnm=inpn
        obj.save()
        return redirect("renewal2/renewal2")
    return render(request,"renewal3.html")  

def delete(request):
    idno=request.GET.get('idn')
    obj=renewal_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect("renewal2/renewal2")

def emergency(request):
    if request.method=='POST':
        pname = request.POST.get('pn')
        ag = request.POST.get('ag')
        plce = request.POST.get('pl')
        cdtn = request.POST.get('cndn')
        obj = emergency_tbl.objects.create(pnm=pname,age=ag,plc=plce,cdn=cdtn)
        obj.save()
        if obj:
            return render(request,"emergency1.html")
        else:
            return render(request,"emergeny.html")
    else:
        return render(request,"emergency.html")
    
def smart_card(request):
    patient_id = request.GET.get('idn')
    patient = renewal_tbl.objects.get(id=patient_id)
    return render(request, 'smt.html', {'datas': patient})

def contact(request):
    return render(request,"contact.html")








        

