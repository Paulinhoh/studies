
public class ListaTeste {

	public static void main(String[] args) {
		
		ListaEncadeada lista = new ListaEncadeada();
		
		lista.insereInicio(150);
		lista.insereInicio(13);
		lista.insereInicio(5);
			
		
		System.out.println(lista.search(151));
		
//		System.out.println(lista.exibeLista());

	}
}
