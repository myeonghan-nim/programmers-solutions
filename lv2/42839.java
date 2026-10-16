import java.util.*;

class Solution {
    public int solution(String numbers) {
        HashSet<Integer> set = new HashSet<>();
        boolean[] checked = new boolean[numbers.length()];
        check(0, "", numbers.toCharArray(), set, checked);

        int ans = 0;
        for (int n : set) {
            if (isPrime(n)) {
                ans++;
            }
        }
        return ans;
    }

    public void check(int depth, String number, char[] numbers, HashSet set,
            boolean[] checked) {
        if (depth == numbers.length) {
            return;
        }

        for (int nxt = 0; nxt < numbers.length; nxt++) {
            if (!checked[nxt]) {
                checked[nxt] = true;
                int intNumber = Integer.parseInt(number + numbers[nxt]);
                set.add(intNumber);
                check(depth + 1, number + numbers[nxt], numbers, set, checked);
                checked[nxt] = false;
            }
        }
    }

    public boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int d = 2; d * d <= n; d++) {
            if (n % d == 0) {
                return false;
            }
        }
        return true;
    }
}
