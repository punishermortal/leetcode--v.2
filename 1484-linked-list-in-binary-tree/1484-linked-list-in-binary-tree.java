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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    ArrayList<TreeNode>ls = new ArrayList<>();
    public boolean isSubPath(ListNode head, TreeNode root) {
        getNodeFromTreeWhichIsInLinkList(head , root);
        for(TreeNode element : ls){
            if(isRootIsDubPathOrNot(head ,element))return true;
        }
        return false;
    }
    public void getNodeFromTreeWhichIsInLinkList(ListNode head , TreeNode root){
        if(head == null || root ==null) return;
        if(head.val == root.val){
            ls.add(root);
        }
        getNodeFromTreeWhichIsInLinkList(head ,root.left);
        getNodeFromTreeWhichIsInLinkList(head ,root.right);
    }
    public static boolean isRootIsDubPathOrNot(ListNode head , TreeNode root){
        if (head == null) return true;
        if (root == null) return false;
        if (head.val == root.val){
            return isRootIsDubPathOrNot(head.next,root.left) || isRootIsDubPathOrNot(head.next,root.right);
        }
        return false;
    }
}