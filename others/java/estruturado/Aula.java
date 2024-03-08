// ------------------------ criando projetos -----------------------------------
// ctrl + shift + p -> Java: Create Java Project

// ------------------------ forma basica ---------------------------------------
// No public class <nome> o nome deve ser o mesmo que o arquivo.

// import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

import javax.swing.JOptionPane;

public class Aula {
    public static void main(String[] args) throws Exception {
        // print
        System.out.println("Olá, mundo!");

        // ------------------- variaveis ---------------------------------------
        // em java as variaveis são fortementes tipadas
        // variaveis do tipo inteiro
        byte numero_pequeno = 125; // -128 à 127
        short numero_short = 1021; // -32768 à 32767
        int numero_inteiro = 7555; // -2147483648 à 2147483647
        long numero_long = 151548l; // -922337203685477001 à 922337203685477000
        // na variavel do tipo long é necessario adicionar um l ao final do numero

        // variaveis do tipo ponto flutuante
        float numero_floar = 65.2f; // no tipo float é necessario adionar um f ao final do numero
        double pi = 3.142154548482121894521; // serve para armazenar numeros muito grandes ou muito pequenos

        // variaveis do tipo caractere
        char letra = 'p'; // char só armazena 1 unico caractere

        // variavel do tipo booleano (true OR false)
        boolean estou_com_fome = true;

        // variavel do tipo String
        String nome = "paulinho";

        String nome_completo; // declarando variavel
        nome_completo = "Monkey D. Luffy"; // iniciando variavel

        // ------------------- mensagens contendo variaveis --------------------
        String filme = "Duna: part two"; // %s
        int ano_de_lancamento = 2024; // %d
        int duracao = 150; // %d
        float nota_critica = 9.8f; // %f
        char letra_inicial = 'D'; // %c
        boolean foi_sucesso = true; // %b

        // O Filme <filme> lançado em <ano> tem duração de <duração> minutos

        System.out.println(
                "O Filme " + filme + " lançado em " + ano_de_lancamento + " tem duração de "
                        + duracao + " minutos");
        System.out.format("O Filme %s lançado em %d tem duração de %d minutos\n",
                filme, ano_de_lancamento, duracao);

        // direto em variaveis
        String texto = "O Filme " + filme + " lançado em " + ano_de_lancamento +
                " tem duração de " + duracao + " minutos";
        String texto2 = String.format("O Filme %s lançado em %d tem duração de %d minutos\n", filme,
                ano_de_lancamento, duracao);

        // ------------------- como ler dados do teclado -----------------------
        String ranking;
        int tier;
        String valor;

        // Scanner -> classe
        Scanner leitor = new Scanner(System.in);
        // configurando (definindo que os separadores é: \r OU \n)
        /*
         * leitor.useDelimiter("[\r\n]+");
         */

        System.out.print("Digite o seu ranking: ");
        ranking = leitor.nextLine();

        System.out.print("Digite o tier: ");
        valor = leitor.nextLine();
        tier = Integer.parseInt(valor);

        System.out.print("Qual o seu campeão preferido: ");
        String campeao = leitor.nextLine();

        System.out.format("Você é mono %s no elo %s %d", campeao, ranking, tier);

        String oscar = JOptionPane.showInputDialog(null,
                "Qual o seu filme preferido do ano de 2023?", "Oscar 2024",
                JOptionPane.QUESTION_MESSAGE);
        System.out.println(oscar);

        // ------------------- operações aritmeticas e classe MATH -------------
        /*
         * Operações aritmeticas:
         * 5 + 2 == 7 --> soma
         * 5 - 2 == 3 --> subtração
         * 5 * 2 == 10 --> multiplicação
         * 5 / 2 == 2.5 --> divisão
         * 5 // 2 == 2 --> divisão inteira
         * 5 % 2 == 1 --> resto da divisão inteira
         * ++ | += --> incremento
         * -- | -= --> decremento
         */

        /*
         * Ordem de Precedencia
         * ()
         * / or *
         * + or -
         */

        int numeroA = 5;
        int numeroB = 2;

        double resultado = (double) numeroA + numeroB;
        int resultado2 = Math.abs(-55); // abs: retorna o modulo do valor
        int resultado3 = (int) Math.pow(5, 2); // pow: retorna a exponenciação
        int resultado4 = (int) Math.sqrt(4); // sqrt: retorna a raiz quadrada
        double resultado5 = Math.ceil(4); // ceil: arredonda para cima
        double resultado6 = Math.floor(4); // floor: arredonda para baixo
        double resultado7 = Math.min(4, 55); // min: retorna o valor minimo
        double resultado8 = Math.max(4, 55); // max: retorna o valor maximo

        JOptionPane.showMessageDialog(null, resultado, "Matemática",
                JOptionPane.INFORMATION_MESSAGE);

        // ------------------- como gerar numeros aleatorios -------------------
        // outra maneira só que com menos desempenho
        /*
         * int dado6Faces = 1 + (int) (Math.random() * 6);
         * JOptionPane.showMessageDialog(null, dado6Faces);
         */

        // maneira com mais desempenho
        /*
         * Random gerador = new Random();
         * int numero = gerador.nextInt(6) + 1; // 6 é o maior numero e 1 o valor minimo
         * JOptionPane.showMessageDialog(null, numero);
         */

        Random dado = new Random();

        int faceDados = Integer.parseInt(JOptionPane.showInputDialog(null,
                "Quantas faces tem o dado?"));
        int resultado42 = dado.nextInt(faceDados) + 1;
        JOptionPane.showMessageDialog(null, "Voce tirou " + resultado42 + " no dado.");

        // ------------------- expressões booleanas no java --------------------
        int idade = 18;

        /*
         * > maior que
         * < menor que
         * >= maior ou igual que
         * <= menor ou igual que
         * == igual a
         * != diferente
         */

        boolean resultado55 = idade >= 18;
        System.out.println(resultado55);

        /*
         * && and (e)
         * || or (ou)
         * ! not (negação)
         */

        // credenciais ultra secretas para acessar o projeto
        String usuario = "paulinho";
        String senha = "40028922";

        // o usuario digitou na tela de login
        String usuarioDigitado = "robson";
        String senhaDigitada = "1234";

        boolean loginCorreto = usuario == usuarioDigitado && senha == senhaDigitada;
        System.out.println(loginCorreto);

        /*
         * A B A && B A || B
         * true true true true
         * true false flase true
         * false true flase true
         * false false false false
         */

        // ------------------- econdições em java ------------------------------
        boolean estaChovendo = true;
        boolean temGuadachuva = false;
        // if -> se
        if (estaChovendo == true && temGuadachuva == true) {
            System.out.println("Boa não esta se molhando");
        } else if (estaChovendo == true) {
            System.out.println("Voce pode dançar na chuva!");
        } else {
            System.out.println("Não esta chovendo");
        }

        String video = "hunter x hunter";

        // operador condicional ternario
        String categoria = (video == "hunter x hunter") ? "anime" : "serie";
        System.out.println(categoria);

        // ------------------- switch case -------------------------------------
        String personagem = "Gohan";

        switch (personagem) {
            case "Vegeta":
                System.out.println("Planeta Sayajin");
                break;
            case "Goku":
                System.out.println("Planeta Sayajin");
                break;
            case "Bulma":
                System.out.println("Planeta Terra");
                break;
            case "Piccolo":
                System.out.println("Planeta Namekuseijin");
                break;
            case "Kuririn":
                System.out.println("Planeta Terra");
                break;
            default:
                System.out.println("Origem Desconhecida!");
                break;
        }

        // ------------------- estrutura de repetição --------------------------
        int contador = 0;
        while (contador < 3) {
            System.out.println("Olá");
            contador++;
        }

        do {
            System.out.println("Olá");
            contador++;
        } while (contador < 3);
        // no do while a execulção vai ser feita pelo menos uma vez ja que a verificação
        // esta no final

        // for (<valor inicial>; <condição>; <passo>)
        for (contador = 0; contador < 3; contador++) {
            System.out.println("Olá");
        }

        // ------------------- Arrays (vetores) --------------------------------
        // armazena varios valores do mesmo tipo
        // tipo[] nome = new tipo[<tamanho>];
        /*
         * String[] nomes = new String[5];
         * nomes[0] = "Paulo"
         * nomes[1] = "Gabriel"
         * nomes[2] = "Ana Clara"
         * nomes[3] = "Nida"
         * nomes[4] = "Val"
         */

        // desse jeito não é necessario informar o tamanho
        String[] nomes = new String[] {
                "Paulo", "Gabriel", "Ana Clara", "Nida", "Val"
        };

        for (int posicaoVetor = 0; posicaoVetor < 5; posicaoVetor++) {
            System.out.println(nomes[posicaoVetor]);
        }

        int[] numeros = new int[100];
        // preenche todo o vetor com valor 0
        /*
         * for (int posicaoVetor = 0; posicaoVetor < 100; posicaoVetor++) {
         * numeros[posicaoVetor] = 0;
         * }
         */
        Arrays.fill(numeros, 0); // preenche to o vetor com valor 0

        System.out.println(numeros.length); // retorna o tamnho do vetor
        System.out.println(Arrays.toString(numeros)); // retorna todo o vetor
    }
}
