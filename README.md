# Tagged-Document-Lookup

In this repo are two python files and a pdf: Tag_Problem_Brute_Force.py, Tag_Problem_Optimization.py, and Prime_Factorization_Proof.pdf

My brute force solution to the Tagged Document Lookup problem is as simple as iterating through the list of documents and checking if all of its tags are elements of the larger set of tags in question. For each document, each tag is compared with every element of the larger set of tags, and if they are all found to be elements of the larger set of tags, then the document is added to a list that is returned at the end of the function.

My optimized solution to the Tagged Document Lookup problem involves representing tags as unique prime numbers. This way, determining whether or not a document's tags are a subset of a larger set of tags is as simple as checking if the product of the document's tags evenly divides the product of the larger set of tags. A detailed proof outlining why this relationship is true can be found in this repo titled "Prime_Factorization_Proof". So, for each document, its tags are multiplied together, and if it divides the product of the larger set of tags, the document is added to a list that is returned at the end of the function.

If we let the number of documents be "n", the number of tags in a document be "m", and the number of tags in the subset be "k", then we see that the brute force method runs in O(n * m * k) time, while the optimized solution runs in O((n * m) + k) time, which reduces to O(n * m) time. In the specific example where the number of documents is 10,000, the number of tags per document is 7, and the number of tags in the subset is 40, the optimized solution runs around 7-10 times faster.
