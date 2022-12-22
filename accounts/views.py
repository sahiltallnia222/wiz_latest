from django.shortcuts import render,redirect
from .form import RegisterUserForm
from .models import User
from django.contrib import auth,messages
from .utils import send_verification_email,send_password_reset_email
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
def register_user(request):
    try:
        if request.user.is_authenticated:
            messages.warning(request,'You are already logged in.')
            return redirect('home')
        elif request.method=='POST':
            form=RegisterUserForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                user=User.objects.create_user(username,email,password)
                send_verification_email(request,user,'Click on the link to confirm your registration')
                messages.success(request, 'Your account has been registered sucessfully. Check mail for account activation.')
                return redirect('accounts:login')
            else:
                messages.error(request,'Something went wrong !')
        else:
            form=RegisterUserForm()
        context={
            'form':form
        }
        return render(request,'accounts/register.html',context)
    except:
        messages.error(request,'Something went wrong. Please try again.')
        return render(request,'accounts/register.html',context)

def login_user(request):
    try:
        if request.user.is_authenticated:
            messages.warning(request,'You are already logged in.')
            return redirect('home')
        elif(request.method=='POST'):
            email=request.POST['email']
            password=request.POST['password']
            user=auth.authenticate(email=email,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,'You are logged in successfully.')
                return redirect('home')
            else:
                messages.error(request,'Invalid Credentials.')
                return redirect('accounts:login')
        return render(request,'accounts/login.html')
    except:
        messages.error(request,'Something went wrong.')
        return render(request,'accounts/login.html')

def logout_user(request):
   try:
        if not request.user.is_authenticated:
            messages.warning(request,'You are already logged out.')
            return redirect('home')
        auth.logout(request)
        messages.success(request,'You are logged out successfully.')
        return redirect('accounts:login')
   except:
        messages.success(request,'Something went wrong.')
        return redirect('accounts:login')


def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,'Congratulation Your account is activated.')
        return redirect('home')
    else:
        messages.error(request,'Invalid Activation link')
        return redirect('home')


def forgot_password(request):
    if request.method=='POST':
        try:
            email=request.POST['email']
            if User.objects.filter(email=email).exists():
                user=User.objects.get(email__exact=email)
                send_password_reset_email(request,user)
                messages.success(request,'Password reset link has been sent to your email account')
                return render(request,'accounts/forgot_redirect.html')
            else:
                messages.error(request,'Account does not exists')
                return redirect('accounts:forgot_password')
        except:
            messages.error(request,'Account does not exists')
            return redirect('accounts:forgot_password')
        
            
        
    else:
        return render(request,'accounts/forgot_password.html')
    


def reset_password(request):
    
    try:
        if request.method=='POST':
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            if password==confirm_password:
                pk=request.session.get('uid')
                user=User.objects.get(pk=pk)
                user.set_password(password)
                user.is_active=True
                user.save()
                messages.success(request,'Password reset successfully')
                return redirect('accounts:login')
            else:
                messages.error(request,'Password does not match')
                return render(request,'accounts/reset_password.html')
        else:
            return render(request,'accounts/reset_password.html')
    except:
        messages.error(request,'Something went wrong.')
        return render(request,'accounts/reset_password.html')

def reset_password_validate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid']=uid
        messages.info(request,'Please reset your password')
        return redirect('accounts:reset_password')
    else:
        messages.error(request,'This link has been expired.')
        return redirect('accounts:login')


def deactivate_account(request):
    try:
        if not request.user.is_authenticated:
            messages.error(request,'Please log in to deactivate your account.')
            return redirect('home')
        if(request.method=='POST'):
            try:
                email=request.POST['email']
                user=request.user
                if(email==user.email):
                    user.is_active=False
                    user.save()
                    messages.success(request,'Your account deactivated.')
                    return redirect('/')
                else:
                    messages.error(request,'Enter the valid email address.')
                    return render(request,'accounts/deactivate_account.html')
            except:
                messages.error(request,'Something went wrong.')
                return render(request,'accounts/deactivate_account.html')
        else:
            return render(request,'accounts/deactivate_account.html')
    except:
        messages.error(request,'Something went wrong.')
        return render(request,'accounts/deactivate_account.html')

def activate_account(request):
    if(request.method=='POST'):
        try:
            email=request.POST['email']
            if(not User.objects.filter(email=email).exists()):
                messages.error(request, 'Please check your email address.')
                return render(request,'accounts/activate_account.html')
            user=User.objects.get(email=email)
            send_verification_email(request,user,'Click on the link to acctivate your account.')
            messages.success(request, 'Check mail for account activation.')
            return redirect('/')
        except:
            messages.error(request,'Something went wrong.')
            return render(request,'accounts/activate_account.html')
    else:
        return render(request,'accounts/activate_account.html')