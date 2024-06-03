from django.shortcuts import render, HttpResponse
from home.models import Contact

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


# Create your views here.
def home(request):
    #return HttpResponse("This is the data created using views")
    context = {'success': False}
    if request.method == 'POST': 
        #print("This is a post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        
        ins = Contact(name= name, email = email, phone = phone, desc = desc) # create the data
        ins.save() # save the data in the database
        print("The data has been sent to the database")
        context = {'success':True}
    return render(request, 'home.html', context)

#def register(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         # Process the data, for instance, save it, or send an email
    #         form.save()
    # else:
    #     form = UserCreationForm()
    # context = {'form':form}
    # return render(request, 'register.html', context)
#     def registerAccount(request):
#         if request.method == 'POST':
#             form = SignUpForm(request.POST)
#             if form.is_valid():
#                 form.save()  # This saves the User to the database
#                 #return redirect('login')  # Redirect to a login page, or wherever you want
#         # else:
#         #         form = SignUpForm()
#     return render(request, 'register.html', {'form': form})

# def text(request):
#     context = {'firstname': 'Abass', 'secondname': 'Kuku', 'greeting': 1}
#     return render(request, 'text.html', context)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the User to the database
            #return redirect('login')  # Redirect to a login page, or wherever you want
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

