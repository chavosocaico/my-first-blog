from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Sala
from .forms import SalaForm
from .forms import RSalaForm
from .models import Material
from .forms import MaterialForm
from .forms import RMaterialForm
from django.utils import timezone
from .models import ReservarMaterial
from .models import ReservarSala
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
import requests


# Create your views here.
@login_required(login_url='login')
def inicio (request):
	return render(request,'app/inicio.html')

@login_required(login_url='login')
def listar_salas(request):
	sls = Sala.objects.all()
	return render(request, 'app/sala/listar_salas.html', {'salas': sls})

@login_required(login_url='login')
def cadastrar_salas(request):
	if(request.method == "POST"):
		form = SalaForm(request.POST)
		if form.is_valid():
			sala = form.save(commit=False)
			sala.save()
			return redirect('/listar_salas')

	else:
		form = SalaForm()
		return render(request,'app/sala/cadastrar_salas.html',{'form': form})

@login_required(login_url='login')
def listar_materiais(request):
	mtr = Material.objects.all()
	return render(request, 'app/material/listar_material.html',{'material': mtr})

@login_required(login_url='login')
def cadastrar_materiais(request):
	if(request.method == "POST"):
		form = MaterialForm(request.POST)
		if form.is_valid():
			material = form.save(commit=False)
			material.save()
			return redirect('/listar_materiais')

	else:
		form = MaterialForm()
		return render(request,'app/material/cadastrar_material.html', {'form': form})

def loginSUAP(matricula, senha):
	url = 'https://suap.ifrn.edu.br/api/autenticacao/token/'
	params = {'username': matricula, 'password': senha}
	r = requests.post(url, data=params)
	token = r.json()
	return token['token'] if 'token' in token else None


def login(request):
	if request.user.is_authenticated():
		return redirect('inicio')
	else:
		if(request.method == "POST"):
			matricula = request.POST['matricula']
			senha = request.POST['senha']
			if loginSUAP(matricula,senha) is not None:
				user = authenticate(request=request,username=matricula, password=senha)
				if user is not None:
					auth_login(request, user)
					return redirect('inicio')
				else:
					try:
						user = User.objects.get(username = matricula)
						if not user is None:
							user.set_password(senha)
							user.save()
					except ObjectDoesNotExist:
						user = User.objects.create_user(username = matricula, password = senha)
					user = authenticate(request=request, username=matricula, password=senha)
					if user is not None:
						auth_login(request, user)
						return redirect('inicio')
					else:
						return render(request, 'app/login.html')
		return render(request, 'app/login.html')


@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('/login')

@login_required(login_url='login')
def reservar_salas(request,pk):
	sl = Sala.objects.get(pk=pk)
	if(request.method == "POST"):
		form = RSalaForm(request.POST)
		if form.is_valid():
			sala = form.save(commit=False)
			sala.usuario=request.user
			sala.dataHora_Atual = timezone.now()
			sala.sala = sl
			sala.save()
			return redirect('/salas_reservadas')

	else:
		form = RSalaForm()
		return render(request,'app/sala/reservar_sala.html', {'form': form})

@login_required(login_url='login')
def reservar_materiais(request,pk):
	mat = Material.objects.get(pk=pk)
	if(request.method == "POST"):
		form = RMaterialForm(request.POST)
		if form.is_valid():
			material = form.save(commit=False)
			material.usuario=request.user
			material.dataHora_Atual = timezone.now()
			material.material = mat
			material.save()
			return redirect('/materiais_reservados')

	else:
		form = RMaterialForm()
		return render(request,'app/material/reservar_material.html', {'form': form})

@login_required(login_url='login')
def apagar_salas(request, pk):
	sala = Sala.objects.get(pk=pk)
	sala.delete()

	return redirect('listar_salas')

@login_required(login_url='login')
def apagar_materiais(request, pk):
	material= Material.objects.get(pk=pk)
	material.delete()

	return redirect('listar_materiais')

@login_required(login_url='login')
def materiais_reservados(request):
	if request.user.is_staff:
		material = ReservarMaterial.objects.all()
	else:
		material = ReservarMaterial.objects.filter(usuario=request.user)
	return render(request,'app/material/materiais_reservados.html', {'material': material})

@login_required(login_url='login')
def salas_reservadas(request):
	if request.user.is_staff:
		sala = ReservarSala.objects.filter()
	else:
		sala = ReservarMaterial.objects.filter(usuario=request.user)
	return render(request,'app/sala/salas_reservadas.html', {'sala': sala})

@login_required(login_url='login')
def cancelar_RSala(request, pk):
	sala = ReservarSala.objects.get(pk=pk)
	sala.delete()
	return redirect('salas_reservadas')

@login_required(login_url='login')
def cancelar_RMaterial(request, pk):
	material = ReservarMaterial.objects.get(pk=pk)
	material.delete()
	return redirect('materiais_reservados')

@login_required(login_url='login')
def deferir_reserva_sala(request, pk):
	reserva = ReservarSala.objects.get(pk=pk)
	reserva.deferir()
	reserva.save()
	print(reserva.status)
	return redirect('salas_reservadas')

def indeferir_reserva_sala(request, pk):
	reserva = ReservarSala.objects.get(pk=pk)
	reserva.indeferir()
	reserva.save()
	print(reserva.status)
	return redirect('salas_reservadas')

def deferir_reserva_material(request, pk):
	reserva = ReservarMaterial.objects.get(pk=pk)
	reserva.deferir()
	reserva.save()
	print(reserva.status)
	return redirect('materiais_reservados')

def indeferir_reserva_material(request, pk):
	reserva = ReservarMaterial.objects.get(pk=pk)
	reserva.indeferir()
	reserva.save()
	print(reserva.status)
	return redirect('materiais_reservados')

def editar_sala(request, pk):
	sala = get_object_or_404(Sala, pk=pk)
	if request.method == "POST":
		form = SalaForm(request.POST, instance=sala)
		if form.is_valid():
			sala = form.save(commit=False)

			sala.save()
			return redirect('/listar_salas')
	else: 
		sala = SalaForm(instance=sala)
		return render(request, 'app/sala/editar_sala.html', {'sala': sala})

def editar_material(request, pk):
	material = get_object_or_404(Material, pk=pk)
	if request.method == "POST":
		form = MaterialForm(request.POST, instance=material)
		if form.is_valid():
			material = form.save(commit=False)
			material.save()
			return redirect('/listar_materiais', pk=material.pk)
	else: 
		material = MaterialForm(instance=material)
		return render(request, 'app/material/editar_material.html', {'material': material})
	
