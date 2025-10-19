def is_green(nums, mid, t):
    return nums[mid] >= t

def b_search(nums, t):
    l = -1
    r = len(nums)
    while l + 1 < r:
        mid = (l + r) // 2
        if is_green(nums, mid, t):
            r = mid
        else:
            l = mid
    return r

if __name__ == "__main__":
    v = [1, 2, 3, 4, 6, 7, 8, 9, 9, 11]
    print(f"≥ -1的最小值的下标是：{b_search(v, -1)}")
    print(f"≥ 5的最小值的下标是：{b_search(v, 5)}")
    print(f"≥ 9的最小值的下标是：{b_search(v, 9)}")
    print(f"≥ 12的最小值的下标是：{b_search(v, 12)}")