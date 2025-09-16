/**
 * @author  Aster Marias <aster@bitangent.org>
 * @date    09/16/2025
 *
 * @brief   You are given two non-empty linked lists representing two
 *          non-negative integers. The digits are stored in reverse order, and
 *          each of their nodes contains a single digit. Add the two numbers and
 *          return the sum as a linked list. You may assume the two numbers do
 *          not contain any leading zero, except the number 0 itself.
 * @details <https://leetcode.com/problems/add-two-numbers/description/>
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // a single digit in l1 or l2 is [0, 9] so with carry solution digits
        // are only [0, 19] and the carry is either 0 or 1 (no need for more
        // memory like an int)
        char digit1{}, digit2{}, soln_digit{};
        bool carry{};

        // allocate dummy head on the stack to avoid cleaning up dynamic memory
        ListNode sum;
        ListNode* sum_it{&sum};

        while (l1 || l2 || carry) {
            digit1 = 0;
            digit2 = 0;

            if (l1) {
                digit1 = l1->val;
                l1 = l1->next;
            }

            if (l2) {
                digit2 = l2->val;
                l2 = l2->next;
            }

            soln_digit = digit1 + digit2 + carry;
            carry = soln_digit > 9;

            // only push back least significant digit of current sum
            sum_it->next = new ListNode(soln_digit % 10);
            sum_it = sum_it->next;
        }

        return sum.next;
    }
};
