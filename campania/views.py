from django.shortcuts import render, redirect
from campania.models import Campania, Donacion
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import SignUpForm, donarMonto
from django.contrib import messages
from datetime import datetime, date
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.views.generic import DetailView
from .models import Campania


class CampaniaDetailView(DetailView):
    model = Campania
    template_name = "campania/detail.html"  # Make sure you have this template in your templates directory


# Create your views here.


def home(request):
    campanias = Campania.objects.all().order_by("-id")
    return render(request, "catalog.html", {"campanias": campanias})


def get_campania_por_categoria(request, categoria_id):
    campanias = Campania.objects.filter(categorias__in=[categoria_id])
    return render(request, "catalog.html", {"campanias": campanias})


def do_signup(request):
    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            username = sign_up_form.cleaned_data.get("username")
            password = sign_up_form.cleaned_data.get("password1")
            nombre = sign_up_form.cleaned_data.get("nombre")
            apellido = sign_up_form.cleaned_data.get("apellido")
            email = sign_up_form.cleaned_data.get("email")

            if User.objects.filter(username=username).exists():
                messages.error(
                    request, "El username ingresado ya está siendo utilizado!"
                )
            else:
                nuevo_usuario = User(
                    username=username,
                    password=make_password(password),
                    is_superuser=False,
                    first_name=nombre,
                    last_name=apellido,
                    email=email,
                    is_staff=False,
                    is_active=True,
                    date_joined=datetime.now(),
                )
                nuevo_usuario.save()

                return redirect("success_signup")
    else:
        sign_up_form = SignUpForm()

    return render(request, "signup.html", {"sign_up_form": sign_up_form})


def success_signup(request):
    return render(request, "success_signup.html")


def do_signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Usuario o contraseña inválidos.")
        else:
            messages.error(request, "Usuario o contraseña inválidos.")

    form = AuthenticationForm()
    return render(request, "signin.html", {"signin_form": form})


def do_logout(request):
    logout(request)
    return redirect("signin")


def procesar_donacion(request, campania_id):
    if request.method == "POST":

        form_monto = donarMonto(request.POST)

        if form_monto.is_valid():
            monto_donar = form_monto.cleaned_data["monto"]
            campania = Campania.objects.get(pk=campania_id)

            nueva_donacion = Donacion(
                usuario=request.user, campania=campania, monto=monto_donar
            )

            nueva_donacion.save()

            campania.monto_recaudado += Decimal(monto_donar)

            campania.save()

            return redirect("home")
    else:
        campania = Campania.objects.get(pk=campania_id)
        fecha_actual = timezone.now()
        duracion = campania.fecha_cierre - fecha_actual

        duracion_en_dias = duracion.days

        if duracion_en_dias > 0:
            form_monto = donarMonto()
        else:
            return redirect("campania_fin")

    return render(
        request,
        "donacion.html",
        {
            "campania": campania,
            "duracion_en_dias": duracion_en_dias,
            "donar_monto": form_monto,
        },
    )


def campania_fin(request):
    return render(request, "campania_fin.html")


@login_required
def get_mis_donaciones(request):
    donaciones = Donacion.objects.filter(usuario=request.user).order_by("-id")
    return render(request, "list_donaciones.html", {"donaciones": donaciones})
