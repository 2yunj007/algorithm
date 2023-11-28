class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def insert_trie(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True

def has_prefix(root, word):
    node = root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return True

def main():
    n, m = map(int, input().split())
    words = [input().rstrip() for _ in range(n)]
    queries = [input().rstrip() for _ in range(m)]

    root = TrieNode()

    for word in words:
        insert_trie(root, word)

    result = 0
    for query in queries:
        if has_prefix(root, query):
            result += 1

    print(result)

if __name__ == "__main__":
    main()
