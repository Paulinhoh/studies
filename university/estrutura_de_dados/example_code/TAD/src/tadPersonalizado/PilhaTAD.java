package tadPersonalizado;


//Síntaxe do meu TAD
public interface PilhaTAD {
    
	//metodos de acesso
    public boolean vazia();

    //metodos para atualizacao
    public void push(Object c);
    public Object pop();
}