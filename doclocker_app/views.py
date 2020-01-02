
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .form import RegisterForm
from .form import ContactForm
from .form import DocumentForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Document





# Create your views here.
def homepage(request):

    context = {}

    return render(request, 'homepage.html', context)



def doclocker(request):
      # return HttpResponse("Welcome to docker ")
      context = {
          'doclocker_text':"Welcome to DOCLOCKER , You can access your stored Document from anywhere in the WORLD ."
      }
      return render(request, 'doclocker.html' , context)


def contact(request):
    # return HttpResponse("Welcome to docker ")
    context = {
        'contact_text':"If you have any query , We are here to help you !! Fill the form below."
    }
    form_class = ContactForm
    return render(request, 'contact.html', context, {'form': form_class,})





def aboutus(request):
    # return HttpResponse("Welcome to docker ")
    context = {
        'aboutus_text':"About Us "
    }

    return render(request, 'aboutus.html', context)
0
'''def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})'''

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


'''def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = DocumentForm(['post'], file_field=request.FILES['file'])
            instance.save()
            """form.save()"""
            return redirect('Uploadfile')
    else:
        form = DocumentForm()
    return render(request, 'Upload.html', {
        'form': form
    })'''

'''def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('doclocker_app.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )'''

def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        return render(request, 'upload.html')
