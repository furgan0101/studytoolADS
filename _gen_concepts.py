# -*- coding: utf-8 -*-
"""Build the exam multiple-choice deck (question, answer, reasoning, options, source)."""
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
def it(q, a, why, src, opts=None, fig=None): return (q, a, why, src, opts, fig)

topic("Asymptotics & Growth", TF, [
 it("2.5ⁿ = Θ(2ⁿ)", "False", "2.5ⁿ/2ⁿ = 1.25ⁿ → ∞. Exponentials with different bases are never Θ-equivalent.", "Short test 1 · P2a"),
 it("n² = Θ(4^(lg n))", "True", "4^(lg n) = 2^(2·lg n) = n². They are literally the same function.", "Short test 1 · P2b"),
 it("n·2ⁿ = o(2ⁿ)", "False", "The ratio (n·2ⁿ)/2ⁿ = n → ∞, so it is ω(2ⁿ), the opposite of o.", "Short test 1 · P2c"),
 it("n! = ω(2ⁿ)", "True", "n! beats every exponential: n!/2ⁿ → ∞ (Stirling).", "Short test 1 · P2d"),
 it("f(n) = Ω(f(n))", "True", "Reflexive — take c = 1, since f(n) ≥ 1·f(n).", "Short test 1 · P2e"),
 it("f(n) = ω(f(n))", "False", "ω is strict and would need f/f → ∞, but the ratio is always 1.", "Short test 1 · P2f"),
 it("f(n) = O(g(n)) implies g(n) = O(f(n))", "False", "O is not symmetric: n = O(n²) but n² ≠ O(n).", "Short test 1 · P2g"),
 it("f(n) = O(g(n)) and g(n) = O(h(n)) implies f(n) = O(h(n))", "True", "O is transitive — multiply the two constants.", "Short test 1 · P2h"),
 it("f(n) = o(g(n)) if and only if g(n) = ω(f(n))", "True", "o and ω are duals; both say f/g → 0.", "Short test 1 · P2i"),
 it("There exist f,g with f(n)=Θ(g(n)) and f(n)=o(g(n))", "False", "Θ forces f/g → a positive constant, o forces f/g → 0. Mutually exclusive.", "Bonus Test 1 · P9b"),
 it("There exist f,g with f(n)=o(g(n)) and f(n)≠Θ(g(n))", "True", "o(g) always rules out Θ(g); e.g. f = n, g = n².", "Bonus Test 1 · P9c"),
 it("There exist f,g with f(n)=Θ(g(n)) and f(n)≠O(g(n))", "False", "Θ is defined as O and Ω together, so Θ always implies O.", "Bonus Test 1 · P9d"),
 it("There exist f,g with f(n)=Ω(g(n)) and f(n)≠O(g(n))", "True", "e.g. f = n², g = n: bounded below by g but not above.", "Bonus Test 1 · P9e"),
 it("2^(2n) = O(2ⁿ)", "False", "2^(2n) = (2ⁿ)², so the ratio is 2ⁿ → ∞ — not a constant factor.", "Bonus Test 1 · P9h"),
 it("(log n)^(log n) = Θ(n^(log log n))", "True", "Take logs of both: each gives log n · log log n.", "Bonus Test 1 · P9i"),
 it("2^(n+1) = O(2ⁿ)", "True", "2^(n+1) = 2·2ⁿ — just a constant factor of 2.", "Bonus Test 1 · P9j"),
 it("πⁿ = O(n!)", "True", "n! eventually outgrows any fixed exponential cⁿ.", "Bonus Test 1 · P9k"),
 it("log n = Θ(log²n)", "False", "log²n / log n = log n → ∞, so log²n grows strictly faster.", "Bonus Test 1 · P9l"),
 it("n^(log n) = Θ(2^(n−1))", "False", "Compare logs: (log n)² vs n−1. The linear term dominates.", "Bonus Test 1 · P9m"),
 it("2ⁿ = Θ(3ⁿ)", "False", "3ⁿ/2ⁿ = 1.5ⁿ → ∞.", "Bonus Test 1 · P9n"),
 it("Any recurrence relation can be solved using the Master Method.", "False", "It needs the form aT(n/b)+f(n) and fails in the gap cases, e.g. T(n)=2T(n/2)+n log n.", "Short test 1 · P8c"),
])

topic("Recurrences", REC, [
 it("Θ bound for T(n) = 8T(n/2) + n²/2", "O(n³)", "log₂8 = 3 and f(n)=n² = O(n^(3−ε)) → Master case 1 → Θ(n³).", "Retake · P2b"),
 it("Θ bound for T(n) = 27T(n/9) + n", "O(n^1.5)", "log₉27 = 1.5 and f(n)=n = O(n^(1.5−ε)) → Master case 1 → Θ(n^1.5).", "Retake · P2c"),
])

topic("Sorting", TF, [
 it("The runtime of InsertionSort is O(n log n).", "False", "Worst case is Θ(n²) — reverse-sorted input shifts j−1 elements on step j.", "Bonus Test 1 · P9f"),
 it("Formulating InsertionSort as a recursive procedure improves its runtime.", "False", "Same comparisons and shifts; recursion only changes the control flow.", "Bonus Test 1 · P9g"),
 it("The runtime of MERGE is O(n).", "True", "One pass over both halves, one comparison per output element.", "Bonus Test 1 · P9q"),
 it("The runtime of MaxHeapify is Θ(n log n).", "False", "It sifts down a single root-to-leaf path: Θ(log n). Build-Heap is the O(n) one.", "Bonus Test 1 · P9r"),
 it("Stable (or easily made stable): InsertionSort", "True", "It shifts only strictly-greater elements, so equal keys keep their order.", "Bonus Test 1 · P9o"),
 it("Stable (or easily made stable): MergeSort", "True", "Ties are broken in favour of the left run during MERGE.", "Bonus Test 1 · P9o"),
 it("Stable (or easily made stable): HeapSort", "False", "Sift-down swaps far-apart elements, destroying the order of equal keys.", "Bonus Test 1 · P9o"),
 it("In-place (or easily made in-place): InsertionSort", "True", "Sorts within the array using O(1) extra space.", "Bonus Test 1 · P9p"),
 it("In-place (or easily made in-place): MergeSort", "False", "MERGE needs an O(n) auxiliary buffer.", "Bonus Test 1 · P9p"),
 it("In-place (or easily made in-place): HeapSort", "True", "The heap lives in the array itself; it only swaps.", "Bonus Test 1 · P9p"),
 it("In QuickSort, always using the last element of the sub-array as pivot gives worst-case recursion depth Θ(log n).", "False", "On already-sorted input the split is 0 / n−1, so the depth is Θ(n).", "Bonus Test 2 · P8c"),
 it("BucketSort runs in expected linear time if the input has uniform distribution.", "True", "Uniform keys give ~1 element per bucket, so per-bucket sorting is O(1) expected.", "Bonus Test 2 · P8d"),
 it("BucketSort can sort an arbitrary collection of numbers in O(n) time.", "False", "Without uniformity every key can land in one bucket → Θ(n²).", "Retake · P10d"),
 it("Any comparison-based sorting algorithm requires Ω(n lg n) time for input size n.", "True", "A decision tree with n! leaves has height ≥ lg(n!) = Ω(n lg n).", "Short test 1 · P8f"),
 it("Counting sort is stable.", "True", "Scanning the input right-to-left while decrementing counts preserves order.", "Bonus Test 2 · P8j"),
 it("Sorting an array of n integers in the range [0, n²−1] runs in Ω(n lg n) time.", "False", "Radix sort in base n does it in O(n); the bound only binds comparison sorts.", "Bonus Test 2 · P8l"),
 it("The minimum, maximum, and median elements can be found in Θ(n) time.", "True", "Min/max by a scan; median by SELECT (median-of-medians) in linear time.", "Bonus Test 2 · P8e"),
 it("2(n−1) is the lower bound for the comparisons needed to find both the min and max of n distinct integers.", "False", "Pairing elements first needs only ⌈3n/2⌉−2, which is fewer.", "Bonus Test 2 · P8k"),
])

topic("Heaps", TF, [
 it("There exists a heap T storing seven distinct elements whose rLR traversal yields them in sorted order.", "True", "rLR visits right subtree, then left, then root — a suitable max-heap makes that increasing.", "Bonus Test 1 · P9a"),
 it("The sequence [23,17,14,6,13,10,1,5,7,12] is a max-heap.", "False", "A[4]=6 has child A[9]=7, so a parent is smaller than its child.", "Short test 1 · P8i"),
 it("A min-heap can be represented by an array.", "True", "It is a complete tree, so children of i sit at 2i and 2i+1.", "Retake · P10l"),
 it("An array sorted in decreasing order is a min-heap.", "False", "Decreasing order is a max-heap; a min-heap needs parent ≤ children.", "Final Exam · P13l"),
])

topic("Heap sizes", None, [
 it("What is the height h of a heap of size n?", "⌊log n⌋", "Halving the index from n up to the root takes ⌊lg n⌋ steps.",
    "Short test 1 · P7a", ["2ⁿ", "n", "⌊n/2⌋", "⌊log n⌋"]),
 it("What is the largest size n for a heap with height h?", "2^(h+1) − 1", "Every level 0..h is completely filled.",
    "Short test 1 · P7b", ["2ʰ", "2^(h+1) − 1", "2h − 1", "⌊log h⌋ + 1"]),
 it("What is the smallest size n for a heap with height h?", "2ʰ", "Levels 0..h−1 full (2ʰ−1 nodes) plus a single node on level h.",
    "Short test 1 · P7c", ["2ʰ", "h", "h²", "2^(h+1) − 1"]),
])

topic("Trees", TF, [
 it("A full binary tree is complete.", "False", "Full only means every node has 0 or 2 children — the leaves may sit at different depths.", "Bonus Test 2 · P8a"),
 it("A complete binary tree is full.", "True", "With every level filled, every internal node has exactly two children.", "Bonus Test 2 · P8b"),
 it("Given the sequence (v₁,…,vₙ) of a binary tree traversal by LrR, one can reconstruct the exact structure of the tree.", "False", "Inorder alone is ambiguous — many shapes give the same sequence. You need a second traversal.", "Retake · P10g"),
])

topic("Tree Traversals", TRAV, [
 it("{C, B, D, A, F, E, H, G, I}", "Inorder", "Whole left subtree, then the root A, then the right subtree.", "Bonus Test 2 · P9a"),
 it("{H, D, B, E, F, I, C, G, A}", "None of the above", "It matches no pre-, post- or in-order walk of this tree.", "Bonus Test 2 · P9b"),
 it("{A, B, C, D, E, F, G, H, I}", "Preorder", "Root A first, then the left subtree, then the right.", "Bonus Test 2 · P9c"),
 it("{A, B, E, C, D, F, G, H, I}", "None of the above", "Starts like preorder but the sibling order is wrong.", "Bonus Test 2 · P9d"),
 it("{C, D, B, F, H, I, G, E, A}", "Postorder", "Both subtrees are emitted before the root A, which comes last.", "Bonus Test 2 · P9e"),
])

topic("Data Structure Operations", DS4, [
 it("PUSH in a stack", "O(1)", "Write at the top pointer.", "Retake · P1a"),
 it("ENQUEUE in a queue", "O(1)", "Append at the tail pointer.", "Retake · P1b"),
 it("APPEND in an unsorted array", "O(1)", "Write at the end — memory is assumed sufficient.", "Retake · P1c"),
 it("INSERT in a priority queue", "O(log n)", "Place at the end, then sift up one heap path.", "Retake · P1d"),
 it("FIND_MIN in a stack", "O(n)", "A stack keeps no order information, so every element must be scanned.", "Retake · P1e"),
 it("FIND_MIN in a queue", "O(n)", "A queue keeps no order information, so every element must be scanned.", "Retake · P1f"),
 it("INSERT at an arbitrary position in an unsorted array", "O(n)", "All following elements have to be shifted right.", "Retake · P1g"),
 it("FIND_MIN in a priority queue", "O(1)", "The minimum is simply the root of the min-heap.", "Retake · P1h"),
 it("POP in a stack", "O(1)", "Remove at the top pointer.", "Retake · P1i"),
 it("DEQUEUE in a queue", "O(1)", "Remove at the head pointer.", "Retake · P1j"),
 it("SEARCH in a sorted array", "O(log n)", "Binary search halves the range each step.", "Retake · P1k"),
 it("SEARCH in a priority queue", "O(n)", "Heap order says nothing about siblings, so an arbitrary key needs a full scan.", "Retake · P1l"),
])

topic("Linked Lists", TF, [
 it("ListSearch in a linked list runs in O(1) time.", "False", "There is no random access — you walk the list, O(n).", "Bonus Test 2 · P8f"),
 it("ListPrepend in a linked list runs in O(1) time.", "True", "Splice the new node in at the head pointer.", "Bonus Test 2 · P8g"),
 it("ListDelete in a singly linked list runs in O(1) time.", "False", "You need the predecessor to relink, and finding it costs O(n).", "Bonus Test 2 · P8h"),
 it("ListDelete in a doubly linked list runs in O(1) time.", "True", "The prev pointer lets you relink both neighbours directly.", "Bonus Test 2 · P8i"),
])

topic("Red-Black Trees & BST", TF, [
 it("Any BST storing n numbers can be transformed into any other BST with these n numbers using rotations.", "True", "Rotations can lift any key to the root, then recurse on the subtrees; O(n) rotations suffice.", "Bonus Test 3 · P8d"),
 it("It is possible that a leaf in a red-black tree is twice as deep as another leaf in the same tree.", "True", "Longest path (alternating red/black) is at most twice the shortest (all black) — 2× is attainable.", "Short test 3 · P8c"),
 it("It is possible that a leaf in a red-black tree is three times as deep as another leaf in the same tree.", "False", "The same 2× bound forbids any ratio beyond two.", "Bonus Test 3 · P9a"),
 it("Given a red-black tree with black-height k, the largest possible number of internal nodes is 2^(2k)−1.", "True", "Maximum height is 2k, so at most a full tree of that height.", "Bonus Test 3 · P9b"),
 it("Given a red-black tree with black-height k, the smallest possible number of internal nodes is 2k.", "False", "The minimum is 2ᵏ−1, given by the all-black tree of height k.", "Bonus Test 3 · P9c"),
 it("Given a red-black tree with black-height k≥2, the maximum ratio between two subtrees is Θ(2ᵏ).", "True", "One side can be all-black of height k while the other reaches height 2k using red nodes.", "Bonus Test 3 · P9d"),
 it("A red-black tree with more than 1 element built with RB-Insert contains at least one red node.", "True", "New nodes are inserted red, and with n>1 they cannot all be recoloured away.", "Bonus Test 3 · P9e"),
 it("The height of a node is the number of edges in a longest path to a leaf.", "True", "That is the standard definition of node height.", "Bonus Test 3 · P9f"),
 it("The black-height of a node x counts the black nodes including the sentinel nil[T] and x on a path from x to a leaf.", "False", "Black-height excludes x itself — it counts black nodes below x down to and including nil.", "Bonus Test 3 · P9g"),
 it("A red-black tree with n internal nodes has height ≤ 2·lg(n+1).", "True", "Black-height is ≥ h/2 and a tree of black-height b has ≥ 2^b − 1 internal nodes.", "Bonus Test 3 · P9h"),
 it("Some leaves of a red-black tree can be red.", "False", "All leaves are the nil sentinel, which is black by definition.", "Bonus Test 3 · P9i"),
 it("To save space, a single sentinel nil[T] can be used for all leaves.", "True", "The standard CLRS optimisation — one shared black sentinel node.", "Bonus Test 3 · P9j"),
 it("The root's parent is nil[T].", "True", "The same sentinel also serves as the parent of the root.", "Bonus Test 3 · P9k"),
 it("Deleting a black node requires no fix-up.", "False", "Removing a black node breaks the black-height invariant, so RB-Delete-Fixup must run.", "Bonus Test 3 · P9l"),
])

topic("BST Rotations", ROT5, [
 it("Maximum number of rotations needed to transform any BST on n vertices into any other BST?", "O(n)", "Rotate the first tree into a right spine (O(n)), then rotate down into the target (O(n)).", "Retake · P13b"),
])

topic("Hashing", None, [
 it("Uniform hash into 1..n — likelihood a new element x is assigned a particular index i?", "1 / n", "Uniform means each of the n slots is equally likely.",
    "Bonus Test 2 · P8m", ["1 / n", "n", "1 / i", "1 / C(n,2)"]),
 it("How many elements must be added to the hash table to ensure a collision?", "n + 1", "Pigeonhole principle: n slots but n+1 items.",
    "Bonus Test 2 · P8n", ["n", "n + 1", "2n", "2n + 1"]),
 it("With k unique elements already present and no collisions, likelihood the next insert causes a collision?", "k / n", "Exactly k of the n slots are occupied.",
    "Bonus Test 2 · P8o", ["1 / n", "n / k", "C(k,2)", "k / n"]),
])

topic("Dynamic Programming", TF, [
 it("The matrix-chain multiplication problem exhibits overlapping sub-problems.", "True", "The same subchain Aᵢ..Aⱼ is re-solved under many different split points.", "Bonus Test 3 · P8e"),
 it("The longest common subsequence problem exhibits the greedy-choice property.", "False", "A locally longest match can block a better global alignment, so LCS needs DP.", "Bonus Test 4 · P8j"),
 it("The longest path problem exhibits the optimal substructure property.", "False", "Subpaths of a longest path need not be longest, because vertices may not repeat.", "Short test 3 · P8h"),
 it("Every optimization problem can be solved optimally with dynamic programming.", "False", "DP needs optimal substructure and overlapping subproblems; many problems have neither.", "Short test 3 · P8j"),
 it("Matrix-Chain-Multiplication: any parenthesization of n elements has exactly n−1 pairs of parentheses.", "True", "Induction: multiplying n matrices takes n−1 multiplications and each contributes one pair. (n=3: ((A₁A₂)A₃) has 2.)", "Bonus Test 3 · P5b"),
])

topic("DP Properties", None, [
 it("Problems solvable by dynamic programming exhibit which two properties?", "Overlapping sub-problems + Optimal substructure",
    "Overlap is what makes memoisation pay off; optimal substructure is what makes the recurrence valid.",
    "Bonus Test 3 · P8a",
    ["Overlapping sub-problems + Optimal substructure", "Greedy-choice property + Optimal substructure",
     "Overlapping sub-problems + Independence of sub-problems", "Optimal substructure + Monotone substructure"]),
 it("The rod-cutting problem has which of the following properties?", "Overlapping sub-problems",
    "The same remaining length is re-solved after many different first cuts.",
    "Bonus Test 3 · P8b", ["Greedy-choice property", "Overlapping sub-problems", "Monotone substructure"]),
 it("The matrix-chain multiplication problem has which of the following properties?", "Optimal substructure",
    "An optimal parenthesization contains optimal parenthesizations of both of its subchains.",
    "Bonus Test 3 · P8c", ["Optimal substructure", "Monotone substructure", "Independence of sub-problems"]),
])

topic("Greedy, MST & Huffman", TF, [
 it("The binary tree corresponding to an optimal prefix code is full.", "True", "A node with a single child could be replaced by that child, shortening every code below it.", "Bonus Test 4 · P8a"),
 it("Every graph has a unique MST.", "False", "Equal edge weights allow several distinct minimum spanning trees.", "Bonus Test 4 · P8b"),
 it("Prim's algorithm is an instance of GenericMST.", "True", "It repeatedly adds a safe edge crossing the cut (tree, rest).", "Bonus Test 4 · P8c"),
 it("Kruskal's algorithm is an instance of GenericMST.", "True", "It repeatedly adds the lightest safe edge joining two components.", "Bonus Test 4 · P8d"),
 it("The greedy algorithm for computing change with coins (25,10,5,1) is optimal.", "True", "The US system is canonical, so greedy provably matches the optimum.", "Bonus Test 4 · P8e"),
 it("The greedy algorithm for computing change with coins (30,24,12,6) is optimal.", "False", "For 48 greedy gives 30+12+6 = 3 coins, but 24+24 = 2 coins is better.", "Bonus Test 4 · P8f"),
 it("The greedy algorithm for computing change with coins (27,9,3,1) is optimal.", "True", "Each coin is a multiple of the next (powers of 3), which makes greedy optimal.", "Bonus Test 4 · P8g"),
 it("Huffman's algorithm creates an optimal prefix code.", "True", "Exchange argument: merging the two least frequent symbols is always a safe choice.", "Bonus Test 4 · P8h"),
 it("The Shannon-Fano algorithm creates an optimal prefix code.", "False", "Top-down splitting can be suboptimal; only Huffman's bottom-up merge guarantees optimality.", "Bonus Test 4 · P8i"),
 it("If all edges in a graph have unique weights, then there is a unique MST.", "True", "The cut and cycle properties then force a single choice at every step.", "Retake · P10j"),
 it("If all edges in a graph have unique weights, then there is a unique NST (next-to-best spanning tree).", "False", "Distinct edge weights do not stop two different swaps from tying for second best.", "Final Exam · P13k"),
 it("Given G=(V,E), any tree T=(V,E*) with E*⊆E is a minimum spanning tree of G.", "False", "It is a spanning tree, but nothing forces its total weight to be minimum.", "Retake · P10c"),
 it("If an edge is the unique lightest edge crossing some cut of a connected undirected graph, it belongs to every MST.", "True", "Cut property — swapping it into any tree without it strictly reduces the weight.", "Short test 5 · P9c"),
 it("The lower bound for computing the Convex Hull of n points is Ω(n lg n).", "True", "Sorting reduces to convex hull, so the sorting bound carries over.", "Short test 3 · P8e"),
])

topic("Disjoint Sets", TF, [
 it("MakeSet(x) runs in O(1) time.", "True", "It just creates a one-element list with x as its own representative.", "Bonus Test 4 · P8k"),
 it("Union(x,y) runs in O(1) time.", "False", "Appending one list to the other must update the representative pointer of every element moved.", "Bonus Test 4 · P8l"),
 it("FindSet(x) runs in O(1) time.", "True", "Each element stores a direct pointer to its set representative.", "Bonus Test 4 · P8m"),
 it("A sequence of m MakeSet/Union/FindSet operations, n of which are MakeSet, takes O(m + n lg n) time.", "True", "With weighted union each element's representative is updated at most lg n times.", "Bonus Test 4 · P8n"),
])

topic("Algorithmic Paradigms", PARA3, [
 it("SelectionSort", "Incremental", "It grows a sorted prefix one element at a time.", "Bonus Test 1 · P5a"),
 it("QuickSort", "Divide-and-Conquer", "Partition splits the array, then it recurses on both sides.", "Bonus Test 1 · P5b"),
 it("InsertionSort", "Incremental", "Each new element is inserted into the already-sorted prefix.", "Bonus Test 1 · P5c"),
 it("MergeSort", "Divide-and-Conquer", "Split in half, sort each half, then merge.", "Bonus Test 1 · P5d"),
 it("Partition", "Other", "A single linear rearrangement pass — neither recursive nor prefix-growing.", "Bonus Test 1 · P5e"),
 it("Binary Search", "Divide-and-Conquer", "It discards half of the search range at every step.", "Bonus Test 1 · P5f"),
])

topic("Algorithm Types", TYPE3, [
 it("Tarjan's Select", "Divide & Conquer", "Median-of-medians splits into groups of 5 and recurses on one side.", "Retake · P4d"),
 it("Fractional Knapsack (thief with fractions of items)", "Greedy", "Taking the best value/weight ratio first is provably safe.", "Bonus Test 4 · P9b"),
 it("0-1 Knapsack (thief with whole items)", "Dynamic Programming", "Indivisible items break the greedy choice, so you need a table over capacity.", "Bonus Test 4 · P9c"),
 it("Optimal Activity Scheduling", "Greedy", "Always picking the earliest finishing time is a safe choice.", "Bonus Test 4 · P9d"),
 it("Shannon-Fano Encoding", "Divide & Conquer", "It recursively splits the symbol set into halves of near-equal probability.", "Bonus Test 4 · P9e"),
 it("Huffman Encoding", "Greedy", "It repeatedly merges the two least frequent nodes.", "Bonus Test 4 · P9f"),
 it("Optimal Rod Cutting", "Dynamic Programming", "Overlapping subproblems on the remaining rod length.", "Bonus Test 4 · P9g"),
 it("Prim's Algorithm", "Greedy", "It always adds the lightest edge leaving the current tree.", "Bonus Test 4 · P9h"),
 it("Kruskal's Algorithm", "Greedy", "It always adds the lightest edge that joins two components.", "Bonus Test 4 · P9i"),
 it("Optimal Matrix Chain Order", "Dynamic Programming", "A table m[i,j] over all subchains, reusing shared subproblems.", "Final Exam · P7h"),
 it("Dijkstra's Algorithm", "Greedy", "It always finalises the closest unvisited vertex.", "Final Exam · P7i"),
 it("Longest Common Subsequence", "Dynamic Programming", "A table c[i,j] over all prefix pairs.", "Retake · P4g"),
 it("Optimal Polygon Triangulation", "Dynamic Programming", "Same recurrence shape as matrix-chain multiplication.", "Retake · P4h"),
])

topic("Complexity Bounds", CB, [
 it("Optimal Rod Cutting", "O(n²)", "n subproblems, each trying up to n first cuts.", "Bonus Test 3 · P6d"),
 it("Longest Common Subsequence", "O(n²)", "Fill an n×m table with O(1) work per cell.", "Bonus Test 3 · P6e"),
 it("Multiplying two n×n matrices", "O(n³)", "The classical triple loop (ignoring Strassen).", "Bonus Test 3 · P6f"),
 it("Optimal Matrix Chain Multiplication", "O(n³)", "O(n²) table entries, each scanning O(n) split points.", "Bonus Test 3 · P6g"),
 it("Enumerating all Rod Cutting solutions", "O(2ⁿ)", "Each of the n−1 cut positions is independently in or out.", "Bonus Test 3 · P6h"),
 it("Huffman's Algorithm", "O(n lg n)", "n−1 merges, each doing two extract-mins on a heap.", "Bonus Test 4 · P6a"),
 it("Optimal Activity Selection (input already sorted by finish time)", "O(n)", "A single greedy scan once the sorting is given.", "Bonus Test 4 · P6b"),
 it("Optimal Polygon Triangulation", "O(n³)", "Same DP shape as matrix-chain: O(n²) entries × O(n) splits.", "Bonus Test 4 · P6c"),
 it("Longest Palindromic Subsequence", "O(n²)", "It is the LCS of the string with its own reverse.", "Bonus Test 4 · P6d"),
 it("Minimum number of points so every interval contains at least one point", "O(n lg n)", "Sort by right endpoint, then one greedy scan.", "Bonus Test 4 · P6e"),
 it("Minimum Water Stops", "O(n)", "One greedy pass over the stops, taking the farthest reachable each time.", "Bonus Test 4 · P6f"),
])

topic("Complexity — Search", CA, [
 it("FIND in a BST", "O(n)", "An unbalanced BST can degenerate into a path.", "Bonus Test 3 · P6a"),
 it("FIND in a Red-Black tree", "O(lg n)", "The height is bounded by 2·lg(n+1).", "Bonus Test 3 · P6b"),
 it("DELETE in a Red-Black tree, given a pointer to the node", "O(lg n)", "Splice the node out, then O(log n) fix-up rotations and recolourings.", "Bonus Test 3 · P6c"),
])

topic("Complexity — Graphs", CR, [
 it("Tarjan's Select", "O(n)", "Median-of-medians selection runs in worst-case linear time.", "Retake · P9a"),
 it("Topological Sort", "O(n²)", "Θ(V+E), and expressed in n alone E = O(n²).", "Retake · P9b"),
 it("Depth-first Search", "O(n²)", "Θ(V+E), and expressed in n alone E = O(n²).", "Retake · P9c"),
 it("Find Longest Path", "O(n!)", "NP-hard — brute force enumerates vertex orderings.", "Retake · P9d"),
 it("Multiply an n×n matrix by an n×n matrix", "O(n³)", "The classical triple loop.", "Retake · P9e"),
 it("Mergesort", "O(n lg n)", "T(n) = 2T(n/2) + n.", "Retake · P9f"),
 it("Quicksort", "O(n²)", "Worst case when the pivot always splits 0 / n−1.", "Retake · P9g"),
 it("Single-source Shortest Path in an unweighted graph", "O(n²)", "BFS is Θ(V+E), and E = O(n²) in terms of n.", "Retake · P9h"),
 it("Single-source Shortest Path in a weighted graph", "O(n² lg n)", "Dijkstra with a binary heap is O((V+E)·lg V).", "Retake · P9i"),
 it("Floyd-Warshall Algorithm", "O(n³)", "A triple loop over all intermediate vertices.", "Retake · P9j"),
])

topic("Graphs", TF, [
 it("A DAG has no cycles.", "True", "Directed Acyclic Graph — acyclic is part of the definition.", "Retake · P10a"),
 it("The union of all unique shortest paths from a single source in a positively weighted, connected, undirected graph is a tree.", "True", "Unique shortest paths give every vertex exactly one parent — a shortest-path tree.", "Retake · P10b"),
 it("The union of all shortest paths (source fixed) in an undirected graph is an MST.", "False", "A shortest-path tree minimises distance from s, not the total edge weight.", "Short test 5 · P9h"),
 it("An Eulerian cycle of a connected graph can be found in polynomial time.", "True", "It exists iff every degree is even, and Hierholzer's algorithm builds one in O(E).", "Retake · P10e"),
 it("A Hamiltonian cycle of a connected graph can be found in polynomial time.", "False", "Hamiltonian cycle is NP-complete — no polynomial algorithm is known.", "Final Exam · P13e"),
 it("If all edges in a graph have the same weight, then BFS computes the single-source shortest path.", "True", "With equal weights, fewest edges is the same as shortest distance.", "Retake · P10i"),
 it("If all edges have the same weight in a connected undirected graph, BFS produces an MST.", "True", "When all weights are equal every spanning tree has the same total weight, so any is minimum.", "Short test 5 · P9a"),
 it("The PageRank of an n-vertex graph is an n×n matrix.", "False", "PageRank is a vector of n probabilities; it is the transition matrix that is n×n.", "Retake · P10k"),
 it("When adding an edge to a directed graph, the number of SCCs can decrease.", "True", "A new edge can close a cycle and merge several components into one.", "Retake · P10m"),
 it("When adding an edge to a directed graph, the number of SCCs can increase.", "False", "Adding edges never splits an existing strongly connected component.", "Final Exam · P13m"),
 it("When adding an edge to a directed graph, the number of SCCs can stay the same.", "True", "An edge inside an existing SCC, or one that closes no new cycle, changes nothing.", "Short test 5 · P9f"),
 it("When adding an edge to a directed graph, the number of SCCs decreases by at most 1.", "False", "One edge closing a long chain of SCCs into a cycle can merge many at once.", "Short test 5 · P9g"),
 it("The Vertex Cover algorithm that computes a matching is a 2-approximation.", "True", "Taking both endpoints of each matching edge is ≤ 2×, since OPT needs ≥1 endpoint per edge.", "Final Exam · P13a"),
 it("Every computational problem can be solved in a finite amount of time.", "False", "The halting problem is undecidable.", "Final Exam · P13c"),
 it("Every problem in the class NP can be verified in polynomial time.", "True", "That is precisely the definition of NP.", "Final Exam · P13d"),
])

topic("Shortest Paths", TF, [
 it("Dijkstra solves the SSSP problem on weighted graphs, even with some negative edge weights.", "False", "A vertex finalised early can still be improved later by a negative edge.", "Retake · P10n"),
 it("Dijkstra can solve SSSP with negative weights if k+1 is added to every edge (−k = most negative weight).", "False", "Adding a constant per edge penalises paths with more edges, changing which path is shortest.", "Short test 5 · P9j"),
 it("Given a weighted DAG, running BFS and relaxing all outgoing edges of v when v is dequeued correctly computes SSSP.", "False", "BFS dequeues in hop-count order, which is not a topological order.", "Short test 5 · P9d"),
 it("For all (u,v)∈E: δ(s,v) < δ(s,u) + w(u,v).", "False", "The triangle inequality is stated with ≤; equality holds along a shortest path.", "Final Exam · P10a"),
 it("If δ(s,v) = ∞, then d[v] = ∞ always.", "True", "No-path property — relaxation can never produce a finite estimate for an unreachable vertex.", "Final Exam · P10b"),
 it("d[v] ≤ δ(s,v) for all v, and once d[v] = δ(s,v) it never changes.", "False", "The upper-bound property runs the other way: d[v] ≥ δ(s,v) at all times.", "Final Exam · P10c"),
 it("If s⇝u followed by edge (u,v) is a shortest path and d[u]=δ(s,u), then after Relax(u,v,w) we have d[v]=δ(s,v).", "True", "The convergence property — relaxing the final edge with a correct d[u] settles v.", "Final Exam · P10d"),
 it("If p=⟨v₀,…,vₖ⟩ is a shortest path and we relax (v₀,v₁),…,(vₖ₋₁,vₖ) in order, even intermixed with other relaxations, then d[vₖ]=δ(s,vₖ).", "True", "The path-relaxation property — order along the path is all that matters.", "Final Exam · P10e"),
])

topic("DFS Edge Types", CASE3, [
 it("Tree edge u→v satisfies which case of the DFS theorem?", "Case 2", "v is first discovered from u, so v's interval nests inside u's.", "Retake · P7a"),
 it("Back edge u→v satisfies which case of the DFS theorem?", "Case 3", "v is an ancestor of u, so u's interval nests inside v's.", "Retake · P7b"),
 it("Forward edge u→v satisfies which case of the DFS theorem?", "Case 2", "v is a descendant of u already finished — still nested inside u's interval.", "Retake · P7c"),
 it("Cross edge u→v satisfies which case of the DFS theorem?", "Case 1", "The two intervals are disjoint and neither vertex is an ancestor of the other.", "Retake · P7d"),
])

topic("Graph Figures", None, [
 it("For exactly what values of y is there a YES answer to “Does G have a Vertex Cover of size y?”", "≥ 5",
    "A minimum vertex cover of this graph has size 5, and any superset of a cover is still a cover — so YES exactly for y ≥ 5.",
    "Retake · P5b", ["≥ 3", "≥ 4", "≥ 5", "≥ 6"], "fig-retake-p5"),
 it("How many strongly connected components are there in G?", "5",
    "The SCCs are {r}, {u}, {q,t,y}, {x,z} and {s,v,w} — five in total.",
    "Retake · P11b", ["1", "2", "3", "4", "5", "6", "7", "8"], "fig-retake-p11"),
])

# ---------------- emit JS ----------------
def js(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

out = ["const CONCEPTS=["]
total = 0
seen = {}
for name, opts, items in T:
    o = ("opts:[" + ",".join(js(x) for x in opts) + "],") if opts else ""
    out.append(" {topic:%s,%sitems:[" % (js(name), o))
    for (q, a, why, src, ov, fig) in items:
        key = (" ".join(q.split()), tuple(ov or opts or []))
        if key in seen:
            raise SystemExit("DUPLICATE question: %r (also in %s)" % (q, seen[key]))
        seen[key] = name
        if not (ov or opts) or a not in (ov or opts):
            raise SystemExit("answer not among options: %r -> %r" % (q, a))
        row = "  [" + js(q) + "," + js(a) + "," + js(why) + ","
        row += ("[" + ",".join(js(x) for x in ov) + "]" if ov else "null") + ","
        row += js(src) + "," + (js(fig) if fig else "null") + "],"
        out.append(row); total += 1
    out.append(" ]},")
out.append("];")
open("_concepts.js", "w", encoding="utf-8").write("\n".join(out))
print("topics:", len(T), "questions:", total)
