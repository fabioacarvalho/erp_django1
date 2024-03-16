from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Value, IntegerField, Case, When
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def pedidos_cliente(self):
        return self.pedido_set.all()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    componente = models.BooleanField(default=False)
    pn = models.CharField(max_length=300, verbose_name="PN", blank=True, null=True)
    sn = models.CharField(max_length=300, verbose_name="SN", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    status = models.CharField(max_length=10, default='draft', choices=[('draft', 'Em preenchimento'), ('waiting', 'Aguardando'), ('cancelled', 'Cancelado'), ('done', "Finalizado")])
    done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.status == 'done' and not self.done:
            self.done = True
        else:
            self.done = False

        super(Pedido, self).save(*args, **kwargs)

    @property
    def valor_total(self):
        return sum([x.subtotal for x in self.itempedido_set.all()])

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.calculo_subtotal()
        super(ItemPedido, self).save(*args, **kwargs)

    # def post_save(self, request=None):
    #     self.subtotal = self.calculo_subtotal()

    def calculo_subtotal(self):
        return self.quantidade * self.produto.preco

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Item Pedido'
        verbose_name_plural = 'Itens Pedido'


# @receiver(post_save, sender=ItemPedido)
# def post_save_receiver(sender, instance, *args, **kwargs):
#     if instance:
#         instance.post_save()


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    produtos_fornecidos = models.ManyToManyField(Produto)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


class Funcionario(User):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_contratacao = models.DateField()
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    criar_acesso = models.BooleanField(default=True, verbose_name='Criar Acesso')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'


class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    localizacao = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
