import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> countByCategory = new HashMap<>();

        for (String[] clothing : clothes) {
            String category = clothing[1];
            int count = countByCategory.getOrDefault(category, 0);
            countByCategory.put(category, count + 1);
        }

        int combinations = 1;
        for (int count : countByCategory.values()) {
            combinations *= count + 1;
        }

        return combinations - 1;
    }
}
