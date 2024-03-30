package aula01;

public class App {

  public static void main(String[] args) {
    // iPhone 12, tela de 6.1, 256gb
    // Galaxy Note 20 Ultra, tela de 6.9, 256gb
    // Xiaomi Mi 11 Pro, tela de 6.81, 128gb
    // <tipoVariavel> nomeVariavel = valor;

    // Declarando um objeto do tipo Celular = Instanciar um objeto
    Celular celularA = new Celular();
    celularA.nome = "iPhone 12";
    celularA.tamanhoTela = 6.1f;
    celularA.espacoArmazenamento = 256;
    celularA.sistemaOperacional = "iOS";

    System.out.println(
      "%s com tela de %.1f polegadas e %dgb de armazenamento.".formatted(
          celularA.nome,
          celularA.tamanhoTela,
          celularA.espacoArmazenamento
        )
    );

    Celular celularB = new Celular();
    celularB.nome = "Galaxy Note 20 Ultra";
    celularB.tamanhoTela = 6.9f;
    celularB.espacoArmazenamento = 256;
    celularB.sistemaOperacional = "Android";

    System.out.println(
      "%s com tela de %.1f polegadas e %dgb de armazenamento.".formatted(
          celularB.nome,
          celularB.tamanhoTela,
          celularB.espacoArmazenamento
        )
    );

    Celular celularC = new Celular();
    celularC.nome = "Xiaomi Mi 11 Pro";
    celularC.tamanhoTela = 6.81f;
    celularC.espacoArmazenamento = 128;
    celularC.sistemaOperacional = "Android";

    System.out.println(
      "%s com tela de %.1f polegadas e %dgb de armazenamento.".formatted(
          celularC.nome,
          celularC.tamanhoTela,
          celularC.espacoArmazenamento
        )
    );
  }
}
