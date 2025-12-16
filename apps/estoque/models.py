class EstoqueMovimento (models.Model):
    TIPOS = (('E', 'Entrada'), ('S','Saída'),('A', 'Ajuste'))
    produto = models.ForeignKey ('produtos.Produto', on_delete = models.CASCADE)
    tipo = models.CharField(max_length = 1, choices = TIPOS)
    quantidade = models.DecimalField(max_digits = 10, decimal_places = 2)
    data_mov = models.DateTimeField (auto_now_add=True)
    