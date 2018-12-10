from django.shortcuts import render,HttpResponse,redirect
import random
from django.views import View
from app1 import models
# Create your views here.
#生成验证码
def give_val():
    from utils import val
    val=val.gene_code('/computer_game/static','test').upper() #会把生成的图片存成/static/test.png
    return val
#调用验证码
def show_val():
    global val
    val=give_val()
    return val
def index(request):
    return render(request,'index.html')
class login(View):
    def dispatch(self, request, *args, **kwargs):
        result=super(login,self).dispatch(request, *args, **kwargs)
        show_val()
        print(val)
        return result
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        get_tel=request.POST.get('tel',None)
        get_pwd=request.POST.get('password',None)
        get_val=request.POST.get('val',None).upper()
        if get_val==val:
            if models.user_info.objects.filter(tel=get_tel):
                pwd=models.user_info.objects.filter(tel=get_tel).values('password').first()['password']
                if pwd==get_pwd:
                    request.session['tel']=get_tel
                    request.session['is_login']=True
                    return redirect('/home/')
                else:
                    return render(request,'login.html',{'pwd_error':'密码错误'})
            else:
                return render(request,'login.html',{'tel_error':'用户未被注册'})
        else:
            return render(request,'login.html',{'error':'验证码错误！'})
class register(View):
    def dispatch(self, request, *args, **kwargs):
        result=super(register, self).dispatch(request, *args, **kwargs)
        show_val()
        print(val)
        return result
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        get_user=request.POST.get('username',None)
        get_pwd=request.POST.get('password',None)
        # get_repwd=request.POST.get('repassword',None)
        get_tel=request.POST.get('tel',None)
        get_val=request.POST.get('val',None).upper()
        print(get_val,val)
        if get_val==val:
            have_tel=models.user_info.objects.filter(tel=get_tel).first()
            if have_tel:
                return render(request,'register.html',{'user_error':"该电话已注册"})
            else:
                models.user_info.objects.create(
                    username=get_user,
                    password=get_pwd,
                    tel=get_tel
                )
                return redirect('/login/')
        else:
            return render(request, 'register.html', {'error': '验证码错误！'})

def home(request):
    return redirect('/yuyuepaidui/')
def yuyuepaidui(request):
    if request.session.get('is_login',None):
        tel=request.session.get('tel',None)
        return render(request,'yuyuepaidui.html',{'tel':tel})
    else:
        return redirect('/login/')
def k1(request):
    data=models.department_info.objects.values('dname','did').all()
    return render(request,'kl.html',{'data':data})
def doctor(request,uid):
    request.session['id']=uid
    data=models.doctor_info.objects.filter(r_id=uid).all()
    return render(request,'doctor.html',{'data':data})
def center(request):
    if request.session.get('is_login',None):
        tel=request.session.get('tel',None)
        return render(request,'center.html',{'tel':tel})
    else:
        return redirect('/login/')
def info(request):
    return render(request,'info.html')
def time(request,uid):
    import datetime
    id=request.session.get('id',None)
    request.session['doc_id']=uid
    now_time =datetime.datetime.now()
    f_time = now_time + datetime.timedelta(days=+1)
    day=now_time.strftime('%a')
    date=now_time.strftime('%m-%d')
    f2_time_md = f_time.strftime('%m-%d')
    f3_time = now_time + datetime.timedelta(days=+2)
    f3_time_md=f3_time.strftime('%m-%d')
    f4_time = now_time + datetime.timedelta(days=+3)
    f4_time_md = f4_time.strftime('%m-%d')
    f5_time = now_time + datetime.timedelta(days=+4)
    f5_time_md = f5_time.strftime('%m-%d')
    f6_time = now_time + datetime.timedelta(days=+5)
    f6_time_md = f6_time.strftime('%m-%d')
    f7_time = now_time + datetime.timedelta(days=+6)
    f7_time_md = f7_time.strftime('%m-%d')
    day2 = f_time.strftime('%a')
    day3 = f3_time.strftime('%a')
    day4 = f4_time.strftime('%a')
    day5 = f5_time.strftime('%a')
    day6 = f6_time.strftime('%a')
    day7 = f7_time.strftime('%a')
    return render(request,'time.html',{
        'id':id,
        'date1':date,
        'day':day,
        'day2':day2,
        'day3':day3,
        'day4':day4,
        'day5':day5,
        'day6':day6,
        'day7':day7,
        'date2':f2_time_md,
        'date3':f3_time_md,
        'date4':f4_time_md,
        'date5':f5_time_md,
        'date6':f6_time_md,
        'date7':f7_time_md,
    })
def wodepaihao(request):
    if request.session.get('doc_id',None):
        id=request.session.get('doc_id',None)
        data=models.ap_success.objects.filter(user_id=id).first()
        f_times=models.ap_success.objects.filter(user_id=id).values('num').first()['num']
        times=int(f_times)*4
        keshi_id=request.session['id']
        keshi_name=models.department_info.objects.filter(did=keshi_id).first()
        doc_id=request.session['doc_id']
        doc_name=models.doctor_info.objects.filter(id=doc_id).first()
        return render(request,'wodepaihao.html',
                      {'data':data,
                       'time':times,
                       'name':keshi_name,
                       'doc_name':doc_name
                       })
    else:
        return render(request,'erro.html')
def footer(request):
    return render(request,'footer.html')
def login_out(request):
    request.session.clear()
    return redirect('/')




