from django.db import models


class Ministerio(models.Model):
    nome_ministerio = models.CharField(max_length=30)
    funcao = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_ministerio


class Pessoa(models.Model):
    nome = models.CharField(max_length=25)
    sobre_nome = models.CharField(max_length=25)
    # ministerio = models.ForeignKey('Ministerio', on_delete=models.DO_NOTHING, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    celular = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.nome} {self.sobre_nome}'


class Escala(models.Model):
    nome = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    data = models.DateTimeField()
    ministerio = models.ForeignKey('Ministerio', on_delete=models.DO_NOTHING)
    ultima_alteração = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        ministerio = str(self.ministerio)
        return f'{str(self.nome)} {ministerio}'

    def get_ministerio(self):
        return f' {self.ministerio}'

    def get_data(self):
        return self.data.strftime('%d/%m/%Y %H:%M')

    def get_ultima_alteracao(self):
        return self.ultima_alteração.strftime('%d/%m/%Y %H:%M')


