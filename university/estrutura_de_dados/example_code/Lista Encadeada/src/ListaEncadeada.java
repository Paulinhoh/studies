/* Código adaptado de @marvinferreira. 
 * Disponível em: https://gist.github.com/marvinferreira/598a1a3295dfa80755325ea325b5c076
 */

public class ListaEncadeada {

	private No inicio; //representa a cabeça (inicio) da lista

	//construtor da lista
	public ListaEncadeada(){   
		inicio = null;
	}

	public boolean isEmpty(){
		return inicio == null;
	}
	
	public boolean search( int elem){
		for(No n = inicio; n != null; n = n.prox)
			if (elem == n.valor)
				//encontrou o elemento
				return true;
		// não encontrou o elemento
		return false;                  

	}

	//insere no inicio da lista
	public void insereInicio(int elem){ 
		No novoNo = new No(elem);
		novoNo.prox = inicio; //novoNo -> inicio antigo
		inicio = novoNo;      // inicio -> novoNo
	}

	//elimina o primeiro item da lista
	public void removeInicio(){ 
		inicio = inicio.prox; // elimina o elemento e reposiciona o inicio
	}

	public String exibeLista(){
		//teste de lista vazia
		if(isEmpty()) 
			return "Lista vazia\n"; 
		
		String str = "Lista Encadeada: ";
		
		for (No n = inicio; n != null; n = n.prox)
			str+= " "+ n.valor;
		return str + "\n";
	}

}// fim da classe Lista
