class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    # Функция для добавления нового узла

    def insert(root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = root.insert(root.right, key)
            else:
                root.left = root.insert(root.left, key)
        return root
