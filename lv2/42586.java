import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> batches = new ArrayList<>();

        List<Integer> completed = new ArrayList<>();
        for (int i = 0; i < progresses.length; i++) {
            int remaining = 100 - progresses[i];
            int days = (remaining + speeds[i] - 1) / speeds[i];
            completed.add(days);
        }

        int deploymentDay = -1;
        int batchSize = 0;

        for (int i = 0; i < progresses.length; i++) {
            int remaining = 100 - progresses[i];
            int days = (remaining + speeds[i] - 1) / speeds[i];

            if (batchSize == 0) {
                deploymentDay = days;
                batchSize = 1;
            } else if (days <= deploymentDay) {
                batchSize++;
            } else {
                batches.add(batchSize);
                deploymentDay = days;
                batchSize = 1;
            }
        }

        if (batchSize > 0) {
            batches.add(batchSize);
        }

        int[] answer = new int[batches.size()];
        for (int i = 0; i < batches.size(); i++) {
            answer[i] = batches.get(i);
        }
        return answer;
    }
}
