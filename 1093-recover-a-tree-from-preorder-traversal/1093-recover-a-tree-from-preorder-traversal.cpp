class Solution {
public:
    TreeNode* recoverFromPreorder(string traversal) {
        int lstNum=0;
        int dashCnt=0;
        char lstChar='#';
        int n=traversal.size();
        stack<pair<TreeNode*,int>> st; // TreeNode depth
        TreeNode* ans= NULL;
        for(int i=0;i<n+1;i++) {
            if((i==n || traversal[i]=='-') && lstChar!='-') {
               int curDep=dashCnt;
               while( !st.empty() && st.top().second>=curDep) {
                  st.pop();
               }
               TreeNode* newNode = new TreeNode(lstNum);
               if( st.empty()) {
                     ans=newNode;
               } else {
                 TreeNode* toUpdate=st.top().first;
                 if( toUpdate->left == NULL) {
                    toUpdate->left=newNode;
                 } else if( toUpdate->right == NULL ){
                    toUpdate->right=newNode;
                 } else {
                    assert( toUpdate->left == NULL || toUpdate->right == NULL ); 
                 } 

               }
               st.push({ newNode, curDep});
               dashCnt=1;
               lstNum=0;
            } else if( traversal[i] =='-') {
                   dashCnt++;
            } else {
                lstNum= lstNum*10+ traversal[i]-'0';
            }
            if( i<n) {
            lstChar=traversal[i];
            }
        }
        return ans;
    }
};