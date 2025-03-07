class WordDictionary:

    class Node:
        def __init__(self,x):
            self.val = x
            self.children = {}
            self.endOfWord = False

    def __init__(self):
        self.root = self.Node('start')

    def addWord(self, word: str) -> None:
        
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = self.Node(letter)
            node = node.children[letter]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        
        def recurse(node,index):

            if index == len(word):
                return node.endOfWord

            letter = word[index]

            if letter != '.': #it is a definite alphabet
                if letter not in node.children:
                    return False
                return recurse(node.children[letter], index+1)

            else:
                answer = False
                for child in node.children:
                    answer = answer or recurse(node.children[child], index+1)
                    if answer:
                        break
                return answer

        return recurse(self.root,0)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
