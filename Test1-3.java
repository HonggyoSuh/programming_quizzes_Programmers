import java.util.*;

class Solution {
    static String[] arr = { "RR", "Rr", "Rr", "rr" };

    public String[] solution(int[][] queries) {

        int len = queries.length;

        String rst[] = new String[len];
        for (int i = 0; i < len; i++) {
            int gen = queries[i][0];
            int num = queries[i][1] - 1;
            Stack<Integer> stk = new Stack<>();
            if (gen == 1) {
                rst[i] = "Rr";
            } else {
                while (gen > 1) {
                    gen--;
                    stk.push(num % 4);
                    num /= 4;
                }
                boolean flag = false;
                while (!stk.isEmpty()) {
                    int pop = stk.pop();
                    if (pop == 0 || pop == 3) {
                        rst[i] = arr[pop];
                        flag = true;
                        break;
                    }
                }
                if (!flag) {
                    rst[i] = "Rr";
                }

            }
        }
        return rst;
    }
}