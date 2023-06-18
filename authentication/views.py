from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class Sign_Up(View): # Registro

    def get(self, request): # Nos muestra el formulario
        form=UserCreationForm() # Construye un formulario de usuario con 3 campos
        return render(request, "signup/signup.html",{"form":form})

    def post(self, request): # Gestiona el envío de información a través del formulario
        form=UserCreationForm(request.POST) # Hace la relación con la tabla de usuario de la base de datos 

        if form.is_valid():
            user=form.save() # Almacena toda la info del usuario
            login(request, user) # envía una petición para logear al usuario
            return redirect('Home') # Redirecciona al home una vez logeado
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg]) # Muestra mensajes de error cuando el formulario no es válido
            return render(request, "signup/signup.html",{"form":form}) 


def log_out(request): # Cerrar sesión
    logout(request)
    return redirect('Home') # Redirecciona al Home una vez que se cierra la sesión

def log_in(request): # Iniciar sesión
    if request.method=="POST": # Pregunta si se ha enviado el formulario con el post
        form=AuthenticationForm(request, data=request.POST) # guarda el formulario del login con los datos introducidos
        if form.is_valid():
            name_user=form.cleaned_data.get("username") # Consigue la info que hay en el campo username
            contra=form.cleaned_data.get("password") # Consigue la info que hay en el campo password
            user=authenticate(username=name_user, password=contra) # Aitentica al usuario
            if user is not None:
                login(request, user) # si el usuario existe se logea y redirecciona al home
                return redirect('Home')
            else:
                messages.error(request, "User not valid") # si no existe suelta un mensaje de error
        else:
            messages.error(request, "Incorrect information") # mensaje de error para cuando la información se halla introducido incorrectamente
    form=AuthenticationForm() # Construye un formulario para login
    return render(request, "login/login.html",{"form":form})
