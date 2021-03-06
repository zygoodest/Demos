"""
大顶堆：
    每个节点的值都大于等于其左右子节点的值
    的完全二叉树

小顶堆：
    每个节点的值都小于等于其左右子节点的值
    的完全二叉树

完全二叉树：
    除最后一层外，其他各层的节点数都达到最大值
    且最后一层的节点都连续集中在最左边

堆排序：
    利用堆数据结构设计的排序算法
    大顶堆用于升序排序
    小顶堆用于降序排序

堆的用途：
    1.排序算法的一种，也是稳定效率最高的一种
    2.可用于实现优先队列

堆的特点：
    1.以数组的方式存储，节约空间
    2.堆中不需要整棵树都是有序的，所以堆平衡不是问题
    3.在二叉树中搜索很快，但在堆中会很慢
    不过堆中的搜索不是第一优先级
    堆的目的是将最大或最小的节点放到最前面
    从而快速进行相关插入、删除操作
"""
