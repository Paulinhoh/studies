// Custo: 
public class Pilha {
    private Object[] array;
    private int positionHandle;

    public Pilha() {
        this(10);
    }

    public Pilha(int size) {
        this.array = new Object[size];
        this.positionHandle = -1;
    }

    public void push(Object item) {
        if (this.positionHandle < this.array.length - 1) {
            this.positionHandle++;
            this.array[this.positionHandle] = item;
        }
    }

    public Object pop() {
        if (isEmptyList()) {
            return null;
        }
        Object value = array[this.positionHandle];
        this.positionHandle--;

        return value;
    }

    public Object top() {
        if (isEmptyList()) {
            return null;
        }
        return this.array[this.positionHandle];
    }

    public boolean isEmptyList() {
        return this.positionHandle == -1;
    }

    public boolean isFull() {
        return this.array.length == this.positionHandle;
    }
}
