// https://leetcode.com/problems/top-k-frequent-elements/

public static int[] BucketSortSolution(int[] nums, int k)
{

    var buckets = new List<List<int>>();
    for (int x = 0; x <= nums.Length; x++) { 
        buckets.Add(new List<int>());
    }

    var frequencyCounter = new Dictionary<int, int>();
    foreach (int n in nums) {
        if (frequencyCounter.ContainsKey(n)) {
            frequencyCounter[n] += 1;
        } else {
            frequencyCounter.Add(n, 1);
        }
    }

    foreach (var (n, freq) in frequencyCounter) {
        buckets[freq].Add(n);	
    }

    var res = new int[k];
    var i = 0;
    var countDown = nums.Length; 
    while(countDown != 0) {
        foreach (var b in buckets[countDown]) {
            res[i] = b;
            i++;
            if (i == k) {
                return res;
            }
        }
        countDown--;
    }

    return res;
}