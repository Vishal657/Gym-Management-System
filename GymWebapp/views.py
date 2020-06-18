from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from GymWebapp.models import Packages,Subscription,Customer_Details,Workoutplan
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login,logout
from datetime import datetime,timedelta
from django.views.decorators.csrf import csrf_exempt
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'
def home(request):
    return render(request,'home.html') 

def signup(request):
    if request.method == 'POST':
        name = request.POST['customer_name']
        name = name.strip()
        user_name = request.POST['username']
        user_name = user_name.strip()
        number = request.POST['number']
        number = number.strip()
        password = request.POST['pass1']
        password1 = request.POST['pass2']
        gender = request.POST['gender']
        a = Customer_Details.objects.filter(username=user_name).count()

        if a == 0:
            user = Customer_Details(name=name,username=user_name,PhoneNumber=number,password=password1,gender=gender)
            user.save()
            return render(request,'home.html',{'mess' : ' ' })
        
        else:
            return render(request,'signup.html',{'username' : user_name })
        
    else:
        return render(request,'signup.html')

def cushome(request):
        if 'sess' in request.session:
            greeting:str
            now = datetime.now()
            hour = now.hour
            if hour < 12:
                greeting = "Good morning !"
            elif hour < 18:
                greeting = "Good afternoon !"
            else:
                greeting = "Good night !"
            x=Customer_Details.objects.get(id=request.session['sess'])
            S=Subscription.objects.filter(customer_id=int(x.id))
            if len(S) != 0:
                Sa=Subscription.objects.get(customer_id=int(x.id))
                if now.date() == Sa.end_date:
                    Sa.delete()
                    return render(request,'customer_page.html',{'z' : x,'gre':greeting})
                else:
                    return render(request,'customer_page.html',{'z' : x,'gre':greeting,'Su':Sa,'pa':Packages.objects.get(id=int(Sa.package_id))})
            else:
                return render(request,'customer_page.html',{'z' : x,'gre':greeting})
        else:
            return render(request,'home.html')

def logmeout(request):
    if 'sess' in request.session:
        logout(request)
        return render(request,'home.html',{'lol':'lol'})
    else:
            return render(request,'home.html')

def T(request):
    try:
        if request.method == 'POST' :
        
            m1 = request.POST['m1']
            m2 = request.POST['m2']
            m3 = request.POST['m3']
            m4 = request.POST['m4']
            m5 = request.POST['m5']
            t1 = request.POST['t1']
            t2 = request.POST['t2']
            t3 = request.POST['t3']
            t4 = request.POST['t4']
            t5 = request.POST['t5']
            w1 = request.POST['w1']
            w2 = request.POST['w2']
            w3 = request.POST['w3']
            w4 = request.POST['w4']
            w5 = request.POST['w5']
            th1 = request.POST['th1']
            th2 = request.POST['th2']
            th3= request.POST['th3']
            th4 = request.POST['th4']
            th5 = request.POST['th5']
            f1 = request.POST['f1']
            f2 = request.POST['f2']
            f3 = request.POST['f3']
            f4 = request.POST['f4']
            f5 = request.POST['f5']
            sa1 = request.POST['sa1']
            sa2 = request.POST['sa2']
            sa3= request.POST['sa3']
            sa4 = request.POST['sa4']
            sa5 = request.POST['sa5']
            s1 = request.POST['s1']
            s2 = request.POST['s2']
            s3 = request.POST['s3']
            s4 = request.POST['s4']
            s5 = request.POST['s5']
        
            str = m1 + '_' + m2 + '_'+m3 + '_' + m4 + '_'+m5+'_e_'+t1 + '_' + t2 + '_'+t3 + '_' + t4 + '_'+t5+'_e_'+w1 + '_' + w2 + '_'+w3 + '_' + w4 + '_'+w5+'_e_'+th1 + '_' + th2 + '_'+th3 + '_' + th4 + '_'+th5+'_e_'+f1 + '_' + f2 + '_'+f3 + '_' + f4 + '_'+f5+'_e_'+sa1 + '_' + sa2 + '_'+sa3 + '_' + sa4 + '_'+sa5+'_e_'+s1 + '_' + s2 + '_'+s3 + '_' + s4 + '_'+s5
            return render(request,'fortrainers.html',{'str' : str})    
        else:
            return render(request,'fortrainers.html')  

    except(Exception):
        return render(request,'fortrainers.html')



def user_login(request):
    z:int
    greeting:str
    now = datetime.now()
    hour = now.hour

    if hour < 12:
        greeting = "Good morning !"
    elif hour < 18:
        greeting = "Good afternoon !"
    else:
        greeting = "Good night !"

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['pass2']
        li = Customer_Details.objects.filter(username=username,password=password1)
        if len(li) == 0:
            return render(request,'user_login.html',{'a' : 10})
        else:
            for i in li:
                z = i
            
            
            S=Subscription.objects.filter(customer_id=int(z.id))
            if len(S) != 0:
                request.session['sess']=int(z.id)
                Sa=Subscription.objects.get(customer_id=int(z.id))
                if str(now.date()) == str(Sa.end_date):
                    Sa.delete()
                    return render(request,'customer_page.html',{'z' : z,'gre':greeting})
                else:
                    return render(request,'customer_page.html',{'z' : z,'gre':greeting,'Su':Sa,'pa':Packages.objects.get(id=int(Sa.package_id))})
            else:
                            request.session['sess']=int(z.id)
                            return render(request,'customer_page.html',{'z' : z,'gre':greeting})

        
    else:
        return render(request,'user_login.html')
        

def aboutus(request):
    if 'sess' in request.session:
        x=Customer_Details.objects.get(id=request.session['sess'])
        return render(request,'aboutus.html',{'x':x})
    else:
        return render(request,'aboutus.html')

def edit_profile(request):
    if 'sess' in request.session:
        z = request.POST['editprofile']
        c = Customer_Details.objects.get(id=z)
        return render(request,'edit_profile.html',{'z' : c})
    else:
        return render(request,'home.html')
#def save_edit(request):



def save_edit(request):
    if 'sess' in request.session:
        greeting:str
        name = request.POST['customer_name']
        username = request.POST['username']
        number = request.POST['number']
        password = request.POST['pass1']
        gender = request.POST['gender']
        z = request.POST['edit']
        now = datetime.now()
        hour = now.hour
        if hour < 12:
                greeting = "Good morning !"
        elif hour < 18:
                greeting = "Good afternoon !"
        else:
                greeting = "Good night !"
        a = Customer_Details.objects.filter(username=username).count()
        c = Customer_Details.objects.get(id=z)
        if a == 0 or c.username == username:
            
            c.name = name
            c.username = username
            c.PhoneNumber = number
            c.password = password
            c.gender = gender
            c.save()
            if len(Subscription.objects.filter(customer_id=request.session['sess'])) == 0:
                return render(request,'customer_page.html',{ 'z' : c,'gre' : greeting})
            else:
                Sa=Subscription.objects.get(customer_id=request.session['sess'])
                return render(request,'customer_page.html',{ 'z' : Customer_Details.objects.get(id=int(z)),'gre' : greeting,'Su':Sa,'pa':Packages.objects.get(id=int(Sa.package_id))})

        else:
            
                return render(request,'edit_profile.html',{'username' : username, 'z' : c})
               
    else:
        return render(request,'home.html')

def undefine(request):
    if 'sess' in request.session:

        if request.method == "POST":
            z = request.POST['undefine']
            return render(request,"page_sub.html",{'z' : z})
        else:
            return render(request,'new.html')
    else:
        return render(request,'home.html')

def adddata(request):
    if 'sess' in request.session:
        payment:int
        greeting:str
        now = datetime.now()
        hour = now.hour
        if hour < 12:
                greeting = "Good morning !"
        elif hour < 18: 
                greeting = "Good afternoon !"
        else:
                greeting = "Good night !"
        z = request.POST['subc']
        package = request.POST['selct']
        date_package = int(request.POST['month'])   
        Enddate = datetime.now() + timedelta(days=date_package)
        y = Packages.objects.filter(package_type=package)
        S=Subscription.objects.filter(customer_id=request.session['sess'])
        if len(S) == 0 :
            x : Packages
            for i in y:
                x = i

            if date_package == 30:
                payment = int(x.cost)
            
            elif date_package == 180:
                z=Packages(x)
                payment = (int(x.cost) * 6)-int(((int(x.cost) * 6)* 20)/100)

            else:
                z=Packages(x)
                payment = (int(x.cost) * 12)-int(((int(x.cost) * 12)*30)/100)
            

            return render(request,'checkout.html',{'Enddate' : date_package , 'payment' : payment , 'x' : x,'v':z} )
        else:
            Sa=Subscription.objects.get(customer_id=request.session['sess'])
            return render(request,'customer_page.html',{'z': Customer_Details.objects.get(id=int(z)),'message' : ' ','gre' : greeting,'Su': Sa,'pa':Packages.objects.get(id=int(Sa.package_id))})
    else:
        return render(request,'home.html')

def showpackage(request):
    return render(request,'silver_package.html')

def checkout(request):
    if 'sess' in request.session:
        greeting:str
        if len(Subscription.objects.filter(customer_id=request.session['sess'])) == 0:
            w = ''
            name = request.POST['q7_name[first]']
            address = request.POST['q4_address4[addr_line1]']
            address2 = request.POST['q4_address4[addr_line2]']
            city = request.POST['q4_address4[city]']
            state = request.POST['q4_address4[state]']
            zipcode = request.POST['q4_address4[postal]']
            country = request.POST['q4_address4[country]']
            areacode = request.POST['q5_phoneNumber5[area]']
            phonenumber = request.POST['q5_phoneNumber5[phone]']
            email = request.POST['q6_email6']
            date_package = request.POST['Enddate']
            payment = request.POST['payment']
            v = request.POST['v']
            x = request.POST['x']
            Enddate = datetime.now() + timedelta(days=int(date_package))
            xa:int
            package= Packages.objects.filter(package_type=x)
            for i in package:
                xa=i
            '''
            print(payment)
            for i in range(0,len(payment)-1):
                w = w + payment[i]  
            param_dict = {
                    'MID':'Ilezrv50470136374083',
                    'ORDER_ID': str(x.id),
                    'TXN_AMOUNT': w,
                    'CUST_ID': v.username,
                    'INDUSTRY_TYPE_ID':'Retail',
                    'WEBSITE':'DIYtestingweb',
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL':'http://127.0.0.1:8000/GymWebapp/handlerequest/',
            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
            '''
            c = Subscription(end_date=Enddate.date(),payment=payment,customer=Customer_Details.objects.get(id=request.session['sess']),package=xa,pay_check=True)
            c.save()
            
            now = datetime.now()
            hour = now.hour
            if hour < 12:
                greeting = "Good morning !"
            elif hour < 18:
                greeting = "Good afternoon !"
            else:
                greeting = "Good night !"
            Sa=Subscription.objects.get(customer_id=request.session['sess'])
            return render(request,'customer_page.html',{'z': Customer_Details.objects.get(id=request.session['sess'] ), 'gre':greeting,'Su': Sa,'pa':Packages.objects.get(id=int(Sa.package_id))})
        else:
            now = datetime.now()
            hour = now.hour
            if hour < 12:
                greeting = "Good morning !"
            elif hour < 18:
                greeting = "Good afternoon !"
            else:
                greeting = "Good night !"
            Sa=Subscription.objects.get(customer_id=request.session['sess'])
            return render(request,'customer_page.html',{'z': Customer_Details.objects.get(id=request.session['sess'] ),'mess':' ', 'gre':greeting,'Su': Sa,'pa':Packages.objects.get(id=int(Sa.package_id))})

    else:
        return render(request,'home.html')    
'''
@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})
'''

def dietplan(request):
    if 'sess' in request.session:
        id=int(request.POST['dietplane'])
        x:Workoutplan
        try:
            for i in Workoutplan.objects.filter(Customer=id):
                x=i
            Mon,Tue,Wed,Thus,Fri,Sat,Sun=[],[],[],[],[],[],[]
            cols=x.Dietplan.split('_')
            Li=[Mon,Tue,Wed,Thus,Fri,Sat,Sun]
            
            xz=0
            for z in Li:
                for i in range(xz,len(cols)):
                    if cols[i]=='e':
                        xz=i+1
                        break
                    else:                        
                        z.append(cols[i])
            sul=['1','2','3','4','5']
            return render(request,'dietplan.html',{'Mon':Mon,'Tue':Tue,'Wed':Wed,'Thus':Thus,'Fri':Fri,'Sat':Sat,'Sun':Sun,'sul':sul})
        except(Exception):
            greeting:str
            now = datetime.now()
            hour = now.hour
            if hour < 12:
                greeting = "Good morning !"
            elif hour < 18:
                greeting = "Good afternoon !"
            else:
                greeting = "Good night !"
            if len(Subscription.objects.filter(customer_id=request.session['sess'])) == 0:
                return render(request,'customer_page.html',{'z': Customer_Details.objects.get(id=request.session['sess']),'mes' : ' ','gre' : greeting})
            else:
                Sa=Subscription.objects.get(customer_id=request.session['sess'])
                return render(request,'customer_page.html',{'z': Customer_Details.objects.get(id=request.session['sess']),'m' : ' ','gre' : greeting,'Su': Sa,'pa':Packages.objects.get(id=int(Sa.package_id))})
    else:
        return render(request,'home.html')    

def exerscise(request):
    if 'sess' in request.session:
        Mon,Tue,Wed,Thus,Fri,Sat,Sun,Sad=[],[],[],[],[],[],[],[]
        Li=[Mon,Tue,Wed,Thus,Fri,Sat,Sun]
        Days = ['Monday','Tuesday','Wednesday','Thusday','Friday','Saterday','Sunday']
        id=int(request.POST['exerscise'])
        x:Workoutplan
        for i in Workoutplan.objects.filter(Customer=id):
            x=i
        try:
            cols=x.Exercise.split('_')
            for i in range(len(cols)):
                if i==0:               
                    Sad.append(cols[i])
                else:
                    if cols[i-1] == 'e':
                        Sad.append(cols[i]) 
            x=0
            for z in Li:  
                
                for i in range(x,len(cols)):
                    if cols[i] not in Sad:
                        if cols[i]=='e':
                            x=i+1
                            break
                        else:                        
                            z.append(cols[i])
                        
            Days = ['Monday','Tuesday','Wednesday','Thusday','Friday','Saterday','Sunday']

            return render(request,'exerscise.html',{'x':x,'Sad':Sad,'Mon':Mon,'Tue':Tue,'Wed':Wed,'Thus':Thus,'Fri':Fri,'Sat':Sat,'Sun':Sun,'Days':Days,'Li':Li}) 
        except(Exception):
            greeting:str
            now = datetime.now()
            hour = now.hour
            if hour < 12:
                greeting = "Good morning !"
            elif hour < 18:
                greeting = "Good afternoon !"
            else:
                greeting = "Good night !"
            if len(Subscription.objects.filter(customer_id=request.session['sess'])) == 0:
                return render(request,'customer_page.html',{'z': Customer_Details.objects.get(id=request.session['sess']),'mes' : ' ','gre' : greeting})
            else:
                Sa=Subscription.objects.get(customer_id=request.session['sess'])
                return render(request,'customer_page.html',{'z': Customer_Details.objects.get(id=request.session['sess']),'me' : ' ','gre' : greeting,'Su': Sa,'pa':Packages.objects.get(id=int(Sa.package_id))})

        
    else:
        return render(request,'home.html')   




def exec(request):
    try:
        message = None

        if request.method=='POST':
            if 'remove' in request.POST:
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    return render(request,'exe.html',{ 't1' :t1 , 'o' : request.session['counter']})
                else:
                    if request.session['counter'] != 1:
                        if request.session['check'] == 0 :
                            request.session['counter'] = request.session['counter'] - 1
                            
                            request.session['cr'] =  1 
                            request.session['check'] = 1
                            if request.session['counter'] != 0:
                                z = request.session['y']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y'] = request.session['y1']
                        else:
                            request.session['cr'] =  0
                            request.session['counter'] = request.session['counter'] - 1
                            if request.session['counter'] != 0:
                                z = request.session['y']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y'] = request.session['y1']
                        if request.session['cr'] !=  1 and request.session['check'] == 1:
                            try:
                                y=request.session['y']
                                y.pop()
                                request.session['y'] = y
                            except(Exception):
                                pass
                        y=request.session['y']
                        return render(request,'exe.html',{ 't1' :t1 , 'y' : y , 'o' : request.session['counter']})
                    else:
                        request.session['counter'] = 0
                        request.session['y'] = []
                        return render(request,'exe.html',{ 't1' :t1  , 'o' : request.session['counter']})
            if 'add' in request.POST:
                y=[]
                t1=request.POST['t1']
                request.session['counter'] = request.session['counter'] + 1
                name = 'M'+str(request.session['counter'])
                name1 = 'M'+str(request.session['counter'] - 1)
                try:
                        if len(request.POST[name1]) == 0:
                            message = 'oh'
                            request.session['counter'] = request.session['counter'] - 1
                            y = request.session['y']
                            return render(request,'exe.html',{'y' : y , 't1' :t1 , 'name' : name1 , 'log' : message , 'o' : request.session['counter']})   
                except(Exception):
                        pass
                if request.session['counter'] > 1:                    
                    
                    if request.session['counter'] == 2:
                        if 'y' not in request.session:
                            request.session['y'] = []
                        try:
                            request.session['y'].append(request.POST[name1])

                        except(Exception):
                            pass
                        
                    elif  request.session['counter'] > 2:
                        z = request.session['y']
                        request.session['y1'] = []
                        for i in z:
                            request.session['y1'].append(request.POST[i])
                        request.session['y'] = request.session['y1']
                        try:
                    
                            request.session['y'].append(request.POST[name1])

                        except(Exception):
                           pass
        
                    y = request.session['y']
                try:
                    
                    y = request.session['y']
                except(Exception):
                    pass
                request.session['check'] = 0
                request.session['name'] = name
                return render(request,'exe.html',{'y' : y , 't1' :t1 , 'name' : name , 'o' : request.session['counter']})
            if 'OK' in request.POST:    
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    
                    try:
                        z=request.session['y']
                        request.session['y'] = []                        
                        request.session['y'].append(t1)
                        if len(z) != 0:
                            for i in z:
                                request.session['y'].append(i)
                    except:
                        request.session['y'] = []
                        request.session['y'].append(t1)
                    if 'y1' in request.session:
                         del request.session['yi']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0

                    return render(request,'exeT.html')
                    
                else:
                    try:
                        
                        z=request.session['y']
                        
                        if len(z) != 0:
                            request.session['y'] = []
                            request.session['y'].append(t1)
                            for i in z:
                                request.session['y'].append(i)
                            
                    except(Exception):
                        request.session['y'] = []
                        request.session['y'].append(t1)
                    try:  
                        if len(request.POST[request.session['name']]):
                            request.session['y'].append(request.POST[request.session['name']])
                    except:
                        pass
                    if 'y1' in request.session:
                         del request.session['yi']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
                    return render(request,'exeT.html')
        else:
            logout(request)
            request.session['counter'] = 0
            return render(request,'exe.html')   
    except(Exception):
       logout(request)
       request.session['counter'] = 0
       return render(request,'exe.html')


def axect(request):
    try:
        message = None
        if request.method=='POST':
            if 'remove' in request.POST:
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    return render(request,'exeT.html',{ 't1' :t1})
                else:
                    if request.session['counter'] != 1:
                        if request.session['check'] == 0 :
                            request.session['counter'] = request.session['counter'] - 1
                            
                            request.session['cr'] =  1 
                            request.session['check'] = 1
                            if request.session['counter'] != 0:
                                z = request.session['y2']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y2'] = request.session['y1']
                        else:
                            request.session['cr'] =  0
                            request.session['counter'] = request.session['counter'] - 1
                            if request.session['counter'] != 0:
                                z = request.session['y2']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y2'] = request.session['y1']
                        if request.session['cr'] !=  1 and request.session['check'] == 1:
                            try:
                                y=request.session['y2']
                                y.pop()
                                request.session['y2'] = y
                            except(Exception):
                                pass
                        y=request.session['y2']
                        return render(request,'exeT.html',{ 't1' :t1 , 'y2' : y })
                    else:
                        request.session['counter'] = 0
                        request.session['y2'] = []
                        return render(request,'exeT.html',{ 't1' :t1})
            if 'add' in request.POST:
                y=[]
                t1=request.POST['t1']
                request.session['counter'] = request.session['counter'] + 1
                name = 'M'+str(request.session['counter'])
                name1 = 'M'+str(request.session['counter'] - 1)
                try:
                        if len(request.POST[name1]) == 0:
                            message = 'oh'
                            request.session['counter'] = request.session['counter'] - 1
                            y = request.session['y2']
                            return render(request,'exeT.html',{'y2' : y , 't1' :t1 , 'name' : name1 , 'log' : message , 'o' : request.session['counter']})   
                except(Exception):
                        pass
                if request.session['counter'] > 1:                    
                    
                    if request.session['counter'] == 2:
                        if 'y2' not in request.session:
                            request.session['y2'] = []
                        try:
                            request.session['y2'].append(request.POST[name1])

                        except(Exception):
                            pass
                        
                    elif  request.session['counter'] > 2:
                        z = request.session['y2']
                        request.session['y1'] = []
                        for i in z:
                            request.session['y1'].append(request.POST[i])
                        request.session['y2'] = request.session['y1']
                        try:
                    
                            request.session['y2'].append(request.POST[name1])

                        except(Exception):
                           pass
        
                    y = request.session['y2']
                try:
                    
                    y = request.session['y2']
                except(Exception):
                    pass
                request.session['check'] = 0
                request.session['name'] = name
                return render(request,'exeT.html',{'y2' : y , 't1' :t1 , 'name' : name , 'o' : request.session['counter']})
            if 'OK' in request.POST:    
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    
                    try:
                        z=request.session['y2']
                        request.session['y2'] = []                        
                        request.session['y2'].append(t1)
                        if len(z) != 0:
                            for i in z:
                                request.session['y2'].append(i)
                    except:
                        request.session['y2'] = []
                        request.session['y2'].append(t1)
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
                    return render(request,'exeW.html')
                    
                else:
                    try:
                        
                        z=request.session['y2']
                        
                        if len(z) != 0:
                            request.session['y2'] = []
                            request.session['y2'].append(t1)
                            for i in z:
                                request.session['y2'].append(i)
                            
                    except(Exception):
                        request.session['y2'] = []
                        request.session['y2'].append(t1)
                    try:  
                        if len(request.POST[request.session['name']]):
                            request.session['y2'].append(request.POST[request.session['name']])
                    except:
                        pass
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
        
                    return render(request,'exeW.html')
        else:
            logout(request)
            request.session['counter'] = 0
            return render(request,'exe.html')

    except(Exception):
        if 'y1' in request.session:
                del request.session['y1']
        if 'cr' in request.session:
                del request.session['cr']
        if 'check' in request.session:
                del request.session['check']
        if 'name' in request.session:
                del request.session['name']
        if 'y2' in request.session:
            del request.session['y2']
        request.session['counter'] = 0
        return render(request,'exeT.html')   

def wed(request):
    try:
        message = None
        if request.method=='POST':
            if 'remove' in request.POST:
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    return render(request,'exeW.html',{ 't1' :t1})
                else:
                    if request.session['counter'] != 1:
                        if request.session['check'] == 0 :
                            request.session['counter'] = request.session['counter'] - 1
                            
                            request.session['cr'] =  1 
                            request.session['check'] = 1
                            if request.session['counter'] != 0:
                                z = request.session['y3']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y3'] = request.session['y1']
                        else:
                            request.session['cr'] =  0
                            request.session['counter'] = request.session['counter'] - 1
                            if request.session['counter'] != 0:
                                z = request.session['y3']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y3'] = request.session['y1']
                        if request.session['cr'] !=  1 and request.session['check'] == 1:
                            try:
                                y=request.session['y3']
                                y.pop()
                                request.session['y3'] = y
                            except(Exception):
                                pass
                        y=request.session['y3']
                        return render(request,'exeW.html',{ 't1' :t1 , 'y3' : y })
                    else:
                        request.session['counter'] = 0
                        request.session['y3'] = []
                        return render(request,'exeW.html',{ 't1' :t1})
            if 'add' in request.POST:
                y=[]
                t1=request.POST['t1']
                request.session['counter'] = request.session['counter'] + 1
                name = 'M'+str(request.session['counter'])
                name1 = 'M'+str(request.session['counter'] - 1)
                try:
                        if len(request.POST[name1]) == 0:
                            message = 'oh'
                            request.session['counter'] = request.session['counter'] - 1
                            y = request.session['y3']
                            return render(request,'exeW.html',{'y3' : y , 't1' :t1 , 'name' : name1 , 'log' : message , 'o' : request.session['counter']})   
                except(Exception):
                        pass
                if request.session['counter'] > 1:                    
                    
                    if request.session['counter'] == 2:
                        if 'y3' not in request.session:
                            request.session['y3'] = []
                        try:
                            request.session['y3'].append(request.POST[name1])

                        except(Exception):
                            pass
                        
                    elif  request.session['counter'] > 2:
                        z = request.session['y3']
                        request.session['y1'] = []
                        for i in z:
                            request.session['y1'].append(request.POST[i])
                        request.session['y3'] = request.session['y1']
                        try:
                    
                            request.session['y3'].append(request.POST[name1])

                        except(Exception):
                           pass
        
                    y = request.session['y3']
                try:
                    
                    y = request.session['y3']
                except(Exception):
                    pass
                request.session['check'] = 0
                request.session['name'] = name
                return render(request,'exeW.html',{'y3' : y , 't1' :t1 , 'name' : name , 'o' : request.session['counter']})
            if 'OK' in request.POST:    
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    
                    try:
                        z=request.session['y3']
                        request.session['y3'] = []                        
                        request.session['y3'].append(t1)
                        if len(z) != 0:
                            for i in z:
                                request.session['y3'].append(i)
                    except:
                        request.session['y3'] = []
                        request.session['y3'].append(t1)
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
                    return render(request,'exeW.html')
                    
                else:
                    try:
                        
                        z=request.session['y3']
                        
                        if len(z) != 0:
                            request.session['y3'] = []
                            request.session['y3'].append(t1)
                            for i in z:
                                request.session['y3'].append(i)
                            
                    except(Exception):
                        request.session['y3'] = []
                        request.session['y3'].append(t1)
                    try:  
                        if len(request.POST[request.session['name']]):
                            request.session['y3'].append(request.POST[request.session['name']])
                    except:
                        pass
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
        
                    return render(request,'exeW.html')
        else:
            logout(request)
            request.session['counter'] = 0
            return render(request,'exe.html')

    except(Exception):
        if 'y1' in request.session:
                del request.session['y1']
        if 'cr' in request.session:
                del request.session['cr']
        if 'check' in request.session:
                del request.session['check']
        if 'name' in request.session:
                del request.session['name']
        if 'y3' in request.session:
            del request.session['y3']
        request.session['counter'] = 0
        return render(request,'exeW.html')   

def wed(request):
    try:
        message = None
        if request.method=='POST':
            if 'remove' in request.POST:
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    return render(request,'exeW.html',{ 't1' :t1})
                else:
                    if request.session['counter'] != 1:
                        if request.session['check'] == 0 :
                            request.session['counter'] = request.session['counter'] - 1
                            
                            request.session['cr'] =  1 
                            request.session['check'] = 1
                            if request.session['counter'] != 0:
                                z = request.session['y3']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y3'] = request.session['y1']
                        else:
                            request.session['cr'] =  0
                            request.session['counter'] = request.session['counter'] - 1
                            if request.session['counter'] != 0:
                                z = request.session['y3']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y3'] = request.session['y1']
                        if request.session['cr'] !=  1 and request.session['check'] == 1:
                            try:
                                y=request.session['y3']
                                y.pop()
                                request.session['y3'] = y
                            except(Exception):
                                pass
                        y=request.session['y3']
                        return render(request,'exeW.html',{ 't1' :t1 , 'y3' : y })
                    else:
                        request.session['counter'] = 0
                        request.session['y3'] = []
                        return render(request,'exeW.html',{ 't1' :t1})
            if 'add' in request.POST:
                y=[]
                t1=request.POST['t1']
                request.session['counter'] = request.session['counter'] + 1
                name = 'M'+str(request.session['counter'])
                name1 = 'M'+str(request.session['counter'] - 1)
                try:
                        if len(request.POST[name1]) == 0:
                            message = 'oh'
                            request.session['counter'] = request.session['counter'] - 1
                            y = request.session['y3']
                            return render(request,'exeW.html',{'y3' : y , 't1' :t1 , 'name' : name1 , 'log' : message , 'o' : request.session['counter']})   
                except(Exception):
                        pass
                if request.session['counter'] > 1:                    
                    
                    if request.session['counter'] == 2:
                        if 'y3' not in request.session:
                            request.session['y3'] = []
                        try:
                            request.session['y3'].append(request.POST[name1])

                        except(Exception):
                            pass
                        
                    elif  request.session['counter'] > 2:
                        z = request.session['y3']
                        request.session['y1'] = []
                        for i in z:
                            request.session['y1'].append(request.POST[i])
                        request.session['y3'] = request.session['y1']
                        try:
                    
                            request.session['y3'].append(request.POST[name1])

                        except(Exception):
                           pass
        
                    y = request.session['y3']
                try:
                    
                    y = request.session['y3']
                except(Exception):
                    pass
                request.session['check'] = 0
                request.session['name'] = name
                return render(request,'exeW.html',{'y3' : y , 't1' :t1 , 'name' : name , 'o' : request.session['counter']})
            if 'OK' in request.POST:    
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    
                    try:
                        z=request.session['y3']
                        request.session['y3'] = []                        
                        request.session['y3'].append(t1)
                        if len(z) != 0:
                            for i in z:
                                request.session['y3'].append(i)
                    except:
                        request.session['y3'] = []
                        request.session['y3'].append(t1)
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
                    return render(request,'exeTu.html')
                    
                else:
                    try:
                        
                        z=request.session['y3']
                        
                        if len(z) != 0:
                            request.session['y3'] = []
                            request.session['y3'].append(t1)
                            for i in z:
                                request.session['y3'].append(i)
                            
                    except(Exception):
                        request.session['y3'] = []
                        request.session['y3'].append(t1)
                    try:  
                        if len(request.POST[request.session['name']]):
                            request.session['y3'].append(request.POST[request.session['name']])
                    except:
                        pass
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
        
                    return render(request,'exeTu.html')
        else:
            logout(request)
            request.session['counter'] = 0
            return render(request,'exe.html')

    except(Exception):
        if 'y1' in request.session:
                del request.session['y1']
        if 'cr' in request.session:
                del request.session['cr']
        if 'check' in request.session:
                del request.session['check']
        if 'name' in request.session:
                del request.session['name']
        if 'y3' in request.session:
            del request.session['y3']
        request.session['counter'] = 0
        return render(request,'exeW.html')


def thus(request):
    try:
        message = None
        if request.method=='POST':
            if 'remove' in request.POST:
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    return render(request,'exeTu.html',{ 't1' :t1})
                else:
                    if request.session['counter'] != 1:
                        if request.session['check'] == 0 :
                            request.session['counter'] = request.session['counter'] - 1
                            
                            request.session['cr'] =  1 
                            request.session['check'] = 1
                            if request.session['counter'] != 0:
                                z = request.session['y4']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y4'] = request.session['y1']
                        else:
                            request.session['cr'] =  0
                            request.session['counter'] = request.session['counter'] - 1
                            if request.session['counter'] != 0:
                                z = request.session['y4']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y4'] = request.session['y1']
                        if request.session['cr'] !=  1 and request.session['check'] == 1:
                            try:
                                y=request.session['y4']
                                y.pop()
                                request.session['y4'] = y
                            except(Exception):
                                pass
                        y=request.session['y4']
                        return render(request,'exeTu.html',{ 't1' :t1 , 'y4' : y })
                    else:
                        request.session['counter'] = 0
                        request.session['y4'] = []
                        return render(request,'exeTu.html',{ 't1' :t1})
            if 'add' in request.POST:
                y=[]
                t1=request.POST['t1']
                request.session['counter'] = request.session['counter'] + 1
                name = 'M'+str(request.session['counter'])
                name1 = 'M'+str(request.session['counter'] - 1)
                try:
                        if len(request.POST[name1]) == 0:
                            message = 'oh'
                            request.session['counter'] = request.session['counter'] - 1
                            y = request.session['y4']
                            return render(request,'exeTu.html',{'y4' : y , 't1' :t1 , 'name' : name1 , 'log' : message , 'o' : request.session['counter']})   
                except(Exception):
                        pass
                if request.session['counter'] > 1:                    
                    
                    if request.session['counter'] == 2:
                        if 'y4' not in request.session:
                            request.session['y4'] = []
                        try:
                            request.session['y4'].append(request.POST[name1])

                        except(Exception):
                            pass
                        
                    elif  request.session['counter'] > 2:
                        z = request.session['y4']
                        request.session['y1'] = []
                        for i in z:
                            request.session['y1'].append(request.POST[i])
                        request.session['y4'] = request.session['y1']
                        try:
                    
                            request.session['y4'].append(request.POST[name1])

                        except(Exception):
                           pass
        
                    y = request.session['y4']
                try:
                    
                    y = request.session['y4']
                except(Exception):
                    pass
                request.session['check'] = 0
                request.session['name'] = name
                return render(request,'exeTu.html',{'y4' : y , 't1' :t1 , 'name' : name , 'o' : request.session['counter']})
            if 'OK' in request.POST:    
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    
                    try:
                        z=request.session['y4']
                        request.session['y4'] = []                        
                        request.session['y4'].append(t1)
                        if len(z) != 0:
                            for i in z:
                                request.session['y4'].append(i)
                    except:
                        request.session['y4'] = []
                        request.session['y4'].append(t1)
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
                    return render(request,'exeF.html')
                    
                else:
                    try:
                        
                        z=request.session['y4']
                        
                        if len(z) != 0:
                            request.session['y4'] = []
                            request.session['y4'].append(t1)
                            for i in z:
                                request.session['y4'].append(i)
                            
                    except(Exception):
                        request.session['y4'] = []
                        request.session['y4'].append(t1)
                    try:  
                        if len(request.POST[request.session['name']]):
                            request.session['y4'].append(request.POST[request.session['name']])
                    except:
                        pass
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
        
                    return render(request,'exeF.html')
        else:
            logout(request)
            request.session['counter'] = 0
            return render(request,'exe.html')

    except(Exception):
        if 'y1' in request.session:
                del request.session['y1']
        if 'cr' in request.session:
                del request.session['cr']
        if 'check' in request.session:
                del request.session['check']
        if 'name' in request.session:
                del request.session['name']
        if 'y4' in request.session:
            del request.session['y4']
        request.session['counter'] = 0
        return render(request,'exeTu.html')

def fri(request):
    try:
        message = None
        if request.method=='POST':
            if 'remove' in request.POST:
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    return render(request,'exeF.html',{ 't1' :t1})
                else:
                    if request.session['counter'] != 1:
                        if request.session['check'] == 0 :
                            request.session['counter'] = request.session['counter'] - 1
                            
                            request.session['cr'] =  1 
                            request.session['check'] = 1
                            if request.session['counter'] != 0:
                                z = request.session['y5']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y5'] = request.session['y1']
                        else:
                            request.session['cr'] =  0
                            request.session['counter'] = request.session['counter'] - 1
                            if request.session['counter'] != 0:
                                z = request.session['y5']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y5'] = request.session['y1']
                        if request.session['cr'] !=  1 and request.session['check'] == 1:
                            try:
                                y=request.session['y5']
                                y.pop()
                                request.session['y5'] = y
                            except(Exception):
                                pass
                        y=request.session['y5']
                        return render(request,'exeF.html',{ 't1' :t1 , 'y5' : y })
                    else:
                        request.session['counter'] = 0
                        request.session['y5'] = []
                        return render(request,'exeF.html',{ 't1' :t1})
            if 'add' in request.POST:
                y=[]
                t1=request.POST['t1']
                request.session['counter'] = request.session['counter'] + 1
                name = 'M'+str(request.session['counter'])
                name1 = 'M'+str(request.session['counter'] - 1)
                try:
                        if len(request.POST[name1]) == 0:
                            message = 'oh'
                            request.session['counter'] = request.session['counter'] - 1
                            y = request.session['y5']
                            return render(request,'exeF.html',{'y5' : y , 't1' :t1 , 'name' : name1 , 'log' : message , 'o' : request.session['counter']})   
                except(Exception):
                        pass
                if request.session['counter'] > 1:                    
                    
                    if request.session['counter'] == 2:
                        if 'y5' not in request.session:
                            request.session['y5'] = []
                        try:
                            request.session['y5'].append(request.POST[name1])

                        except(Exception):
                            pass
                        
                    elif  request.session['counter'] > 2:
                        z = request.session['y5']
                        request.session['y1'] = []
                        for i in z:
                            request.session['y1'].append(request.POST[i])
                        request.session['y5'] = request.session['y1']
                        try:
                    
                            request.session['y5'].append(request.POST[name1])

                        except(Exception):
                           pass
        
                    y = request.session['y5']
                try:
                    
                    y = request.session['y5']
                except(Exception):
                    pass
                request.session['check'] = 0
                request.session['name'] = name
                return render(request,'exeF.html',{'y5' : y , 't1' :t1 , 'name' : name , 'o' : request.session['counter']})
            if 'OK' in request.POST:    
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    
                    try:
                        z=request.session['y5']
                        request.session['y5'] = []                        
                        request.session['y5'].append(t1)
                        if len(z) != 0:
                            for i in z:
                                request.session['y5'].append(i)
                    except:
                        request.session['y5'] = []
                        request.session['y5'].append(t1)
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
                    return render(request,'exeS.html')
                    
                else:
                    try:
                        
                        z=request.session['y5']
                        
                        if len(z) != 0:
                            request.session['y5'] = []
                            request.session['y5'].append(t1)
                            for i in z:
                                request.session['y5'].append(i)
                            
                    except(Exception):
                        request.session['y5'] = []
                        request.session['y5'].append(t1)
                    try:  
                        if len(request.POST[request.session['name']]):
                            request.session['y5'].append(request.POST[request.session['name']])
                    except:
                        pass
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
        
                    return render(request,'exeS.html')
        else:
            logout(request)
            request.session['counter'] = 0
            return render(request,'exe.html')

    except(Exception):
        if 'y1' in request.session:
                del request.session['y1']
        if 'cr' in request.session:
                del request.session['cr']
        if 'check' in request.session:
                del request.session['check']
        if 'name' in request.session:
                del request.session['name']
        if 'y5' in request.session:
            del request.session['y5']
        request.session['counter'] = 0
        return render(request,'exeF.html')

def sat(request):
    try:
        message = None
        if request.method=='POST':
            if 'remove' in request.POST:
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    return render(request,'exeS.html',{ 't1' :t1})
                else:
                    if request.session['counter'] != 1:
                        if request.session['check'] == 0 :
                            request.session['counter'] = request.session['counter'] - 1
                            
                            request.session['cr'] =  1 
                            request.session['check'] = 1
                            if request.session['counter'] != 0:
                                z = request.session['y6']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y6'] = request.session['y1']
                        else:
                            request.session['cr'] =  0
                            request.session['counter'] = request.session['counter'] - 1
                            if request.session['counter'] != 0:
                                z = request.session['y6']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y6'] = request.session['y1']
                        if request.session['cr'] !=  1 and request.session['check'] == 1:
                            try:
                                y=request.session['y6']
                                y.pop()
                                request.session['y6'] = y
                            except(Exception):
                                pass
                        y=request.session['y6']
                        return render(request,'exeS.html',{ 't1' :t1 , 'y6' : y })
                    else:
                        request.session['counter'] = 0
                        request.session['y6'] = []
                        return render(request,'exeS.html',{ 't1' :t1})
            if 'add' in request.POST:
                y=[]
                t1=request.POST['t1']
                request.session['counter'] = request.session['counter'] + 1
                name = 'M'+str(request.session['counter'])
                name1 = 'M'+str(request.session['counter'] - 1)
                try:
                        if len(request.POST[name1]) == 0:
                            message = 'oh'
                            request.session['counter'] = request.session['counter'] - 1
                            y = request.session['y6']
                            return render(request,'exeS.html',{'y6' : y , 't1' :t1 , 'name' : name1 , 'log' : message , 'o' : request.session['counter']})   
                except(Exception):
                        pass
                if request.session['counter'] > 1:                    
                    
                    if request.session['counter'] == 2:
                        if 'y6' not in request.session:
                            request.session['y6'] = []
                        try:
                            request.session['y6'].append(request.POST[name1])

                        except(Exception):
                            pass
                        
                    elif  request.session['counter'] > 2:
                        z = request.session['y6']
                        request.session['y1'] = []
                        for i in z:
                            request.session['y1'].append(request.POST[i])
                        request.session['y6'] = request.session['y1']
                        try:
                    
                            request.session['y6'].append(request.POST[name1])

                        except(Exception):
                           pass
        
                    y = request.session['y6']
                try:
                    
                    y = request.session['y6']
                except(Exception):
                    pass
                request.session['check'] = 0
                request.session['name'] = name
                return render(request,'exeS.html',{'y6' : y , 't1' :t1 , 'name' : name , 'o' : request.session['counter']})
            if 'OK' in request.POST:    
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    
                    try:
                        z=request.session['y6']
                        request.session['y6'] = []                        
                        request.session['y6'].append(t1)
                        if len(z) != 0:
                            for i in z:
                                request.session['y6'].append(i)
                    except:
                        request.session['y6'] = []
                        request.session['y6'].append(t1)
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
                    return render(request,'exeSu.html')
                    
                else:
                    try:
                        
                        z=request.session['y6']
                        
                        if len(z) != 0:
                            request.session['y6'] = []
                            request.session['y6'].append(t1)
                            for i in z:
                                request.session['y6'].append(i)
                            
                    except(Exception):
                        request.session['y6'] = []
                        request.session['y6'].append(t1)
                    try:  
                        if len(request.POST[request.session['name']]):
                            request.session['y6'].append(request.POST[request.session['name']])
                    except:
                        pass
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
        
                    return render(request,'exeSu.html')
        else:
            logout(request)
            request.session['counter'] = 0
            return render(request,'exe.html')

    except(Exception):
        if 'y1' in request.session:
                del request.session['y1']
        if 'cr' in request.session:
                del request.session['cr']
        if 'check' in request.session:
                del request.session['check']
        if 'name' in request.session:
                del request.session['name']
        if 'y6' in request.session:
            del request.session['y6']
        request.session['counter'] = 0
        return render(request,'exeS.html')

def aug(request):
    y = request.session['y']
    y1 =request.session['y2']
    y2 =request.session['y3']
    y3 =request.session['y4']
    y4 =request.session['y5']
    y5 =request.session['y6']
    y6 =request.session['y7']
    flag = 0
    count = 1
    st = ''
    gro = ''
    for i in [y,y1,y2,y3,y4,y5,y6]:
        flag = 1
        for j in i:
            if flag == 1:
                st = st +  str(j)
                flag = 0
            else:
                st = st + '_' + str(j)
        else:
            st = st + '_e_'
    
    count = 0

    for i in st:
        if count == len(st) - 3:
            break
        else:
                gro = gro + i
                count += 1
    return gro

def sun(request):
    try:
        message = None
        if request.method=='POST':
            if 'remove' in request.POST:
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    return render(request,'exeSu.html',{ 't1' :t1})
                else:
                    if request.session['counter'] != 1:
                        if request.session['check'] == 0 :
                            request.session['counter'] = request.session['counter'] - 1
                            
                            request.session['cr'] =  1 
                            request.session['check'] = 1
                            if request.session['counter'] != 0:
                                z = request.session['y7']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y7'] = request.session['y1']
                        else:
                            request.session['cr'] =  0
                            request.session['counter'] = request.session['counter'] - 1
                            if request.session['counter'] != 0:
                                z = request.session['y7']
                                request.session['y1'] = []
                                for i in z:
                                    request.session['y1'].append(request.POST[i])
                                request.session['y7'] = request.session['y1']
                        if request.session['cr'] !=  1 and request.session['check'] == 1:
                            try:
                                y=request.session['y7']
                                y.pop()
                                request.session['y7'] = y
                            except(Exception):
                                pass
                        y=request.session['y7']
                        return render(request,'exeSu.html',{ 't1' :t1 , 'y7' : y })
                    else:
                        request.session['counter'] = 0
                        request.session['y7'] = []
                        return render(request,'exeSu.html',{ 't1' :t1})
            if 'add' in request.POST:
                y=[]
                t1=request.POST['t1']
                request.session['counter'] = request.session['counter'] + 1
                name = 'M'+str(request.session['counter'])
                name1 = 'M'+str(request.session['counter'] - 1)
                try:
                        if len(request.POST[name1]) == 0:
                            message = 'oh'
                            request.session['counter'] = request.session['counter'] - 1
                            y = request.session['y7']
                            return render(request,'exeSu.html',{'y7' : y , 't1' :t1 , 'name' : name1 , 'log' : message , 'o' : request.session['counter']})   
                except(Exception):
                        pass
                if request.session['counter'] > 1:                    
                    
                    if request.session['counter'] == 2:
                        if 'y7' not in request.session:
                            request.session['y7'] = []
                        try:
                            request.session['y7'].append(request.POST[name1])

                        except(Exception):
                            pass
                        
                    elif  request.session['counter'] > 2:
                        z = request.session['y7']
                        request.session['y1'] = []
                        for i in z:
                            request.session['y1'].append(request.POST[i])
                        request.session['y7'] = request.session['y1']
                        try:
                    
                            request.session['y7'].append(request.POST[name1])

                        except(Exception):
                           pass
        
                    y = request.session['y7']
                try:
                    
                    y = request.session['y7']
                except(Exception):
                    pass
                request.session['check'] = 0
                request.session['name'] = name
                return render(request,'exeSu.html',{'y7' : y , 't1' :t1 , 'name' : name , 'o' : request.session['counter']})
            if 'OK' in request.POST:    
                t1=request.POST['t1']
                if request.session['counter'] == 0:
                    
                    try:
                        z=request.session['y7']
                        request.session['y7'] = []                        
                        request.session['y7'].append(t1)
                        if len(z) != 0:
                            for i in z:
                                request.session['y7'].append(i)
                    except:
                        request.session['y7'] = []
                        request.session['y7'].append(t1)
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
                    return render(request,'fp.html' ,{ 'sr' : aug(request) })
                    
                else:
                    try:
                        
                        z=request.session['y7']
                        
                        if len(z) != 0:
                            request.session['y7'] = []
                            request.session['y7'].append(t1)
                            for i in z:
                                request.session['y7'].append(i)
                            
                    except(Exception):
                        request.session['y7'] = []
                        request.session['y7'].append(t1)
                    try:  
                        if len(request.POST[request.session['name']]):
                            request.session['y7'].append(request.POST[request.session['name']])
                    except:
                        pass
                    if 'y1' in request.session:
                         del request.session['y1']
                    if 'cr' in request.session:
                         del request.session['cr']
                    if 'check' in request.session:
                         del request.session['check']
                    if 'name' in request.session:
                        del request.session['name']
                    request.session['counter'] = 0
                    return render(request,'fp.html',{ 'sr' : aug(request) })
        else:
            logout(request)
            request.session['counter'] = 0
            return render(request,'exe.html')

    except(Exception):
        if 'y1' in request.session:
                del request.session['y1']
        if 'cr' in request.session:
                del request.session['cr']
        if 'check' in request.session:
                del request.session['check']
        if 'name' in request.session:
                del request.session['name']
        if 'y7' in request.session:
            del request.session['y7']
        request.session['counter'] = 0
        return render(request,'exeSu.html')



