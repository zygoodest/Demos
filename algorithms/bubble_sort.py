def bubble_sort(li):
    length = len(li)
    # 外层循环
    for i in range(length - 1):
        finish = True
        # 内层循环
        for j in range(length - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                finish = False
        if finish:
            break

if __name__ == "__main__":
    li = [2, 8, 3, 7, 5, 1]
    bubble_sort(li)
    print(li)
