import random, time

#query() takes in a 3d list of documents, a list of all tags, and a subset of the total tag list
#returns a list of documents whose tags form a subset of the smaller tag list
def query(document_list, all_tags, tags_list):

    #Final list created that will store all documents whose tags form a subset of the smaller tag list
    final_list = []
    
    #Loops through every document
    for item in document_list:

        #count variable starts at 0 for each document and increases by 1 for each tag that is in the tag list being searched
        count = 0

        #Loops through every tag in a document, and checks to see if it is in the tag list
        for doc_tag in item[1]:
            for tags in tags_list:
                if (doc_tag==tags):
                    count = count + 1

        #If every tag on a document was in the tag list, then the document is appended to the final document list
        if count == len(item[1]):
            final_list.append(item)

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