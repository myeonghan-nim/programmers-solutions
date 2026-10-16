class Solution {
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        return visit(0, k, dungeons, visited);
    }

    public int visit(int depth, int k, int[][] dungeons, boolean[] visited) {
        int best = depth;
        for (int nxt = 0; nxt < dungeons.length; nxt++) {
            if (k >= dungeons[nxt][0] && !visited[nxt]) {
                visited[nxt] = true;
                best = Math.max(best, visit(depth + 1, k - dungeons[nxt][1], dungeons, visited));
                visited[nxt] = false;
            }
        }
        return best;
    }
}
