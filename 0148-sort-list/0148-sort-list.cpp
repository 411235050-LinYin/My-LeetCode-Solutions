/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/*
    -LeetCode format-
    Problem: 148. Sort List
    Difficulty: Medium
    
    by Inversionpeter
*/



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head)
            return nullptr;
        if (!head->next)
            return head;
        ListNode *dummy = new ListNode(0, head), *nowTail = dummy, *slow = dummy, *fast = dummy;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        fast = slow->next;
        slow->next = nullptr;
        head = sortList(head);
        fast = sortList(fast);
        while (head || fast)
            if (!head) {
                nowTail = nowTail->next = fast;
                fast = fast->next;
            }
            else if (!fast) {
                nowTail = nowTail->next = head;
                head = head->next;
            }
            else if (head->val < fast->val) {
                nowTail = nowTail->next = head;
                head = head->next;
            }
            else {
                nowTail = nowTail->next = fast;
                fast = fast->next;
            }
        return dummy->next;
    }
};