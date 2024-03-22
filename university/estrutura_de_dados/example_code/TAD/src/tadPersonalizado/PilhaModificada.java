package tadPersonalizado;

public class PilhaModificada implements PilhaTAD {
	
	private int topo;
	private Object[] pilha;
	private String nome;
	private int indice;
	
	public PilhaModificada() {
		this("pilha", 10);
	}

	public PilhaModificada(String lnome, int capacidade) {
		nome = lnome;
		topo = 0;
		indice = 0;
		pilha = new Object[capacidade];
	}

	public boolean vazia()  {
		return (topo == 0);
	}

	public boolean cheia()  {
		return (topo == pilha.length);
	}

	public void push(Object obj) {		
		
		Object[] aux = pilha.clone();
		
		pilha[0] = obj;
		
		for(int i = 1; i < aux.length;i++) {
			pilha[i] = aux[i-1];
		}
		
		topo++;
	}

	public Object pop() {
		if (topo == 0) 
			throw new PilhaVaziaException(nome);
		else {					
			
			Object valor = pilha[0];
			
			for(int i = 1; i < pilha.length;i++) {
				pilha[i-1] = pilha[i];
			}
			
			pilha[pilha.length-1] = 0;					
			
			topo--;
			return valor;
		}
		
	}
}
