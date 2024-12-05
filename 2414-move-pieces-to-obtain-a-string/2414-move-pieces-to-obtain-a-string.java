public class Solution {

    public boolean canChange(String start, String target) {
        int startLength = start.length();
        
        int startIndex = 0, targetIndex = 0;

        while (startIndex < startLength || targetIndex < startLength) {
        
            while (
                startIndex < startLength && start.charAt(startIndex) == '_'
            ) {
                startIndex++;
            }

            while (
                targetIndex < startLength && target.charAt(targetIndex) == '_'
            ) {
                targetIndex++;
            }

            if (startIndex == startLength || targetIndex == startLength) {
                return startIndex == startLength && targetIndex == startLength;
            }
            if (
                 (start.charAt(startIndex) == 'L' && startIndex < targetIndex) ||
                 (start.charAt(startIndex) != target.charAt(targetIndex)) ||
                (start.charAt(startIndex) == 'R' && startIndex > targetIndex)
            ) return false;

            startIndex++;
            targetIndex++;
        }

        return true;
    }
}