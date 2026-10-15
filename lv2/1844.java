import java.util.ArrayDeque;

public class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int[][] dist = new int[n][m];
        dist[0][0] = 1;

        int[] dr = { 1, -1, 0, 0 };
        int[] dc = { 0, 0, 1, -1 };

        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] { 0, 0 });
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nr = cur[0] + dr[i];
                int nc = cur[1] + dc[i];
                if (0 <= nr && nr < n && 0 <= nc && nc < m && maps[nr][nc] == 1 && dist[nr][nc] == 0) {
                    dist[nr][nc] = dist[cur[0]][cur[1]] + 1;
                    queue.offer(new int[] { nr, nc });
                }
            }
        }

        if (dist[n - 1][m - 1] != 0) {
            return dist[n - 1][m - 1];
        }
        return -1;
    }
}
