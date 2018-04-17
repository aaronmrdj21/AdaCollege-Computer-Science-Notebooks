def insertionsort(A):
    for j in range(1,len(A)): #Begin loop of the second element as first one is already sorted. 
        key = A[j] #Next item to get sorted

        i = j-1 #Last item to compare
        #Key keeps decreasing as long as the item is smaller than the previous item in array
        while (i > -1) and key < A[i]: #if i == -1 indicates it should be at the front
            A[i+1]=A[i] #To move the last item compared forward to make space for key
            i=i-1 #Look at the item for next time
        #Otherwise i < key shows the key belongs to i+1
        A[i+1] = key
    return A



if __name__=="__main__":
    x = [5,2,4,6,1,3] #list of items to sort
    insertionsort(x) #run the code above 
    print(x) #print result
