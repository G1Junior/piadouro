from datetime import date
from django.db import models
from django.contrib.auth.models  import User
from django.core.exceptions import ValidationError

ESTADO_CIVIL = (
    ('s', 'Solteiro'),
    ('n', 'Namorando'),
    ('no', 'Noivando'),
    ('c', 'Casado'),
    ('v', 'Viuvo'),
    ('p', 'Piranhage'),
)

ESTADOS = (
    ('rs', 'Rio Grande do Sul'),
    ('sc','Santa Catarina'),
    ('pr', 'Paraná'),
)


def validador_idade(data_nascimento):
    hoje = date.today()
    delta = hoje - data_nascimento

    if delta.days / 365.25 < 18:
        raise ValidationError(
        'sai fora  menó',
        params={'value': data_nascimento},
        )

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    foto = models.ImageField()
    telefone = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=2, choices=ESTADO_CIVIL)
    data_nascimento = models.DateField(validators=[validador_idade])
    estado = models.CharField(max_length=2, choices=ESTADOS)
    cidade = models.CharField(max_length=64)
    desempregado = models.BooleanField()

    seguindo = models.ManyToManyField('self', related_name='seguidores')

    def __str__(self):
        return f'{self.usuario}'