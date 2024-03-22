import java.util.Iterator;
import java.util.Stack;

public class Pilha {
	public static void main(String[] args) {

		Stack<String> pilha = new Stack<String>();
		
		pilha.push("palavra 1");
		pilha.push("palavra 2");
		pilha.push("palavra 3");		
		
		// ----- Percorrendo os elementos da pilha ----
		
		Iterator<String> it = pilha.iterator();
		
		System.out.println("Elementos da pilha\n");
		
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
		// ----------------------------------------------
		
		System.out.println();
		//Visualiza primeiro elemento da pilha
		System.out.println("Primeiro elemento da pilha: " + pilha.peek());
		
		System.out.println("Verifica se palavra 2 esta na pilha: " + pilha.contains("palavra 2"));
		System.out.println("Indica posicao da palavra 2: " + pilha.search("palavra 2"));
		
		//Remove primeiro elemento da pilha		
		String acessa = pilha.pop();
		System.out.println("Remove e acessa elemento: " + acessa);		
		
		System.out.println("\nElementos da pilha apos remocao: " + pilha);				
	}
}
