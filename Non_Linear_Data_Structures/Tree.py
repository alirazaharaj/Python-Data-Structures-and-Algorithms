# class TreeNode:
#     def __init__(self, data):
#         self.data = data       
#         self.children = []     
#     def add_child(self, child):
#         self.children.append(child)  

#     def print_tree(self, level=0):
#         pr="   " * level + "> " + self.data if level!=0 else "   " * level + self.data 
#         print( pr)  
#         for child in self.children:                
#             child.print_tree(level + 1)            


# if __name__ == '__main__':
#     root = TreeNode("Electronics")
    
#     computer = TreeNode("Computer")
#     computer.add_child(TreeNode("Mac"))
#     computer.add_child(TreeNode("Surface"))

#     think = TreeNode('ThinkPaid')
#     computer.add_child(think)


#     parts = TreeNode('Parts')
#     parts.add_child(TreeNode('Keybord'))
#     parts.add_child(TreeNode('Mouse'))
#     parts.add_child(TreeNode('Speaker'))

#     think.add_child(parts)
    
#     mobile = TreeNode("Mobile")
#     mobile.add_child(TreeNode("iPhone"))
#     mobile.add_child(TreeNode("Samsung"))
#     mobile.add_child(TreeNode("Vivo"))
#     mobile.add_child(TreeNode("Oppo"))
    
#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Dell"))
#     laptop.add_child(TreeNode("HP"))
#     laptop.add_child(TreeNode("Lenovo"))
    
#     root.add_child(computer)
#     root.add_child(mobile)
#     root.add_child(laptop)
    
#     root.print_tree()









# Out Put

# Electronics
#    > Computer
#       > Mac
#       > Surface
#       > ThinkPaid
#          > Parts
#             > Keybord
#             > Mouse
#             > Speaker
#    > Mobile
#       > iPhone
#       > Samsung
#       > Vivo
#       > Oppo
#    > Laptop
#       > Dell
#       > HP
#       > Lenovo



class TreeNode:
    def __init__(self, data):
        self.data = data       
        self.children = []     
    def add_child(self, child):
        self.children.append(child)  

    def print_tree(self, level=0):
        pr="   " * level + "> " + self.data if level!=0 else "   " * level + self.data 
        print( pr)  
        for child in self.children:                
            child.print_tree(level + 1)            


if __name__ == '__main__':
    root=TreeNode('Nilupul (CEO)')

    chinami=TreeNode('Chinamay (CTO)')
    root.add_child(chinami)

    vishwa=TreeNode('Vishwa (Infrastructor Head)')
    vishwa.add_child(TreeNode('Dhaval (Cloud Manager)'))
    vishwa.add_child(TreeNode('Abhijit (App Manager)'))

    amir=TreeNode('Aamir (Application Head)')

    chinami.add_child(vishwa)
    chinami.add_child(amir)

    gels=TreeNode('Gels (HR Head)')
    root.add_child(gels)

    gels.add_child(TreeNode('Peter (Recruitement Manager)'))
    gels.add_child(TreeNode('Waqas (Policy Manager)'))


    root.print_tree()
