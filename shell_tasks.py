

class Tarefa(object):
    name = None  # Nome curto para o botão
    description = None  # descricao da acao
    clients = None  # todos por padrao
    color = "warning"  # cor do botão, warning, danger, success, primary, default

    @classmethod
    def run(cls):
        raise NotImplementedError


class GenerateFakeCustomer(Tarefa):
    name="Generate Fak eCustomers"
    description="Gerar dados fake"
    clients=None
    color="success"

    @classmethod
    def run(cls):
        from faker import Faker
        from app.models import Cliente

        fake = Faker()
        for _ in range(10):
            Cliente.objects.create(
                nome=fake.name(),
                email=fake.email(),
                telefone=fake.phone_number()
            )
        print("Clientes gerados com sucesso.")

class GenerateFakeProduct(Tarefa):
    name="Gerar dados fake"
    description="Gerar dados fake"
    clients=None
    color="success"

    @classmethod
    def run(cls):
        from faker import Faker
        from app.models import Produto

        fake = Faker()
        for _ in range(15):
            nome = fake.word().capitalize()
            descricao = fake.paragraph()
            preco = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
            ativo = fake.boolean(chance_of_getting_true=80)
            componente = fake.boolean(chance_of_getting_true=20)
            pn = fake.random_letters(length=10)
            sn = fake.random_number(digits=10)

            Produto.objects.create(
                nome=nome,
                descricao=descricao,
                preco=preco,
                ativo=ativo,
                componente=componente,
                pn=pn,
                sn=sn
            )
        print("Produtos gerados com sucesso.")


class GenerateFakeSupplier(Tarefa):
    name="Generate Fake Suppliers"
    description="Gerar dados fake"
    clients=None
    color="success"

    @classmethod
    def run(cls):
        from faker import Faker
        from app.models import Fornecedor

        fake = Faker()
        for _ in range(10):
            Fornecedor.objects.create(
                nome=fake.name(),
                endereco=fake.address(),
            )
        print("Fornecedores gerados com sucesso.")


class GenerateFakeStaff(Tarefa):
    name="Generate Fake Staffs"
    description="Gerar dados fake"
    clients=None
    color="success"

    @classmethod
    def run(cls):
        from faker import Faker
        from app.models import Funcionario

        fake = Faker()
        for _ in range(10):
            username = fake.user_name()
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            password = fake.password(length=12)

            nome = f"{first_name} {last_name}"
            cargo = fake.job()
            salario = fake.pydecimal(left_digits=5, right_digits=2, positive=True)
            data_contratacao = fake.date_between(start_date='-5y', end_date='today')
            ativo = fake.boolean(chance_of_getting_true=80)
            criar_acesso = fake.boolean(chance_of_getting_true=70)

            Funcionario.objects.create(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                nome=nome,
                cargo=cargo,
                salario=salario,
                data_contratacao=data_contratacao,
                ativo=ativo,
                criar_acesso=criar_acesso
            )
        print("Funcionários gerados com sucesso.")
