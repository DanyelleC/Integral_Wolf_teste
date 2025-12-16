class VendaItem (models.Model):
    venda = models.ForeignKey (Venda, on_delete = models.CASCADE)
    produto = models.ForeignKey ('produtos.Produto', on_delete = models.CASCADE)
    quantidade = models.DecimalField(max_digits = 10, decimal_places = 2)
    preco_unitario = models.DecimalField(max_digits =10, decimal_places = 2)
    