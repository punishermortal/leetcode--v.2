class Solution {
    fun findChampion(n: Int, edges: Array<IntArray>): Int {
        val isLoser = BooleanArray(n)
        var countLosers = 0
        
        for ((a, b) in edges) {
            if (isLoser[b]) continue
            isLoser[b] = true
            countLosers += 1
        }
        
        return if (countLosers < n - 1) -1 else (isLoser.withIndex().find { !it.value }?.index ?: -1)
    }
}