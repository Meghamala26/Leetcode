class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<int> v1(amount+1,INT_MAX);// dp array to store V1[i], 
        // minumum number of coins to make i amount 
        v1[0] = 0;
        for(int i=1; i<=amount; i++)
        {
            int sub_res = INT_MAX;
            for(int j=0; j<n; j++)
            {
                if(coins[j] <= i)
                    sub_res = min(v1[i - coins[j]],sub_res);
            }
            if(sub_res !=INT_MAX)
                v1[i] = 1 + sub_res;
        }
        if(v1[amount] != INT_MAX)
            return v1[amount];
        return -1;
        
    }
};