class Solution {
    public long solution(int n, int[] times) {
        long minTime = 1000000001;
        for (long t : times) {
            minTime = Math.min(minTime, t);
        }

        long lo = 1;
        long hi = minTime * n * 1L;

        while (lo < hi) {
            long mid = (lo + hi) / 2;
            long done = 0;
            for (long t : times) {
                done += mid / t;
            }
            if (done >= n) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }

        return lo;
    }
}
