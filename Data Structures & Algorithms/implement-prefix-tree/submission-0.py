class TrieNode:
    def __init__(self):
        self.children={} #every node can have 26 children alphabets
        self.endOfWord=False #to check the end of the chanracter
         
class PrefixTree:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root

        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            cur=cur.children[c]
        cur.endOfWord=True

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True    

        
        