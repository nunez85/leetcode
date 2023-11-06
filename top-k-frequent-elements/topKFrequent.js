/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const frequencyCounter = new Map();
  for (let n of nums) {
    if (frequencyCounter.has(n)) {
      frequencyCounter.set(n, frequencyCounter.get(n) + 1);
    } else {
      frequencyCounter.set(n, 1);
    }
  }
  const buckets = [];
  for (let i = 0; i <= nums.length; i++) {
    buckets.push([]);
  }

  for (let [n, count] of frequencyCounter) {
    buckets[count].push(n);
  }

  const res = [];
  let i = nums.length;
  while (i > 0) {
    for (let n of buckets[i]) {
      res.push(n);
      if (res.length === k) {
        return res;
      }
    }
    i--;
  }
};

const nums = [1, 1, 2, 3, 2, 4, 2, 4, 4, 4, 2];
const k = 2;

topKFrequent(nums, k);
