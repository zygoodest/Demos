def binary_search(li, item):

    def fun(start, end):
        if (end - start) <= 1:
            return -1
        
        mid = (start + end) // 2
        if li[mid] == item:
            return mid
        elif li[mid] > item:
            end = mid
        elif li[mid] < item:
            start = mid
        return fun(start, end)

    return fun(0, len(li))


if __name__ == "__main__":
    li = [1, 4, 6, 7, 9, 15]
    rst = binary_search(li, 7)
    print(rst)
