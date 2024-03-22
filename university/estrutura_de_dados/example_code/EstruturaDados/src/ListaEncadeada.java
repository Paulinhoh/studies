import java.util.Iterator;
import java.util.LinkedList;

public class ListaEncadeada {
	public static void main(String[] args) {

		LinkedList<String> lista = new LinkedList<String>();
		
		lista.add("palavra 1");
		lista.add("palavra 2");
		lista.add("palavra 3");		
		
		// ----- Percorrendo os elementos da fila ----
		
		Iterator<String> it = lista.iterator();
		
		System.out.println("Elementos da lista\n");
		
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
		// ----------------------------------------------
		
		System.out.println();
		//Visualiza primeiro elemento da fila
		System.out.println("Primeiro elemento da lista: " + lista.peek());
		
		System.out.println("Verifica se elemento está na lista: " + lista.contains("palavra 2"));
		
		//Remove primeiro elemento da lista		
		String acessa = lista.poll();
		System.out.println("Remove e acessa elemento: " + acessa);
		
		it = lista.iterator();
		
		System.out.println("\nElementos da lista após remoção\n");
		
		for(String s : lista) {
			System.out.println(s);
		}		
		
		//Acessa elemento utilizando um índice. Você escolher o elemento que vai ser manipulado
		System.out.println("Primeiro elemento da lista " + lista.get(0));
	}
}
