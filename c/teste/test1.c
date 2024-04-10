#include <stdio.h>
#include <string.h>

// Definição da estrutura aluno_nota
struct AlunoNota {
    char nome[50]; // Supondo que o nome do aluno tenha no máximo 50 caracteres
    char disciplina; // Supondo que a disciplina seja representada por um único caractere
    float nota;
};

int main() {
    // Declaração da variável 'i' e do array de structs aluno_nota
    int i;
    struct AlunoNota aluno_nota[10];

    // Inicialização dos dados dos alunos
    for (i = 0; i < 10; i++) {
        strcpy(aluno_nota[i].nome, ""); // Inicializando com uma string vazia
        aluno_nota[i].disciplina = ' '; // Inicializando com um espaço em branco
        aluno_nota[i].nota = 0.0; // Inicializando com zero
    }

    // Exibindo os dados iniciais dos alunos (opcional)
    for (i = 0; i < 10; i++) {
        printf("Aluno %d: Nome: %s, Disciplina: %c, Nota: %.2f\n", i+1, aluno_nota[i].nome, aluno_nota[i].disciplina, aluno_nota[i].nota);
    }

    return 0;
}