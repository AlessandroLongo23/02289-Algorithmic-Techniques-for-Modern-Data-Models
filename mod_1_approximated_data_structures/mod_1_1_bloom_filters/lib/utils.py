import matplotlib.pyplot as plt
from lib.bloom_filter import BloomFilter
from sklearn.metrics import confusion_matrix

# function that receives two sets
# builds the two bloom filters from A and B and computes the estimated AND bloom filter with bitwise AND
# builds the true AND bloom filter from A\cap B
# finally, plots the confusion matrix between the true and estimated AND bloom filter
def confusion_matrix_AND(set1, set2, m, h):
    # build two bloom filters and add elements to them
    bf1 = BloomFilter(m, h)
    bf1.add_all(set1)

    bf2 = BloomFilter(m, h)
    bf2.add_all(set2)
    
    # compute the estimated AND bloom filter with bitwise AND
    estimated_bf_AND = bf1 & bf2

    # compute the true AND bloom filter from A\cap B
    true_bf_AND = BloomFilter(m, h)
    true_bf_AND.add_all(list(set(set1) & set(set2)))
    
    # compute the confusion matrix
    cf_matrix = confusion_matrix(true_bf_AND.bit_array, estimated_bf_AND.bit_array, labels=[False, True])
    
    # plot the confusion matrix with numbers in the cells
    plt.figure(figsize=(10, 7))
    plt.imshow(cf_matrix, cmap='Blues')
    for i in range(2):
        for j in range(2):
            plt.text(j, i, cf_matrix[i, j], ha='center', va='center', fontsize=24)
    plt.title('Confusion Matrix', fontsize=14)
    plt.xlabel('Estimated AND', fontsize=12)
    plt.ylabel('True AND', fontsize=12)
    plt.colorbar()
    plt.xticks([0, 1], ['False', 'True'], fontsize=12)
    plt.yticks([0, 1], ['False', 'True'], fontsize=12)
    plt.tight_layout()
    plt.show()