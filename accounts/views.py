from django.shortcuts import render,redirect
from allauth.account import views
from django.core.mail import send_mail

def notify(request):
    subject = "題名"
    message = "本文"
    from_email = 'info.hemap@gmail.com'
    recipient_list = [
        
    ]
    send_mail(subject, message, from_email, recipient_list)
    return render(request, 'lpanalysis/home.html')    

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'
    
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('account_logout')
    