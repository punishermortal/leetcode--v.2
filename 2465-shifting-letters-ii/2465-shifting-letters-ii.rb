# @param {String} s
# @param {Integer[][]} shifts
# @return {String}
def shifting_letters(s, shifts)
  n = s.size
  prefix_sum = Array.new(n + 1, 0)
  shifts.each do |s, e, d|
    addition = d == 0 ? -1 : 1
    prefix_sum[s] += addition
    prefix_sum[e + 1] -= addition
  end

  1.upto(n) do |i|
    prefix_sum[i] += prefix_sum[i - 1]
  end

  s.chars.map.with_index do |char, i|
    shift_char(char, prefix_sum[i])
  end.join
end

def shift_char(char, shift)
  ((char.ord - 'a'.ord + shift) % 26 + 'a'.ord).chr
end