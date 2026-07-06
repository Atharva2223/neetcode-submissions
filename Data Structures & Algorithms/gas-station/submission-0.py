class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_gas = 0
        start_index = 0
        total_gas = 0
        cost_gas = 0

        for i in range(len(gas)):
            total_gas+=gas[i]
            cost_gas+=cost[i]
        if total_gas < cost_gas:
            return -1
        
        for i in range(len(gas)):

            current_gas+=gas[i] - cost[i]
            if current_gas < 0:
                start_index = i+1
                current_gas = 0
        return start_index
        