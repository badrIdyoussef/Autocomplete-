global CAPACIT
CAPACIT = 27 # 26 character (a-A to z-Z ) + space (' ')

class Node:
    def __init__(self) -> None:
        self.child      = [None]*CAPACIT
        self.endOfWord  = False


class Trie:

    def __init__(self) -> None:
        self.root = Node()

 
    def getChild(self,value : chr, node : Node) -> object:
        if value == '_' : return node.child[CAPACIT - 1]
        return node.child[ord(value.lower()) - 97]
    
    def addChild(self , value , node:Node):
        if value == '_' :
            node.child[CAPACIT - 1]    = Node()
            return
        node.child[ord(value.lower()) - 97] = Node()
     
    def buildTrie(self,string : str , root : Node, index = 0):
        string = string.replace(' ' , '_') # to seport the chars a-z and the space
        if index == len(string) : 
            root.endOfWord = True
            return

        child = self.getChild(string[index]  , root)

        if child == None:

            self.addChild(string[index] , root)
            self.buildTrie(string , self.getChild(string[index]  , root) , index = index + 1)
            
        else:

            self.buildTrie(string , child , index = index + 1)
            


    def getLeaves(self , string : str) -> [Node]:
 
        head = self.root
        for ch in string:
            node = self.getChild(ch , head)
            if node != None:
                head = node
            else:
                return  None
            
        return head        

    def autoComplete(self , string : str  , store = []):
        leaves = self.getLeaves(string) 
        if leaves == None:return
        for idx , leave in enumerate(leaves.child):
            if leave != None:
                Space = '_' if (idx + 97) == 123 else chr(idx + 97)
                if leave.endOfWord :
                    store.append(string+Space)

                self.autoComplete(string+Space , store)
        return store
    