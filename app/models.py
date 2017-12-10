from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
opcoes = (
	('Disponível', 'Disponível'),
	('Reservada', 'Reservada'),
	('Indisponível', 'Indisponível'),
)

blocos = (
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),
	('D', 'D'),
	('E', 'E'),
)

horarios = (
	('1° Horário - Manhã', '1° Horário - Manhã'),
	('2° Horário - Manhã', '2° Horário - Manhã'),
	('3° Horário - Manhã', '3° Horário - Manhã'),
	('4° Horário - Manhã', '4° Horário - Manhã'),
	('5° Horário - Manhã', '5° Horário - Manhã'),
	('6° Horário - Manhã', '6° Horário - Manhã'),

	('1° Horário - Tarde', '1° Horário - Tarde'),
	('2° Horário - Tarde', '2° Horário - Tarde'),
	('3° Horário - Tarde', '3° Horário - Tarde'),
	('4° Horário - Tarde', '4° Horário - Tarde'),
	('5° Horário - Tarde', '5° Horário - Tarde'),
	('6° Horário - Tarde', '6° Horário - Tarde'),

	('1° Horário - Noite', '1° Horário - Noite'),
	('2° Horário - Noite', '2° Horário - Noite'),
	('3° Horário - Noite', '3° Horário - Noite'),
	('4° Horário - Noite', '4° Horário - Noite'),
)


status_opc = (
	('Aguardando', 'Aguardando'),
	('Deferido', 'Deferido'),
	('Indeferido', 'Indeferido'),
)


class Sala(models.Model):
	nome = models.CharField(max_length=50)
	numero = models.IntegerField()
	bloco = models.CharField(max_length=1, choices=blocos)

	#Manhã
	h1_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível', verbose_name='07:00 - 07:45') #07:00 - 07:45
	h2_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='07:45 - 08:30') #07:45 - 08:30
	h3_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='08:50 - 09:35') #08:50 - 09:35
	h4_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='09:35 - 10:20') #09:35 - 10:20
	h5_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='10:30 - 11:15') #10:30 - 11:15
	h6_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='11:15 - 12:00') #11:15 - 12:00
	#Tarde
	h1_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='13:00 - 13:45') #13:00 - 13:45
	h2_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='13:45 - 14:30') #13:45 - 14:30
	h3_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='14:50 - 15:35') #14:50 - 15:35
	h4_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='15:35 - 16:20') #15:35 - 16:20
	h5_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='16:30 - 17:15') #16:30 - 17:15
	h6_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='17:15 - 18:00') #17:15 - 18:00
	#Noite
	h1_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='19:00 - 19:45') #19:00 - 19:45
	h2_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='19:45 - 20:00') #19:45 - 20:00
	h3_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='20:45 - 21:30') #20:45 - 21:30
	h4_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='21:30 - 22:15') #21:30 - 22:15

	def __str__(self):
		return self.nome + ' | ' + str(self.numero) + ' | ' + self.bloco

class Material(models.Model):
	nome = models.CharField(max_length=50)
	numero = models.IntegerField()
	localizacao = models.CharField(max_length=50)

	#Manhã
	h1_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='07:00 - 07:45') #07:00 - 07:45
	j1_manha = models.CharField(max_length=300, default='-')
	h2_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='07:45 - 08:30') #07:45 - 08:30
	h3_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='08:50 - 09:35') #08:50 - 09:35
	h4_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='09:35 - 10:20') #09:35 - 10:20
	h5_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='10:30 - 11:15') #10:30 - 11:15
	h6_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='11:15 - 12:00') #11:15 - 12:00
	#Tarde
	h1_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='13:00 - 13:45') #13:00 - 13:45
	h2_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='13:45 - 14:30') #13:45 - 14:30
	h3_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='14:50 - 15:35') #14:50 - 15:35
	h4_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='15:35 - 16:20') #15:35 - 16:20
	h5_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='16:30 - 17:15') #16:30 - 17:15
	h6_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='17:15 - 18:00') #17:15 - 18:00
	#Noite
	h1_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='19:00 - 19:45') #19:00 - 19:45
	h2_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='19:45 - 20:00') #19:45 - 20:00
	h3_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='20:45 - 21:30') #20:45 - 21:30
	h4_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',verbose_name='21:30 - 22:15') #21:30 - 22:15


	def __str__(self):
		return self.nome + ' | ' + str(self.numero) + ' | ' + self.localizacao

class ReservarSala(models.Model):
	usuario = models.ForeignKey(User)
	sala = models.ForeignKey(Sala, null = True)
	dataHora_Atual = models.DateTimeField()
	data_da_reserva = models.DateField(default=datetime.datetime.now())
	horario_de_Entrada = models.CharField(max_length=18, choices=horarios, default='1° Horário - Manhã',)
	horario_de_Saida = models.CharField(max_length=18, choices=horarios, default='2° Horário - Manhã',)
	justificativa = models.TextField()
	status = models.CharField(max_length=10, choices=status_opc, default='Aguardando')

	def deferir(self):
		self.status = 'Deferido'
		return 'Deferido'

	def indeferir(self):
		self.status = 'Indeferido'
		return 'Indeferido'	

	def __str__(self):
		return str(self.sala) + ' | ' + self.justificativa

class ReservarMaterial(models.Model):
	usuario = models.ForeignKey(User)
	material = models.ForeignKey(Material, null = True)
	dataHora_Atual = models.DateTimeField()
	data_da_reserva = models.DateField(default=datetime.datetime.now())
	horario_de_Entrada = models.CharField(max_length=18, choices=horarios, default='1° Horário - Manhã')
	horario_de_Saida = models.CharField(max_length=18, choices=horarios, default='2° Horário - Manhã')
	justificativa = models.TextField()
	status = models.CharField(max_length=10, choices=status_opc, default='Aguardando')

	def deferir(self):
		self.status = 'Deferido'
		return 'Deferido'

	def indeferir(self):
		self.status = 'Indeferido'
		return 'Indeferido'	


	def __str__(self):
		return str(self.material) + ' | ' + self.justificativa
