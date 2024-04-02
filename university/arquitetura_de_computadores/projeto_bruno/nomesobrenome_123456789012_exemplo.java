// Como executar no terminal:
// javac nomesobrenome_123456789012_exemplo.java
// java nomesobrenome_123456789012_exemplo entrada saida

// Entrada/saida
import java.io.*;

// A classe que contem a main deve ter o mesmo nome do arquivo
public class nomesobrenome_123456789012_exemplo {
	// Metodo main
	public static void main(String[] args) {
		// A abertura do arquivo pode causar exececao
		try {
			// Exibindo a quantidade de argumentos
			System.out.println("Quantidade de argumentos (args.length): " + args.length);
			// Iterando sobre o(s) argumento(s) do programa
			for(int i = 0; i < args.length; i++) {
				// Mostrando o argumento i
				System.out.println("Argumento " + i + " (args[" + i + "]): " + args[i]);
			}
			// Abrindo os arquivos com as permissoes corretas
			//BufferedReader input = new BufferedReader(new FileReader(args[0]));
			//BufferedWriter output = new BufferedWriter(new FileWriter(args[1]));
			// .
			// .
			// .
			// Fechando os arquivos
			//input.close();
			//output.close();
		}
		// Tratamento da excecao
		catch(Exception e) {
			// Exibindo a pilha de execucao
			e.printStackTrace();
		}
	}
}