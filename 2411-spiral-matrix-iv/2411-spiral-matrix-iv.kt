class Solution {
    fun spiralMatrix(m: Int, n: Int, head: ListNode?): Array<IntArray> {
        val result = Array(m) { IntArray(n) { -1 } }

        var direction = Direction.RIGHT
        var x = 0
        var y = 0
        var node = head

        while (node != null) {
            result[y][x] = node.`val`
            y += direction.dy
            x += direction.dx
            if (y < 0 || y >= m || x < 0 || x >= n || result[y][x] >= 0) {
                x -= direction.dx
                y -= direction.dy
                direction = direction.next()
                y += direction.dy
                x += direction.dx
            }
            node = node.next
        }
        return result
    }

    enum class Direction(val dx: Int, val dy: Int) {
        RIGHT(1, 0),
        DOWN(0, 1),
        LEFT(-1, 0),
        UP(0, -1);

        fun next(): Direction = items[(ordinal + 1) and 0x03]

        companion object {
            val items = Direction.values()
        }
    }
}