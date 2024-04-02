package avl;

//Esse c�digo � uma contribui��o de Mayank Jaiswal
class AVLTree {
	 
    Node root;
 
    // M�todo que mede a altura da �rvore
    int height(Node N) {
        if (N == null)
            return 0;
 
        return N.height;
    }
 
    // Retorna o valor m�ximo entre dois inteiros
    int max(int a, int b) {
        return (a > b) ? a : b;
    }
 
    // Rotaciona para a direita a sub�rvore com raiz no n� y 
    Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;
 
        // Executa a rota��o
        x.right = y;
        y.left = T2;
 
        // Atualiza as alturas
        y.height = max(height(y.left), height(y.right)) + 1;
        x.height = max(height(x.left), height(x.right)) + 1;
 
        // Retorna a nova raiz
        return x;
    }
 
    // Rotaciona para a esquerda a sub�rvore com raiz no n� x 
    Node leftRotate(Node x) {
        Node y = x.right;
        Node T2 = y.left;
 
        // Executa a rota��o
        y.left = x;
        x.right = T2;
 
        //  Atualiza as alturas
        x.height = max(height(x.left), height(x.right)) + 1;
        y.height = max(height(y.left), height(y.right)) + 1;
 
        // Retorna nova raiz
        return y;
    }
 
    // Obt�m o fator de balanceamento do n� N
    int getBalance(Node N) {
        if (N == null)
            return 0;
 
        return height(N.left) - height(N.right);
    }
 
    Node insert(Node node, int key) {
 
        /* 1.  Inser��o normal na �rvore Bin�ria de Busca (BST) */
        if (node == null)
            return (new Node(key));
 
        if (key < node.key)
            node.left = insert(node.left, key);
        else if (key > node.key)
            node.right = insert(node.right, key);
        else // Valores duplicados n�o s�o permitidos
            return node;
 
        /* 2. Atualiza a altura do ancestral deste n� Update height of this ancestor node */
        node.height = 1 + max(height(node.left),
                              height(node.right));
 
        /* 3. Calcula Fator de Balanceamento */
        int balance = getBalance(node);
 
        // Se o n� est� desbalanceado, ent�o fa�a:
        
        // Rota��o � direita
        if (balance > 1 && key < node.left.key)
            return rightRotate(node);
 
        // Rota��o � esquerda
        if (balance < -1 && key > node.right.key)
            return leftRotate(node);
 
        // Rota��o LR
        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }
 
        // Rota��o RL
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }
       
        return node;
    }
 
    // Exibe o percurso em pr�-ordem
    // Tamb�m exibe a altura de cada n�
    void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.key + " ");
            preOrder(node.left);
            preOrder(node.right);
        }
    }
 
    public static void main(String[] args) {
        AVLTree tree = new AVLTree();
         
        tree.root = tree.insert(tree.root, 10);
        tree.root = tree.insert(tree.root, 20);
        tree.root = tree.insert(tree.root, 30);
        tree.root = tree.insert(tree.root, 40);
        tree.root = tree.insert(tree.root, 50);
        tree.root = tree.insert(tree.root, 25);
 
        /* A �rvore AVL construida seria:
             30
            /  \
          20   40
         /  \     \
        10  25    50
        */
        System.out.println("Percurso em pr�-ordem da �rvore �:");
        tree.preOrder(tree.root);
    }
}