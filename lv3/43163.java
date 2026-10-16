import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int[] route = new int[words.length];
        ArrayDeque<int[]> q = new ArrayDeque<>();

        int found = -1;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(target)) {
                found = i;
            }
            if (oneDiff(begin, words[i])) {
                q.offer(new int[] { i, 1 });
                route[i] = 1;
            }
        }
        if (found == -1) {
            return 0;
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int idx = cur[0];
            int cnt = cur[1];
            for (int nxt = 0; nxt < words.length; nxt++) {
                if (!words[idx].equals(words[nxt]) && oneDiff(words[idx], words[nxt]) && route[nxt] == 0) {
                    q.offer(new int[] { nxt, cnt + 1 });
                    route[nxt] = cnt + 1;
                }
            }
        }

        return route[found];
    }

    public boolean oneDiff(String a, String b) {
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                diff++;
            }
        }
        return diff == 1;
    }
}
