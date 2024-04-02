package recursivo;

//This code is contributed by Ankur Narain Verma
class BinarySearchTree {

	Node raiz;

	public BinarySearchTree(){
		raiz = null;
	}

	void insert(int key) {
		raiz = insertRec(raiz, key);
	}

	/* Insere um n� recursivamente */
	Node insertRec(Node root, int key) {

		/* Se a �rvore est� vazia,
		 * retorne um n� */
		if (root == null){
			root = new Node(key);
			return root;
		}

		/* Caso contr�rio, des�a para a sub�rvore adequada */
		if (key < root.key)
			root.left = insertRec(root.left, key);
		else if (key > root.key)
			root.right = insertRec(root.right, key);

		return root;
	}
		
	Node search(Node root, int key) {
		// Caso base: raiz � nula ou chave est� presente na raiz
		if (root==null || root.key==key)
			return root;

		// Chave � maior do que a chave da raiz
		if (root.key < key)
		return search(root.right, key);

		// Chave � menor do que a chave da raiz
		return search(root.left, key);
	}

    void deleteKey(int key) { 
    	raiz = deleteRec(raiz, key); 
    	}
 
    
    Node deleteRec(Node root, int key) {
        /* Caso base: Se a raiz est� vazia */
        if (root == null)
            return root;
 
        /* Caso contr�rio, percorra recursivamente a �rvore */
        if (key < root.key)
            root.left = deleteRec(root.left, key);
        else if (key > root.key)
            root.right = deleteRec(root.right, key);
 
        // Caso contr�rio, a raiz ser� deletada
        else {
            // Verifica se possui apenas um filho
            if (root.left == null)
                return root.right;
            else if (root.right == null)
                return root.left;
 
            // n� com dois filhos: pega o sucessor
            //em ordem (equivale ao menor na sub�rvore a direita)
            root.key = minValue(root.right);
 
            // Delete the inorder successor
            root.right = deleteRec(root.right, root.key);
        }
 
        return root;
    }
 
    int minValue(Node root) {
        
    	int minv = root.key;
        
    	while (root.left != null){
            minv = root.left.key;
            root = root.left;
        }
        return minv;
    }    
    
	// Wrapper
	void inorder() {
		inorderRec(raiz);
	}

	void inorderRec(Node root){
		if (root != null) {
			inorderRec(root.left);
			System.out.println(root.key);
			inorderRec(root.right);
		}
	}

	public static void main(String[] args) {
		BinarySearchTree tree = new BinarySearchTree();

		/* Cria a seguinte BST
			  50
			/	 \
			30	 70
			/ \ / \
		20 40 60 80 */
		tree.insert(50);
		tree.insert(30);
		tree.insert(20);
		tree.insert(40);
		tree.insert(70);
		tree.insert(60);
		tree.insert(80);

//		System.out.println("Busca: " + tree.search(tree.raiz, 100));
//		
//		System.out.println("\nDelete 50");
//        tree.deleteKey(50);
//        System.out.println("Percurso em ordem da �rvore modificada:");
//        tree.inorder();
        
	}
}