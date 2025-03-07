class Trie:

    class Node:
        def __init__(self,x='start'):
            self.val = x
            self.children = {}
            self.endOfWord = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = self.Node(letter)
            node = node.children[letter]
        node.endOfWord = True

    def search(self, word: str) -> bool:

        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        
        return node.endOfWord
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
