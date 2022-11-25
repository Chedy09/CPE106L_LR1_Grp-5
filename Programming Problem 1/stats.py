# function to find the median of array 
def median(a):
    a.sort()
    n=len(a)
    mid=int(n/2);
    print ("Median:")
    if(n%2==1):
        return a[mid]
    else:
        return (a[mid]+a[mid+1])/2

# function to find the mean of array    
def mean(a):
    n=len(a)
    sumofa=0
    print ("Mean:")
    for i in a:
        sumofa=sumofa+i;
    return sumofa/n

# function to find the mode of array 
def mode(a):
    res = max(set(a), key = a.count)
    print ("Mode:")
    return res

# here is the code to test:

# from stats import median,mode,mean 
a=[1,3,2,6,7,5,9,8,5,4]

print(median(a))
print(mean(a))
print(mode(a))
