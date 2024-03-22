import java.util.Iterator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

//Exemplo de fila
public class Fila {	
	
	public static void main(String[] args) {
		//Queue é uma interface, por isso precisa de uma implementacao para seus metodos
		
		//LinkedList pode ser utilizado para implementar uma fila
		Queue<String> queueA = new LinkedList<String>();
		
		//PriorityQueue tambem pode ser usado na implementacao
//		Queue queueB = new PriorityQueue();
		
		queueA.add("palavra 1");
		queueA.add("palavra 2");
		queueA.add("palavra 3");		
		
		// ----- Percorrendo os elementos da fila ----
		
		Iterator<String> it = queueA.iterator();
		
		System.out.println("Elementos da fila\n");
		
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
		// ----------------------------------------------
		
		System.out.println();
		
		//Visualiza primeiro elemento da fila
		System.out.println("Primeiro elemento da fila: " + queueA.peek());
		
		System.out.println("Verifica se elemento esta na fila: " + queueA.contains("palavra 2"));
		
		//Remove e acessa primeiro elemento da fila
		//Fila nao permite escolher o elemento a ser removido
		String acessa = queueA.poll();
		System.out.println("Remove e acessa elemento: " + acessa);		
		
		System.out.println("\nElementos da fila apos remocao\n");
		
		for(String s : queueA) {
			System.out.println(s);
		}	
	}
}
