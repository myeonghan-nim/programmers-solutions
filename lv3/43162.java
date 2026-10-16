import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        boolean[] visited = new boolean[n];
        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            answer++;
            ArrayDeque<Integer> queue = new ArrayDeque<>();
            queue.offer(i);
            visited[i] = true;
            while (!queue.isEmpty()) {
                int cur = queue.poll();
                for (int nxt = 0; nxt < n; nxt++) {
                    if (computers[cur][nxt] == 1 && !visited[nxt]) {
                        visited[nxt] = true;
                        queue.offer(nxt);
                    }
                }
            }
        }
        return answer;
    }
}
