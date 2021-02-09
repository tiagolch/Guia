from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=25)
    email = models.EmailField(blank=True, null=True)
    celular = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Escala(models.Model):
    choice = [
        ['man', 'Manhã'],
        ['noi', 'Noite'],
    ]
    nome = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    dia = models.CharField(max_length=3, choices=choice, default='noi')
    data = models.DateField()
    ultima_alteração = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nome)

    def get_data(self):
        return self.data.strftime('%d/%m/%Y')

    def get_ultima_alteracao(self):
        return self.ultima_alteração.strftime('%d/%m/%Y %H:%M')


