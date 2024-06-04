class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, size):
        level = self.get_level()
        spaces = ' ' * level * 3
        prefix = spaces + "|__" if self.parent else ""
        
        if level <= size:
            print(prefix + self.data)
            
        if self.children:
            for child in self.children:
                child.print_tree(size)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    baroda = TreeNode("Baroda")
    ahmedabad = TreeNode("Ahmedabad")
    
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(baroda)
    gujarat.add_child(ahmedabad)
    
    mysore = TreeNode("Mysore")
    bangluru = TreeNode("Bangluru")
    
    karnataka = TreeNode("Karnataka")
    karnataka.add_child(bangluru)
    karnataka.add_child(mysore)
    
    india = TreeNode("India")
    india.add_child(gujarat)
    india.add_child(karnataka)
    
    princeton = TreeNode("Princeton")
    trenton = TreeNode("Trenton")
    
    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(princeton)
    new_jersey.add_child(trenton)
    
    san_francisco = TreeNode("San Francisco")
    mountain_view = TreeNode("Mountain View")
    palo_alto = TreeNode("Palo Alto")
    
    california = TreeNode("California")
    california.add_child(san_francisco)
    california.add_child(mountain_view)
    california.add_child(palo_alto)
    
    usa = TreeNode("USA")
    usa.add_child(new_jersey)
    usa.add_child(california)
    
    world = TreeNode("Global")
    world.add_child(india)
    world.add_child(usa)

    return world

if __name__ == '__main__':
    ############## Exercise One ###############
    print("")
    print("############ Answers to Exercise One ################")
    print("")
    
    tree = build_product_tree()
    
    print("")
    print("############ Print To Level 1 ################")
    print("")
    tree.print_tree(1)
    
    print("")
    print("############ Print To Level 2 ################")
    print("")
    tree.print_tree(2)
    
    print("")
    print("############ Print To Level 3 ################")
    print("")
    tree.print_tree(3)
    