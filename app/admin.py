from django.contrib import admin
from app.models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone',)
    list_filter = ('nome', 'email', 'telefone',)
    search_fields = ('nome', 'email', 'telefone',)

admin.site.register(Cliente, ClienteAdmin)



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco',)
    list_filter = ('nome', 'descricao', 'preco',)
    search_fields = ('nome', 'descricao', 'preco',)
admin.site.register(Produto, ProdutoAdmin)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data_pedido', 'valor_total', 'status', 'done',)
    list_filter = ('cliente', 'data_pedido', 'produtos', 'status', 'done',)
    search_fields = ('cliente', 'data_pedido', 'produtos', 'status',)
    inlines = [ItemPedidoInline, ]
    actions = ['aprovar_pedidos', 'cancelar_pedidos']

    def aprovar_pedidos(self, request, queryset):
        if queryset.count():
            for obj in queryset:
                obj.status = 'done'
                obj.save()
            self.message_user(request, "Pedidos aprovados com sucesso.")
    aprovar_pedidos.short_description = "Aprovar pedidos selecionados"

    def cancelar_pedidos(self, request, queryset):
        if queryset.count():
            for obj in queryset:
                obj.status = 'cancelled'
                obj.save()
            self.message_user(request, "Pedidos cancelados com sucesso.")
    cancelar_pedidos.short_description = "Cancelar pedidos selecionados"

admin.site.register(Pedido,PedidoAdmin)


class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'quantidade', 'subtotal',)
    list_filter = ('pedido', 'produto', 'quantidade', 'subtotal',)
    search_fields = ('pedido', 'produto', 'quantidade', 'subtotal',)
admin.site.register(ItemPedido, ItemPedidoAdmin)


class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco',)
    list_filter = ('nome', 'endereco', 'produtos_fornecidos',)
    search_fields = ('nome', 'endereco', 'produtos_fornecidos',)
admin.site.register(Fornecedor, FornecedorAdmin)


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'salario', 'data_contratacao', 'ativo', 'criar_acesso',)
    list_filter = ('nome', 'cargo', 'salario', 'data_contratacao', 'ativo', 'criar_acesso',)
    search_fields = ('nome', 'cargo', 'salario', 'data_contratacao', 'ativo', 'criar_acesso',)
    actions = ['desativar_funcionarios', 'ativar_funcionarios']  # Ações personalizadas


    #  ----- ACTIONS -----
    def desativar_funcionarios(self, request, queryset):
        # queryset contém os objetos selecionados
        for obj in queryset:
            obj.ativo = False  # Exemplo de atualização de um campo
            obj.save()
        self.message_user(request, "Funcionários desativados com sucesso.")

    def ativar_funcionarios(self, request, queryset):
        for obj in queryset:
            obj.ativo = True
            obj.save()
        self.message_user(request, "Funcionários ativados com sucesso.")

    # Definir descrições para as ações personalizadas (opcional)
    desativar_funcionarios.short_description = "Desativar funcionários selecionados"
    ativar_funcionarios.short_description = "Ativar funcionários selecionados"

admin.site.register(Funcionario, FuncionarioAdmin)


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'localizacao',)
    list_filter = ('produto', 'quantidade', 'localizacao',)
    search_fields = ('produto', 'quantidade', 'localizacao',)
admin.site.register(Estoque, EstoqueAdmin)
