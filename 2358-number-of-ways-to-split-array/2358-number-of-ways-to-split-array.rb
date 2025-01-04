def ways_to_split_array(nums)
    sum = nums.sum
    ps = 0
    nums.count {|v| 
        ps += v
        ps >= (sum - ps)
    } - (sum.negative? ? 0 : 1)
end