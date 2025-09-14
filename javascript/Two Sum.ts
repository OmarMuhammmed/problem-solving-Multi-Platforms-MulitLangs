function twoSum(nums: number[], target: number): number[] {
    const seen = new Map<number, number>(); // value -> index

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (seen.has(complement)) {
            return [seen.get(complement)!, i];
        }
        seen.set(nums[i], i);
    }

    return []; // في حال مفيش حل (لكن السؤال ضامن وجود حل)
}
