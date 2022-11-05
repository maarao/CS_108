def merge(alist, blist):

def mergesort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist)//2
    return merge(mergesort(alist[:mid]), mergesort(mid:))