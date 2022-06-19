def binary_search(list,target):
    first=0
    last=len(list)-1

    while first<=last:
        mid_point=(first+last)//2

        if list[mid_point]==target:
            return mid_point
        elif list[mid_point]<target:
            first=mid_point+1
        else:
            last=mid_point-1
    return None

def recursive_binary_search(list,target):
    if not len(list):
        return False
    else:
        mid_point=len(list)//2
    if list[mid_point]==target:
        return True
    elif list[mid_point]<target:
        return recursive_binary_search(list[mid_point+1:],target)
    else:
        return recursive_binary_search(list[:mid_point],target)