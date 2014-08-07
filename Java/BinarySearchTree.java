
class Node
{
    private int value;
    private boolean isRoot;
    private Node leftChild;
    private Node rightChild;

    public Node(int val)
    {
        value = val;
        isRoot = false;
    }

    public void setAsRoot()
    {
        isRoot = true;
    }

    public boolean isRoot()
    {
        return isRoot;
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
        // Insert a new Node into the tree with (null) parent and value of
        // (rootVal)
        Node empty = new Node(0);
        empty.setAsRoot();
        root = insert(empty, rootVal);
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

    public Node insert(Node root, int val)
    {
        // If root is null, we have found the location where we wish to insert
        // our node
        if (root == null)
        {
            return createNode(val);
        }
        else
        {
            // Traverse the left subtree
            if (val <= root.getValue())
            {
                root.setLeftChild(insert(root.getLeftChild(), val));
            }
            // Traverse the right subtree
            else
            {
                root.setRightChild(insert(root.getRightChild(), val));
            }

            return root;
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
