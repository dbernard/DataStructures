
class Node
{
    private int value;
    private Node leftChild;
    private Node rightChild;

    public Node(int val)
    {
        value = val;
    }

    public int getValue()
    {
        return value;
    }

    public void setValue(int val)
    {
        value = val;
    }

    public Node getLeftChild()
    {
        return leftChild;
    }

    public void setLeftChild(Node child)
    {
        leftChild = child;
    }

    public Node getRightChild()
    {
        return rightChild;
    }

    public void setRightChild(Node child)
    {
        rightChild = child;
    }
}


class BST
{
    private Node root;

    public BST(int rootVal)
    {
        // Create root node
        root = createNode(rootVal);
    }

    private Node createNode(int value)
    {
        Node node = new Node(value);
        return node;
    }

    public Node getRoot()
    {
        return root;
    }

    public void insert(Node root, int val)
    {
        // Traverse the left subtree
        if (val <= root.getValue())
        {
            if (root.getLeftChild() == null)
            {
                root.setLeftChild(createNode(val));
                System.out.println("Inserted " + val);
            }
            else
            {
                insert(root.getLeftChild(), val);
            }
        }
        // Traverse the right subtree
        else
        {
            if (root.getRightChild() == null)
            {
                root.setRightChild(createNode(val));
                System.out.println("Inserted " + val);
            }
            else
            {
                insert(root.getRightChild(), val);
            }
        }
    }

    public void search(int value, Node node)
    {
        // IMPLEMENT ME!
    }
}


public class BinarySearchTree
{
    public static void main(String[] args)
    {
        // Create a BST and play with it
        BST tree = new BST(5);
        Node root = tree.getRoot();
        tree.insert(root, 0);
        tree.insert(root, 1);
        tree.insert(root, 2);
        tree.insert(root, 3);
        tree.insert(root, 4);
        tree.insert(root, 6);
        tree.insert(root, 7);
        tree.insert(root, 8);
        tree.insert(root, 9);
    }
}
