def inc_ind(vec,ind,flag):
    if flag == 1:        
        vec[ind] += 1        
    if vec[ind] == 10:
        vec[ind] = 0
        if ind ==0:
            vec.insert(0,1)
        else:
            vec[ind-1]+=1
    return vec

def add_last(vect):
    flag = 1
    i = len(vect) - 1    
    while i>=0:
        vect = inc_ind(vect,i,flag)
        flag = 0
        i -= 1

    return vect

##################################################################

def sorter(vec):
    for i in range(len(vec)):
        for i in range(len(vec)):
            if i == 0:
                continue
            elif vec[i] < vec[i-1]:
                a = vec[i]
                vec[i] = vec[i-1]
                vec[i-1] = a

def merger(vec1, m, vec2, n):
    if m==0:
        vec1 = [num for num in vec2 if num != 0]
    elif n==0:
        vec1 = [num for num in vec1 if num != 0]
    else:
        vec1 = [num for num in vec1 if num != 0]
        vec2 = [num for num in vec2 if num != 0]
        vec1 = vec1 + vec2
        sorter(vec1)

    return vec1

###################################################################

def search_insert(vec, tar):
    flag = 0 # This means the target is not present
    for i in range(len(vec)):
        if vec[i] == tar:
            flag = 1
            return i
        elif vec[i] > tar:
            flag = 0
            return i
        elif (i == len(vec)-1) and flag == 0:
            return i+1
        
###################################################################

def splitt(strg):
    ind = []
    for i in range(len(strg)):
        if strg[i] == " ":
            ind.append(i)

    words = []
    temp_str =[]
    for i in range(len(ind)):
        if i ==0:
            temp_str.append(strg[0:ind[i]])
        else:
            temp_str.append(strg[ind[i-1]:ind[i]])
    
    if strg[-1] != " ":
            temp_str.append(strg[ind[-1]:])
        

    return temp_str

##################################################################

def integ(lis,sample_time, initial_val):
    sum = initial_val
    nums = []
    for i in range(len(lis)):
        if i == 0:
            # sum = initial_val 
            nums.append(sum)
        else:
            sum = sum + (lis.iloc[i-1] +9.81)*sample_time
            nums.append(sum)

    return nums

###################################################################

