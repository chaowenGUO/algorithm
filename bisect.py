def bisect(nums, target, compare):
    left, right = 0, len(nums)
    while left != right:
        middle = left + (right - left) // 2
        if compare(nums[middle], target): left = middle + 1
        else: right = middle
    return left
    
bisect_lower = functools.partial(bisect, compare=operator.lt)
bisect_upper = functools.partial(bisect, compare=operator.le)
bisect_lower_reverse = functools.partial(bisect, compare=operator.ge) - 1
bisect_upper_reverse = functools.partial(bisect, compare=operator.gt) - 1
