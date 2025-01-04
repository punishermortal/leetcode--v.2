def count_palindromic_subsequence s
    s = s.bytes
    g = s.size.times.group_by { s[_1] } .values
    r = 0
    for v in g
        f, l = v.first, v.last
        next if l - f < 2
        for m in g
            x = m.bsearch { _1 > f }
            r += 1 if x && x < l
        end
    end
    r
end