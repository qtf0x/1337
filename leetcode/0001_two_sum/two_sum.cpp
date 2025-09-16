/**
 * @author  Aster Marias <aster@bitangent.org>
 * @date    09/15/2025
 *
 * @brief   Given an array of integers `nums` and an integer `target`, return
 *          indices of the two numbers such that they add up to `target`. You
 *          may assume that each input would have exactly one solution, and you
 *          may not use the same element twice. You can return the answer in any
 *          order.
 * @details <https://leetcode.com/problems/two-sum/description/>
 */

#include <unordered_map>
#include <vector>

#include <cstddef> // size_t

class Solution {
public:
	std::vector<int> twoSum(const std::vector<int>& nums, const int target) {
		std::unordered_map<int, std::size_t> seen;
		
		for (std::size_t i{}; i < nums.size(); ++i) {
			const int num{nums.at(i)};
			const int complement{target - num};

			if (seen.contains(complement)) {
				return {static_cast<int>(i),
					static_cast<int>(seen.at(complement))};
			}

			seen.emplace(num, i);
		}

		return {};
	}
};
