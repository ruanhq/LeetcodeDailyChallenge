#Construct a 
class Node:
    def __init__(self, next = None, prev = None, data = None):
        self.next = next 
        self.prev = prev 
        self.data = data
    def push(self, new_data):
        new_node = Node(data = new_data)
        new_node.next = self.head 
        new_node.prev = None 
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            return 
        new_node = Node(data = new_data)
        new_node.next = prev_node.next 
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
    #new_node.next = None
    #if self.head is None: new_node.prev = None, self.head = new_node return
    def append(self, new_data):
        new_node = Node(data = new_data)
        last = self.head
        new_node.next = None 
        if self.head is None:
            new_node.prev = None 
            self.head = new_node
            return
        ####
        while last.next is not None:
            last = last.next
        last.next = new_node 
        new_node.prev = last
    ########
    def insertBefore(self, head_ref, next_node, new_data):
    	new_node = Node(new_data)
    	new_node.prev = next_node.prev
    	next_node.prev = new_node
    	new_node.next = next_node
    	if new_node.prev != None:
    	    new_node.prev.next = new_node
    	else:
    	    head_ref = new_node
    	return head_ref
    ##############
    #
    #
    #s
