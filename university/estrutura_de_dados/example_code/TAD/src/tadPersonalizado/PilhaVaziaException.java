package tadPersonalizado;

/**
 * Definicao de excecao para TAD pilha
 * 
 */
public class PilhaVaziaException extends RuntimeException {

	private static final long serialVersionUID = 1L;

	public PilhaVaziaException() {
		this("pilha");
	}

	public PilhaVaziaException(String nome) {
		super(nome + " está vazia");
	}

}
