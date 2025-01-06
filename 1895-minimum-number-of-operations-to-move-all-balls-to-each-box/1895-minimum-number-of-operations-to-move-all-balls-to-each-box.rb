# @param {String} boxes
# @return {Integer[]}
def min_operations(boxes)
    answer = []
    i = 1
    balls = []
    boxes.each_char.with_index do |char, i|
        if char == "1"
            balls << i
        end
    end
    
    i = 0
    while i < boxes.size
        total = 0
        balls.each do |b_i|
            if i != b_i
                total += (i - b_i).abs
            end
        end

        answer << total
        i += 1
    end

    answer
end