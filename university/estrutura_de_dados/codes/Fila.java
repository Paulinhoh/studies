// Custo: O(1) baseado em Lista Encadeada 
public class Fila {
    private Object[] array;
    private int front;
    private int rear;
    private int capacity;
    private int currentSize;

    public Fila(int size) {
        this.array = new Object[size];
        this.capacity = size;
        this.front = 0;
        this.rear = -1;
        this.currentSize = 0;
    }

    public void enqueue(Object item) {
        if (isFull()) {
            System.out.println("Tamanho da Fila excedida");
            System.exit(-1);
        }
        this.rear = (this.rear + 1) % this.capacity;
        this.array[this.rear] = item;
        this.currentSize++;
    }

    public Object dequeue() {
        Object value = this.array[this.front];
        this.front = (this.front + 1) % this.capacity;
        this.capacity--;
        return value;
    }

    public int size() {
        return this.currentSize;
    }

    public boolean isFull() {
        return this.currentSize == this.capacity;
    }

    public Object peek() {
        return this.array[this.front];
    }
}
