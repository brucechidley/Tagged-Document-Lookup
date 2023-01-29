import random, time

#query() takes in a 3d list of documents, a list of all tags, and a subset of the total tag list
#returns a list of documents whose tags form a subset of the smaller tag list
def query(document_list, all_tags, tags_list):

    #Multiplies all tags in the size 40 tag list together
    tags_multiplied = 1
    for p in tags_list:
        tags_multiplied = tags_multiplied * p
    
    #Final list created that will store all documents whose tags form a subset of the smaller tag list
    final_list = []

    #Loops through all documents
    for l in document_list:

        document_tags_multiplied = 1

        #Multiplies all tags of a document together
        for j in l[1]:
            document_tags_multiplied = document_tags_multiplied * j

        #If the product of the document's tags evenly divides the product of the size 40 subset of tags, then its elements are a subset of the 40 tags
        if tags_multiplied % document_tags_multiplied == 0:
            final_list.append(l)

    return final_list

def main():
    #The prime number 2 is added to the list of primes manually
    primes = [2]

    i = 2
    #Loops until there are 100 (number can be changed) prime numbers in the primes list. These will represent the tags
    while len(primes) < 100:
        i = i + 1
        prime = True

        #Checks to see if any numbers less than the current number being checked divide it
        for k in range (2, i):
            if i%k == 0:
                prime = False
        if prime:
            primes.append(i)

    #Chooses a random length 40 (number can be changed) subset of the total list of 100 primes to represent the tag subset
    tags_picked_index = random.sample(range(100), 40)
    tags_picked = []
    for x in tags_picked_index:
        tags_picked.append(primes[x])

    #Document will take the form [[1, [p11, p12, ... , p17]], [2, [p21, p22, ..., p27]] ...] where p's represent tags
    documents = []

    #Creates 10 000 documents, each containing 7 values (number can be changed)
    for j in range (0, 10000):
        document_tags = random.sample(range(100), 7)

        #Appends random tags from the total tag list (called primes) to the document
        documents.append([j, [primes[document_tags[0]], primes[document_tags[1]], primes[document_tags[2]], 
                            primes[document_tags[3]], primes[document_tags[4]], primes[document_tags[5]], 
                            primes[document_tags[6]]]])

    #Runs the query function 50 times and records the average time it took to run
    total_time = 0
    for l in range (0, 50):
        start = time.time()
        final_documents_list = query(documents, primes, tags_picked)
        end = time.time()
        total_time = total_time + (end-start)
    
    #Prints the average time
    average_time = total_time / 50
    print("Average Time Taken: " + str(average_time))

    #Prints the last list of documents returned by the functions as well as the tag subset for manual verification
    print("List of Documents: " + str(final_documents_list))
    print("")
    print("Tag Subset: " + str(tags_picked))

main()