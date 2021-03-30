from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname', False)
        lname = request.POST.get('lname', False)
        email = request.POST.get('email', False)
        username = request.POST.get('uname', False)
        password = request.POST.get('pwd', False)
        repassword = request.POST.get('rpwd', False)
        
        if ( fname == "" or lname == "" or username == "" or email == "" or password == ""):
            messages.error(request, "All field must be filled")
            return render(request, "register.html")
        elif ( password != repassword ):
            messages.error(request, "Re-entered password must be same as entered password")
            return render(request, "register.html")
        else:
            user = User.objects.create_user(username = username, password = password, email = email, first_name = fname, last_name = lname)
            user.save()
            messages.error(request, "You have successfully registered yourself. Now you can log in :)")
            return redirect("../login")
    else:
        return render(request, "register.html")