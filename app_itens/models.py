from django.db import models


class Item(models.Model):
    nome = models.TextField(default=None)
    valor = models.CharField(max_length=256, default=None)

    def __init__(self, nome, valor):
        self.nome = nome
        self.categoria = Categoria
        self.valor = valor

    def __str__(self):
        return self.nome


class IAtaque(Item, models.Model):
    dano = models.CharField(max_length=256, default=None)

    def __init__(self, dano, nome, categoria, valor):
        super().__init__(nome, categoria, valor)
        self.dano = dano

    def __str__(self):
        return u'{} - {}'.format(self.dano)


class IDefesa(Item, models.Model):
    defesa = models.CharField(max_length=256, default=None)

    def __init__(self, defesa, nome, categoria, valor):
        super().__init__(nome, categoria, valor)
        self.defesa = defesa

    def __str__(self):
        return u'{} - {}'.format(self.defesa)


class IMagico(Item, models.Model):
    poderMagico = models.CharField(max_length=256, default=None)

    def __init__(self, poderMagico, nome, categoria, valor):
        super().__init__(nome, categoria, valor)
        self.poderMagico = poderMagico

    def __str__(self):
        return u'{} - {}'.format(self.poderMagico)


class Categoria(models.Model):
    cat = models.CharField(max_length=256, default=None)

    def __init__(self, cat):
        self.cat = cat

    def __str__(self):
        return self.cat

# pass 147
