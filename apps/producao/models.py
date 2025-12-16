class OrdemProducao(models.Model):
    STATUS = (
        ('ABERTA', 'Aberta'),
        ('EM_EXEC','Em Execução'),
        ('FINALIZADA', 'Finalizada'),
    )
    data_emissao = models.DateField(auto_now_add = True)
    status = models.CharField (max_length = 20, choices = STATUS)
    quantidade_prevista = models.IntegerField()
    