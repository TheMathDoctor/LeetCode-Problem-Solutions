def permutations(A):
    #assumes that all entries are unique
    #depth first search algorithm for computing permutations
    n = len(A)

    if n == 1:
        return [A]

    if n == 2:
        return [A,A[::-1]]
    permutations = []

    for i in range(n):
        #swap the i-th element with the 0-th element in the list
        temp = A[i]
        A[i] = A[0]
        A[0] = temp

        #compute permutations starting at the  1-st element
        sub_perms = permutations(A[1:n])
        for s in sub_perms:
            perm = s
            #appending is faster than prepending
            perm.append(A[0])
            permutations.append(perm)
            
    return permutations


    def permutations_ii(A):
        #same algorithm as before except we keep track of the elements
        #that have been the 0-th elements
        n = len(A)

        if n == 1:
            return [A]

        if n == 2:
            return [A] if A[0] == A[1] else [A,A[::-1]]

        permutations = []
        seen = []

        for i in range(n):
            if A[i] in seen:
                continue
            #swap i-th entry with #0-th entry
            temp = A[i]
            A[i] = A[0]
            A[0] = temp
            seen.append(temp)

            sub_perms = permutations_ii(A)
            for s in sub_perms:
                perm = s
                perm.append(A[0])
                permutations.append(perm)

        return permutations
