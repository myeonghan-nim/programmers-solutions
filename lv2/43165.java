public class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(0, 0, numbers, target);
    }

    public int dfs(int i, int cur, int[] numbers, int target) {
        if (i == numbers.length) {
            return cur == target ? 1 : 0;
        }
        return dfs(i + 1, cur + numbers[i], numbers, target) + dfs(i + 1, cur - numbers[i], numbers, target);
    }
}