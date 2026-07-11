import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        map = dict()

        for num in hand:
            map[num] = 1+map.get(num,0)
        

        minheap = list(map.keys())
        heapq.heapify(minheap)

        while minheap:

            firstmin =minheap[0]

            for firstcard in range(firstmin,firstmin+groupSize):

                if map.get(firstcard,0) == 0:
                    return False

                map[firstcard]-=1


                if map[firstcard] == 0:

                    if firstcard != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True







        
     