# -*- coding: utf-8 -*-
"""Build the exam multiple-choice deck from all provided PDFs (deduplicated)."""
TF   = ["True", "False"]
PARA3= ["Divide-and-Conquer", "Incremental", "Other"]
TYPE3= ["Divide & Conquer", "Dynamic Programming", "Greedy"]
DS4  = ["O(1)", "O(log n)", "O(n)", "O(n log n)"]
CA   = ["O(1)", "O(lg n)", "O(√n)", "O(n)", "O(n lg n)", "O(n²)"]
CB   = ["O(lg n)", "O(n)", "O(n lg n)", "O(n²)", "O(n³)", "O(2ⁿ)"]
CR   = ["O(n)", "O(n lg n)", "O(n²)", "O(n² lg n)", "O(n³)", "O(n!)"]
REC  = ["O(n)", "O(n lg n)", "O(n^1.5)", "O(n²)", "O(n² lg n)", "O(n³)"]
TRAV = ["Preorder", "Postorder", "Inorder", "None of the above"]
CASE3= ["Case 1", "Case 2", "Case 3"]
ROT5 = ["O(1)", "O(lg n)", "O(n)", "O(n lg n)", "O(n²)"]

T = []
def topic(name, opts, items): T.append((name, opts, items))

topic("Asymptotics & Growth", TF, [
 ("2.5ⁿ = Θ(2ⁿ)", "False", "Short test 1 · P2a"),
 ("n² = Θ(4^(lg n))", "True", "Short test 1 · P2b"),
 ("n·2ⁿ = o(2ⁿ)", "False", "Short test 1 · P2c"),
 ("n! = ω(2ⁿ)", "True", "Short test 1 · P2d"),
 ("f(n) = Ω(f(n))", "True", "Short test 1 · P2e"),
 ("f(n) = ω(f(n))", "False", "Short test 1 · P2f"),
 ("f(n) = O(g(n)) implies g(n) = O(f(n))", "False", "Short test 1 · P2g"),
 ("f(n) = O(g(n)) and g(n) = O(h(n)) implies f(n) = O(h(n))", "True", "Short test 1 · P2h"),
 ("f(n) = o(g(n)) if and only if g(n) = ω(f(n))", "True", "Short test 1 · P2i"),
 ("There exist f,g with f(n)=Θ(g(n)) and f(n)=o(g(n))", "False", "Bonus Test 1 · P9b"),
 ("There exist f,g with f(n)=o(g(n)) and f(n)≠Θ(g(n))", "True", "Bonus Test 1 · P9c"),
 ("There exist f,g with f(n)=Θ(g(n)) and f(n)≠O(g(n))", "False", "Bonus Test 1 · P9d"),
 ("There exist f,g with f(n)=Ω(g(n)) and f(n)≠O(g(n))", "True", "Bonus Test 1 · P9e"),
 ("2^(2n) = O(2ⁿ)", "False", "Bonus Test 1 · P9h"),
 ("(log n)^(log n) = Θ(n^(log log n))", "True", "Bonus Test 1 · P9i"),
 ("2^(n+1) = O(2ⁿ)", "True", "Bonus Test 1 · P9j"),
 ("πⁿ = O(n!)", "True", "Bonus Test 1 · P9k"),
 ("log n = Θ(log²n)", "False", "Bonus Test 1 · P9l"),
 ("n^(log n) = Θ(2^(n−1))", "False", "Bonus Test 1 · P9m"),
 ("2ⁿ = Θ(3ⁿ)", "False", "Bonus Test 1 · P9n"),
 ("Any recurrence relation can be solved using the Master Method.", "False", "Short test 1 · P8c"),
])

topic("Recurrences", REC, [
 ("Θ bound for T(n) = 8T(n/2) + n²/2", "O(n³)", "Retake · P2b"),
 ("Θ bound for T(n) = 27T(n/9) + n", "O(n^1.5)", "Retake · P2c"),
])

topic("Sorting", TF, [
 ("The runtime of InsertionSort is O(n log n).", "False", "Bonus Test 1 · P9f"),
 ("Formulating InsertionSort as a recursive procedure improves its runtime.", "False", "Bonus Test 1 · P9g"),
 ("The runtime of MERGE is O(n).", "True", "Bonus Test 1 · P9q"),
 ("The runtime of MaxHeapify is Θ(n log n).", "False", "Bonus Test 1 · P9r"),
 ("Stable (or easily made stable): InsertionSort", "True", "Bonus Test 1 · P9o"),
 ("Stable (or easily made stable): MergeSort", "True", "Bonus Test 1 · P9o"),
 ("Stable (or easily made stable): HeapSort", "False", "Bonus Test 1 · P9o"),
 ("In-place (or easily made in-place): InsertionSort", "True", "Bonus Test 1 · P9p"),
 ("In-place (or easily made in-place): MergeSort", "False", "Bonus Test 1 · P9p"),
 ("In-place (or easily made in-place): HeapSort", "True", "Bonus Test 1 · P9p"),
 ("In QuickSort, always using the last element of the sub-array as pivot gives worst-case recursion depth Θ(log n).", "False", "Bonus Test 2 · P8c"),
 ("BucketSort runs in expected linear time if the input has uniform distribution.", "True", "Bonus Test 2 · P8d"),
 ("BucketSort can sort an arbitrary collection of numbers in O(n) time.", "False", "Retake · P10d"),
 ("Any comparison-based sorting algorithm requires Ω(n lg n) time for input size n.", "True", "Short test 1 · P8f"),
 ("Counting sort is stable.", "True", "Bonus Test 2 · P8j"),
 ("Sorting an array of n integers in the range [0, n²−1] runs in Ω(n lg n) time.", "False", "Bonus Test 2 · P8l"),
 ("The minimum, maximum, and median elements can be found in Θ(n) time.", "True", "Bonus Test 2 · P8e"),
 ("2(n−1) is the lower bound for the comparisons needed to find both the min and max of n distinct integers.", "False", "Bonus Test 2 · P8k"),
])

topic("Heaps", TF, [
 ("There exists a heap T storing seven distinct elements whose rLR traversal yields them in sorted order.", "True", "Bonus Test 1 · P9a"),
 ("The sequence [23,17,14,6,13,10,1,5,7,12] is a max-heap.", "False", "Short test 1 · P8i"),
 ("A min-heap can be represented by an array.", "True", "Retake · P10l"),
 ("An array sorted in decreasing order is a min-heap.", "False", "Final Exam · P13l"),
])

topic("Heap sizes", None, [
 ("What is the height h of a heap of size n?", "⌊log n⌋",
  ["2ⁿ", "n", "⌊n/2⌋", "⌊log n⌋"], "Short test 1 · P7a"),
 ("What is the largest size n for a heap with height h?", "2^(h+1) − 1",
  ["2ʰ", "2^(h+1) − 1", "2h − 1", "⌊log h⌋ + 1"], "Short test 1 · P7b"),
 ("What is the smallest size n for a heap with height h?", "2ʰ",
  ["2ʰ", "h", "h²", "2^(h+1) − 1"], "Short test 1 · P7c"),
])

topic("Trees", TF, [
 ("A full binary tree is complete.", "False", "Bonus Test 2 · P8a"),
 ("A complete binary tree is full.", "True", "Bonus Test 2 · P8b"),
 ("Given the sequence (v₁,…,vₙ) of a binary tree traversal by LrR, one can reconstruct the exact structure of the tree.", "False", "Retake · P10g"),
])

topic("Tree Traversals", TRAV, [
 ("{C, B, D, A, F, E, H, G, I}", "Inorder", "Bonus Test 2 · P9a"),
 ("{H, D, B, E, F, I, C, G, A}", "None of the above", "Bonus Test 2 · P9b"),
 ("{A, B, C, D, E, F, G, H, I}", "Preorder", "Bonus Test 2 · P9c"),
 ("{A, B, E, C, D, F, G, H, I}", "None of the above", "Bonus Test 2 · P9d"),
 ("{C, D, B, F, H, I, G, E, A}", "Postorder", "Bonus Test 2 · P9e"),
])

topic("Data Structure Operations", DS4, [
 ("PUSH in a stack", "O(1)", "Retake · P1a"),
 ("ENQUEUE in a queue", "O(1)", "Retake · P1b"),
 ("APPEND in an unsorted array", "O(1)", "Retake · P1c"),
 ("INSERT in a priority queue", "O(log n)", "Retake · P1d"),
 ("FIND_MIN in a stack", "O(n)", "Retake · P1e"),
 ("FIND_MIN in a queue", "O(n)", "Retake · P1f"),
 ("INSERT at an arbitrary position in an unsorted array", "O(n)", "Retake · P1g"),
 ("FIND_MIN in a priority queue", "O(1)", "Retake · P1h"),
 ("POP in a stack", "O(1)", "Retake · P1i"),
 ("DEQUEUE in a queue", "O(1)", "Retake · P1j"),
 ("SEARCH in a sorted array", "O(log n)", "Retake · P1k"),
 ("SEARCH in a priority queue", "O(n)", "Retake · P1l"),
])

topic("Linked Lists", TF, [
 ("ListSearch in a linked list runs in O(1) time.", "False", "Bonus Test 2 · P8f"),
 ("ListPrepend in a linked list runs in O(1) time.", "True", "Bonus Test 2 · P8g"),
 ("ListDelete in a singly linked list runs in O(1) time.", "False", "Bonus Test 2 · P8h"),
 ("ListDelete in a doubly linked list runs in O(1) time.", "True", "Bonus Test 2 · P8i"),
])

topic("Red-Black Trees & BST", TF, [
 ("Any BST storing n numbers can be transformed into any other BST with these n numbers using rotations.", "True", "Bonus Test 3 · P8d"),
 ("It is possible that a leaf in a red-black tree is twice as deep as another leaf in the same tree.", "True", "Short test 3 · P8c"),
 ("It is possible that a leaf in a red-black tree is three times as deep as another leaf in the same tree.", "False", "Bonus Test 3 · P9a"),
 ("Given a red-black tree with black-height k, the largest possible number of internal nodes is 2^(2k)−1.", "True", "Bonus Test 3 · P9b"),
 ("Given a red-black tree with black-height k, the smallest possible number of internal nodes is 2k.", "False", "Bonus Test 3 · P9c"),
 ("Given a red-black tree with black-height k≥2, the maximum ratio between two subtrees is Θ(2ᵏ).", "True", "Bonus Test 3 · P9d"),
 ("A red-black tree with more than 1 element built with RB-Insert contains at least one red node.", "True", "Bonus Test 3 · P9e"),
 ("The height of a node is the number of edges in a longest path to a leaf.", "True", "Bonus Test 3 · P9f"),
 ("The black-height of a node x counts the black nodes including the sentinel nil[T] and x on a path from x to a leaf.", "False", "Bonus Test 3 · P9g"),
 ("A red-black tree with n internal nodes has height ≤ 2·lg(n+1).", "True", "Bonus Test 3 · P9h"),
 ("Some leaves of a red-black tree can be red.", "False", "Bonus Test 3 · P9i"),
 ("To save space, a single sentinel nil[T] can be used for all leaves.", "True", "Bonus Test 3 · P9j"),
 ("The root's parent is nil[T].", "True", "Bonus Test 3 · P9k"),
 ("Deleting a black node requires no fix-up.", "False", "Bonus Test 3 · P9l"),
])

topic("BST Rotations", ROT5, [
 ("Maximum number of rotations needed to transform any BST on n vertices into any other BST?", "O(n)", "Retake · P13b"),
])

topic("Hashing", None, [
 ("Uniform hash into 1..n — likelihood a new element x is assigned a particular index i?", "1 / n",
  ["1 / n", "n", "1 / i", "1 / C(n,2)"], "Bonus Test 2 · P8m"),
 ("How many elements must be added to the hash table to ensure a collision?", "n + 1",
  ["n", "n + 1", "2n", "2n + 1"], "Bonus Test 2 · P8n"),
 ("With k unique elements already present and no collisions, likelihood the next insert causes a collision?", "k / n",
  ["1 / n", "n / k", "C(k,2)", "k / n"], "Bonus Test 2 · P8o"),
])

topic("Dynamic Programming", TF, [
 ("The matrix-chain multiplication problem exhibits overlapping sub-problems.", "True", "Bonus Test 3 · P8e"),
 ("The longest common subsequence problem exhibits the greedy-choice property.", "False", "Bonus Test 4 · P8j"),
 ("The longest path problem exhibits the optimal substructure property.", "False", "Short test 3 · P8h"),
 ("Every optimization problem can be solved optimally with dynamic programming.", "False", "Short test 3 · P8j"),
 ("Matrix-Chain-Multiplication: any parenthesization of n elements has exactly n−1 pairs of parentheses.", "True", "Bonus Test 3 · P5b"),
])

topic("DP Properties", None, [
 ("Problems solvable by dynamic programming exhibit which two properties?", "Overlapping sub-problems + Optimal substructure",
  ["Overlapping sub-problems + Optimal substructure", "Greedy-choice property + Optimal substructure",
   "Overlapping sub-problems + Independence of sub-problems", "Optimal substructure + Monotone substructure"], "Bonus Test 3 · P8a"),
 ("The rod-cutting problem has which of the following properties?", "Overlapping sub-problems",
  ["Greedy-choice property", "Overlapping sub-problems", "Monotone substructure"], "Bonus Test 3 · P8b"),
 ("The matrix-chain multiplication problem has which of the following properties?", "Optimal substructure",
  ["Optimal substructure", "Monotone substructure", "Independence of sub-problems"], "Bonus Test 3 · P8c"),
])

topic("Greedy, MST & Huffman", TF, [
 ("The binary tree corresponding to an optimal prefix code is full.", "True", "Bonus Test 4 · P8a"),
 ("Every graph has a unique MST.", "False", "Bonus Test 4 · P8b"),
 ("Prim's algorithm is an instance of GenericMST.", "True", "Bonus Test 4 · P8c"),
 ("Kruskal's algorithm is an instance of GenericMST.", "True", "Bonus Test 4 · P8d"),
 ("The greedy algorithm for computing change with coins (25,10,5,1) is optimal.", "True", "Bonus Test 4 · P8e"),
 ("The greedy algorithm for computing change with coins (30,24,12,6) is optimal.", "False", "Bonus Test 4 · P8f"),
 ("The greedy algorithm for computing change with coins (27,9,3,1) is optimal.", "True", "Bonus Test 4 · P8g"),
 ("Huffman's algorithm creates an optimal prefix code.", "True", "Bonus Test 4 · P8h"),
 ("The Shannon-Fano algorithm creates an optimal prefix code.", "False", "Bonus Test 4 · P8i"),
 ("If all edges in a graph have unique weights, then there is a unique MST.", "True", "Retake · P10j"),
 ("If all edges in a graph have unique weights, then there is a unique NST (next-to-best spanning tree).", "False", "Final Exam · P13k"),
 ("Given G=(V,E), any tree T=(V,E*) with E*⊆E is a minimum spanning tree of G.", "False", "Retake · P10c"),
 ("If an edge is the unique lightest edge crossing some cut of a connected undirected graph, it belongs to every MST.", "True", "Short test 5 · P9c"),
 ("The lower bound for computing the Convex Hull of n points is Ω(n lg n).", "True", "Short test 3 · P8e"),
])

topic("Disjoint Sets", TF, [
 ("MakeSet(x) runs in O(1) time.", "True", "Bonus Test 4 · P8k"),
 ("Union(x,y) runs in O(1) time.", "False", "Bonus Test 4 · P8l"),
 ("FindSet(x) runs in O(1) time.", "True", "Bonus Test 4 · P8m"),
 ("A sequence of m MakeSet/Union/FindSet operations, n of which are MakeSet, takes O(m + n lg n) time.", "True", "Bonus Test 4 · P8n"),
])

topic("Algorithmic Paradigms", PARA3, [
 ("SelectionSort", "Incremental", "Bonus Test 1 · P5a"),
 ("QuickSort", "Divide-and-Conquer", "Bonus Test 1 · P5b"),
 ("InsertionSort", "Incremental", "Bonus Test 1 · P5c"),
 ("MergeSort", "Divide-and-Conquer", "Bonus Test 1 · P5d"),
 ("Partition", "Other", "Bonus Test 1 · P5e"),
 ("Binary Search", "Divide-and-Conquer", "Bonus Test 1 · P5f"),
])

topic("Algorithm Types", TYPE3, [
 # QuickSort / MergeSort omitted here: already covered under "Algorithmic Paradigms" (rule #2)
 ("Tarjan's Select", "Divide & Conquer", "Retake · P4d"),
 ("Fractional Knapsack (thief with fractions of items)", "Greedy", "Bonus Test 4 · P9b"),
 ("0-1 Knapsack (thief with whole items)", "Dynamic Programming", "Bonus Test 4 · P9c"),
 ("Optimal Activity Scheduling", "Greedy", "Bonus Test 4 · P9d"),
 ("Shannon-Fano Encoding", "Divide & Conquer", "Bonus Test 4 · P9e"),
 ("Huffman Encoding", "Greedy", "Bonus Test 4 · P9f"),
 ("Optimal Rod Cutting", "Dynamic Programming", "Bonus Test 4 · P9g"),
 ("Prim's Algorithm", "Greedy", "Bonus Test 4 · P9h"),
 ("Kruskal's Algorithm", "Greedy", "Bonus Test 4 · P9i"),
 ("Optimal Matrix Chain Order", "Dynamic Programming", "Final Exam · P7h"),
 ("Dijkstra's Algorithm", "Greedy", "Final Exam · P7i"),
 ("Longest Common Subsequence", "Dynamic Programming", "Retake · P4g"),
 ("Optimal Polygon Triangulation", "Dynamic Programming", "Retake · P4h"),
])

topic("Complexity Bounds", CB, [
 ("Optimal Rod Cutting", "O(n²)", "Bonus Test 3 · P6d"),
 ("Longest Common Subsequence", "O(n²)", "Bonus Test 3 · P6e"),
 ("Multiplying two n×n matrices", "O(n³)", "Bonus Test 3 · P6f"),
 ("Optimal Matrix Chain Multiplication", "O(n³)", "Bonus Test 3 · P6g"),
 ("Enumerating all Rod Cutting solutions", "O(2ⁿ)", "Bonus Test 3 · P6h"),
 ("Huffman's Algorithm", "O(n lg n)", "Bonus Test 4 · P6a"),
 ("Optimal Activity Selection (input already sorted by finish time)", "O(n)", "Bonus Test 4 · P6b"),
 ("Optimal Polygon Triangulation", "O(n³)", "Bonus Test 4 · P6c"),
 ("Longest Palindromic Subsequence", "O(n²)", "Bonus Test 4 · P6d"),
 ("Minimum number of points so every interval contains at least one point", "O(n lg n)", "Bonus Test 4 · P6e"),
 ("Minimum Water Stops", "O(n)", "Bonus Test 4 · P6f"),
])

topic("Complexity — Search", CA, [
 ("FIND in a BST", "O(n)", "Bonus Test 3 · P6a"),
 ("FIND in a Red-Black tree", "O(lg n)", "Bonus Test 3 · P6b"),
 ("DELETE in a Red-Black tree, given a pointer to the node", "O(lg n)", "Bonus Test 3 · P6c"),
])

topic("Complexity — Graphs", CR, [
 ("Tarjan's Select", "O(n)", "Retake · P9a"),
 ("Topological Sort", "O(n²)", "Retake · P9b"),
 ("Depth-first Search", "O(n²)", "Retake · P9c"),
 ("Find Longest Path", "O(n!)", "Retake · P9d"),
 ("Multiply an n×n matrix by an n×n matrix", "O(n³)", "Retake · P9e"),
 ("Mergesort", "O(n lg n)", "Retake · P9f"),
 ("Quicksort", "O(n²)", "Retake · P9g"),
 ("Single-source Shortest Path in an unweighted graph", "O(n²)", "Retake · P9h"),
 ("Single-source Shortest Path in a weighted graph", "O(n² lg n)", "Retake · P9i"),
 ("Floyd-Warshall Algorithm", "O(n³)", "Retake · P9j"),
])

topic("Graphs", TF, [
 ("A DAG has no cycles.", "True", "Retake · P10a"),
 ("The union of all unique shortest paths from a single source in a positively weighted, connected, undirected graph is a tree.", "True", "Retake · P10b"),
 ("The union of all shortest paths (source fixed) in an undirected graph is an MST.", "False", "Short test 5 · P9h"),
 ("An Eulerian cycle of a connected graph can be found in polynomial time.", "True", "Retake · P10e"),
 ("A Hamiltonian cycle of a connected graph can be found in polynomial time.", "False", "Final Exam · P13e"),
 ("If all edges in a graph have the same weight, then BFS computes the single-source shortest path.", "True", "Retake · P10i"),
 ("If all edges have the same weight in a connected undirected graph, BFS produces an MST.", "True", "Short test 5 · P9a"),
 ("The PageRank of an n-vertex graph is an n×n matrix.", "False", "Retake · P10k"),
 ("When adding an edge to a directed graph, the number of SCCs can decrease.", "True", "Retake · P10m"),
 ("When adding an edge to a directed graph, the number of SCCs can increase.", "False", "Final Exam · P13m"),
 ("When adding an edge to a directed graph, the number of SCCs can stay the same.", "True", "Short test 5 · P9f"),
 ("When adding an edge to a directed graph, the number of SCCs decreases by at most 1.", "False", "Short test 5 · P9g"),
 ("The Vertex Cover algorithm that computes a matching is a 2-approximation.", "True", "Final Exam · P13a"),
 ("Every computational problem can be solved in a finite amount of time.", "False", "Final Exam · P13c"),
 ("Every problem in the class NP can be verified in polynomial time.", "True", "Final Exam · P13d"),
])

topic("Shortest Paths", TF, [
 ("Dijkstra solves the SSSP problem on weighted graphs, even with some negative edge weights.", "False", "Retake · P10n"),
 ("Dijkstra can solve SSSP with negative weights if k+1 is added to every edge (−k = most negative weight).", "False", "Short test 5 · P9j"),
 ("Given a weighted DAG, running BFS and relaxing all outgoing edges of v when v is dequeued correctly computes SSSP.", "False", "Short test 5 · P9d"),
 ("For all (u,v)∈E: δ(s,v) < δ(s,u) + w(u,v).", "False", "Final Exam · P10a"),
 ("If δ(s,v) = ∞, then d[v] = ∞ always.", "True", "Final Exam · P10b"),
 ("d[v] ≤ δ(s,v) for all v, and once d[v] = δ(s,v) it never changes.", "False", "Final Exam · P10c"),
 ("If s⇝u followed by edge (u,v) is a shortest path and d[u]=δ(s,u), then after Relax(u,v,w) we have d[v]=δ(s,v).", "True", "Final Exam · P10d"),
 ("If p=⟨v₀,…,vₖ⟩ is a shortest path and we relax (v₀,v₁),…,(vₖ₋₁,vₖ) in order, even intermixed with other relaxations, then d[vₖ]=δ(s,vₖ).", "True", "Final Exam · P10e"),
])

topic("DFS Edge Types", CASE3, [
 ("Tree edge u→v satisfies which case of the DFS theorem?", "Case 2", "Retake · P7a"),
 ("Back edge u→v satisfies which case of the DFS theorem?", "Case 3", "Retake · P7b"),
 ("Forward edge u→v satisfies which case of the DFS theorem?", "Case 2", "Retake · P7c"),
 ("Cross edge u→v satisfies which case of the DFS theorem?", "Case 1", "Retake · P7d"),
])

# ---------- emit JS ----------
def js(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

out = ["const CONCEPTS=["]
total = 0
seen = {}
for name, opts, items in T:
    o = ("opts:[" + ",".join(js(x) for x in opts) + "]," ) if opts else ""
    out.append(" {topic:%s,%sitems:[" % (js(name), o))
    for it in items:
        if len(it) == 3:
            q, a, src = it; ov = None
        else:
            q, a, ov, src = it
        # duplicate = same question asked with the same answer options.
        # (same stem with a different option set is a different question, e.g.
        #  "Optimal Rod Cutting" as a paradigm vs. as a complexity bound)
        norm = (" ".join(q.split()), tuple(ov or opts or []))
        if norm in seen:
            raise SystemExit("DUPLICATE question: %r (also in %s)" % (q, seen[norm]))
        seen[norm] = name
        row = "  [" + js(q) + "," + js(a) + ","
        row += ("[" + ",".join(js(x) for x in ov) + "]" if ov else "null") + "," + js(src) + "],"
        out.append(row); total += 1
    out.append(" ]},")
out.append("];")
open("_concepts.js", "w", encoding="utf-8").write("\n".join(out))
print("topics:", len(T), "questions:", total)
