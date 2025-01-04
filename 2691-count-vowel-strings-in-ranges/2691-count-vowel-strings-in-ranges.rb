# @param {String[]} words
# @param {Integer[][]} queries
# @return {Integer[]}
def vowel_strings(words, queries)
    vowels = Set.new(['a', 'e', 'i', 'o', 'u'])
    prefix_sum = Array.new(words.length + 1, 0)
    words.each_with_index do |word, i|
        if vowels.include?(word[0]) && vowels.include?(word[-1])
            prefix_sum[i + 1] = prefix_sum[i] + 1
        else
            prefix_sum[i + 1] = prefix_sum[i]
        end
    end
    result = queries.map do |l, r|
        prefix_sum[r + 1] - prefix_sum[l]
    end
    result
end