/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        Set<Integer> exist = new HashSet<>();
        for(int n : nums)
        {
            exist.add(n);
        }
        ListNode res = new ListNode();
        while(head != null && exist.contains(head.val))
        {
            head = head.next;
        }
        if(head == null ) return null;
        res.val = head.val;
        head = head.next;
        ListNode ptr = res;
        while(head != null)
        {
            if(!exist.contains(head.val))
            {
                ListNode node = new ListNode(head.val);
                ptr.next = node;
                ptr = ptr.next;
            }
            head = head.next;
        }
        return res;
    }
}