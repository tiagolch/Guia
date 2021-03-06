from django.db import models


class Ministerio(models.Model):
    nome_ministerio = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_ministerio


class Funcao(models.Model):
    ministerio = models.ForeignKey(Ministerio, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=30)

    def __str__(self):
        return f'{str(self.ministerio)} {self.funcao}'


class Pessoa(models.Model):
    nome = models.CharField(max_length=25)
    sobre_nome = models.CharField(max_length=25)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    celular = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.nome} {self.sobre_nome}'


class Escala(models.Model):
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    nome = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    data = models.DateTimeField()
    ultima_alteração = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.nome)} {str(self.funcao)}'

    def datas(self):
        return self.data.strftime('%A %d/%m/%Y %H:%M')

    def ultima_alteracao(self):
        return self.ultima_alteração.strftime('%d/%m/%Y %H:%M')


