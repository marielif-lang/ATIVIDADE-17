from django.db import models

# 1. Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# 2. Aluno
class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

# 3. Perfil Academico (Relacionamento 1:1 com Aluno)
class PerfilAcademico(models.Model):
    link_lattes = models.URLField()
    biografia = models.TextField()
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='perfil')

    def __str__(self):
        return f"Perfil de {self.aluno.nome}"

# 4. Projeto (Relacionamento 1:N com Categoria e N:M com Aluno)
class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='projetos')
    equipe = models.ManyToManyField(Aluno, related_name='projetos')

    def __str__(self):
        return self.titulo