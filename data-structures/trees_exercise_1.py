class TreeNode:
    def __init__(self, name, designation):
        self.data = (name, designation)
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, choice):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if choice == "name":
            print(prefix + self.data[0])
        elif choice == "designation":
            print(prefix + "(" + self.data[1] + ")")
        elif choice == "both":
            print(prefix + self.data[0] + "(" + self.data[1] + ")")

        if self.children:
            for child in self.children:
                child.print_tree(choice)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    
    infrastructure = TreeNode("Vishwa", "Infrastructure Head")
    infrastructure.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infrastructure.add_child(TreeNode("Abhijit", "App Manager"))
    
    application = TreeNode("Aamir", "Application Head")
    
    cto.add_child(infrastructure)
    cto.add_child(application)
    
    hr = TreeNode("Gels", "HR Head")
    
    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Waqas", "Policy Manager"))
    
    root.add_child(cto)
    root.add_child(hr)
    
    return root



if __name__ == '__main__':
    
    ############## Exercise One ###############
    print("")
    print("############ Answers to Exercise One ################")
    print("")

    root_node = build_management_tree()

    print("")
    print("############ Print By Names ################")
    print("")
    root_node.print_tree("name") 
    
    print("")
    print("############ Print By Designations ################")
    print("")
    root_node.print_tree("designation")
    
    print("")
    print("############ Print By Both Names and Designations ################")
    print("")
    root_node.print_tree("both")