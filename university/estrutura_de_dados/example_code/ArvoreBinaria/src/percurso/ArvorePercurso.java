package percurso;

import recursivo.Node;

public class ArvorePercurso {

    Node raiz;
 
    public ArvorePercurso() { 
    	raiz = null; 
    }

    void printPostorder(Node node) {
        
    	if (node == null)
            return;
 
        printPostorder(node.left);
 
        printPostorder(node.right);
 
        System.out.print(node.key + " ");
    }
 
    void printInorder(Node node){
        if (node == null)
            return;
 
        printInorder(node.left);
 
        System.out.print(node.key + " ");
 
        printInorder(node.right);
    }
 
    void printPreorder(Node node) {
        if (node == null)
            return;
 
        System.out.print(node.key + " ");
 
        printPreorder(node.left);
 
        printPreorder(node.right);
    }
 
    // Wrappers
    void printPostorder() { printPostorder(raiz); }
    void printInorder() { printInorder(raiz); }
    void printPreorder() { printPreorder(raiz); }
 
    public static void main(String[] args) {
        
    	ArvorePercurso tree = new ArvorePercurso();
        tree.raiz = new Node(1);
        tree.raiz.left = new Node(2);
        tree.raiz.right = new Node(3);
        tree.raiz.left.left = new Node(4);
        tree.raiz.left.right = new Node(5);
 
        System.out.println("Percurso pré-ordem da árvore binária é ");
        tree.printPreorder();
 
        System.out.println("\nPercurso em ordem da árvore binária é ");
        tree.printInorder();
 
        System.out.println("\nPercurso pós-ordem da árvore binária é ");
        tree.printPostorder();
    }
}
