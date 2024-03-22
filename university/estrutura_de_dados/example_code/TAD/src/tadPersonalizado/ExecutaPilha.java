package tadPersonalizado;

/**
 * Testa TAD Pilha
 * 
 * @author Evandro Eduardo Seron Ruiz
 * 
 * Versão original disponível em: https://dcm.ffclrp.usp.br/~evandro/ibm1030/constru/tad_java.html
 */
public class ExecutaPilha {
	public static void main(String[] args) {		
		
		//TAD
		PilhaModificada p;

		p =  new PilhaModificada("Pilha 1", 10); // 10 caracteres
		
		for (int i=10; i<20; i++)
			p.push(Integer.valueOf(i));
		
		System.out.println("Encheu!");

		for (int i=10; i<20; i++)
			System.out.println(p.pop());
		
		System.out.println("Fim");
	}
}
