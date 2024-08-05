import stack as st
import queue as qu
import node as nd
import graf as gr

# menu = 1
# menu = 2
# menu = 3
menu = 4

if menu == 1:
    stack = st.Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.is_empty())
    print(stack.peek())

if menu == 2:
    queue = qu.Queue()
    print(queue.is_empty())
    queue.enqueue("действие 1")
    queue.enqueue("действие 2")
    queue.enqueue("действие 3")
    queue.enqueue("действие 4")

    print(queue.is_empty())
    print(queue.size())
    print(queue.dequeue())
    print(queue.size())

if menu == 3:
    root = nd.Node(70)

    root = root.insert(root)
    root = root.insert(root, 30)
    root = root.insert(root, 56)
    root = root.insert(root, 89)
    root = root.insert(root, 45)
    root = root.insert(root, 60)
    root = root.insert(root, 73)
    root = root.insert(root, 98)
    root = root.insert(root, 84)

if menu == 4:
    g = gr.Graph()

    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.print_graph()
