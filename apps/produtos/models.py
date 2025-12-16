class Produto(models.Model):
    nome = models.CharField(max_length = 120)
    unidade = models.CharField(max_length = 20)
    custo = models.DecimalField(max_digits = 10, decimal_places = 2)
    estoque_atual= models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)