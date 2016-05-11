class Solution(object):
	def twoSum(self, nums, target):
		"""
		"""

		my_dict = {}

		for item in xrange(len(nums)):
			if target - nums[item] in my_dict:
				return [my_dict[target-nums[item]], item]
			my_dict[nums[item]] = item

		return []

