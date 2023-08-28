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
    ListNode* rotateRight(ListNode* head, int k) 
    {
        if(k == 0 || head == NULL)
            return head;
            
        ListNode *end,*ptr;
        int n=0;

        ptr = end = head;
        while(ptr!=NULL)
        {
            if(end->next != NULL)
                end = end->next;
            n++;
            ptr = ptr->next;
            
        }
        // cout<<"\nn = "<<n;
        // cout<<"\nk = "<<k;
        // cout<<"\nend->val = "<<end->val;

        k = k%n;
        ptr = head;
        for(int i=2;i<=(n-k);i++)
            ptr = ptr->next;

        //ptr points to kth node from end
        //end points to the last node

        end->next = head;
        head = ptr->next;
        ptr->next = NULL;
        
        return head;

    }
};
