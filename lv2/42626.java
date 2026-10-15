import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Long> heap = new PriorityQueue<>();
        for (long s : scoville) {
            heap.offer(s);
        }

        int count = 0;
        while (heap.peek() < K) {
            if (heap.size() < 2) {
                return -1;
            }
            long a = heap.poll();
            long b = heap.poll();
            heap.offer(a + 2L * b);
            count++;
        }
        return count;
    }
}
