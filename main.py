from hashlib import sha256

class Node:
    def __init__(self, data):
        self.left     = None
        self.right    = None
        self.parent   = None
        self.sibling  = None
        self.position = None
        self.data     = data
        self.hash = sha256(data.encode()).hexdigest()
       
class Tree:
    def __init__(self, leaves):
        self.leaves = [Node(leaf) for leaf in leaves]
        self.layer  = self.leaves[::]
        self.root   = None
        self.build_tree()
    
    def build_layer(self):
        new_layer = []
        
        if len(self.layer) % 2 == 1:
            self.layer.append(self.layer[-1])
        
        for i in range(0, len(self.layer), 2):
            left = self.layer[i]
            right = self.layer[i+1]
            parent = Node(left.hash + right.hash)
            
            left.parent = parent
            left.sibling = right
            left.position = "left"
            
            right.parent = parent
            right.sibling = left
            right.position = "right"
            
            parent.left = left
            parent.right = right
            
            new_layer.append(parent)
        
        self.layer = new_layer
    
    def build_tree(self):
        while len(self.layer) > 1:
            self.build_layer()
        self.root = self.layer[0].hash
    
    def search(self, data):
        target = None
        hash_value = sha256(data.encode()).hexdigest()
        for node in self.leaves:
            if node.hash == hash_value:
                target = node
        return target
    
    def get_pass(self, data):
        target = self.search(data)
        markle_pass = []
        if not(target):
            return
        markle_pass.append(target.hash)
        while target.parent:
            sibling = target.sibling
            markle_pass.append((sibling.hash, sibling.position))
            target = target.parent
        return markle_pass   
      
def caluculator(markle_pass):
    value = markle_pass[0]
    for node in markle_pass[1:]:
        sib = node[0]
        position = node[1]
        if position == "right":
            value = sha256(value.encode() + sib.encode()).hexdigest()
        else:
            value = sha256(sib.encode() + value.encode()).hexdigest()
    return value  