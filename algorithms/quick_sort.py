def quick_sort(li):
    # 分片处理
    def divide(start, end):
        if end > start:
            pivot = get_pivot(start, end)
            divide(start, pivot - 1)
            divide(pivot + 1, end)

    # 一趟快排
    def get_pivot(start, end):
        pivot_value = li[start]
        while start < end:
            while start < end and li[end] >= pivot_value:
                end -= 1
            li[start] = li[end]
            while start < end and li[start] <= pivot_value:
                start += 1
            li[end] = li[start]
        li[start] = pivot_value
        return start

    divide(0, len(li) - 1)


if __name__ == "__main__":
    li = [3, 4, 9, 1, 5, 2, 6]
    quick_sort(li)
    print(li)
