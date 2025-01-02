class Solution {
    public char[][] rotateTheBox(char[][] box) {
        
        for(int i=0;i<box.length;i++){
            int zero=-1;
            for(int j=box[i].length-1;j>=0;j--){
                if(box[i][j]=='.' && zero==-1 ){
                    zero=j;
                }else if(box[i][j]=='*'){
                    zero=-1;
                }else{
                    if(zero!=-1){
                        swap(box,zero,j,i);
                        while(j<zero&& box[i][zero]!='.'){
                            zero--;
                        }

                    }
                }
            }
        }
        box=transpose(box);
        return box;
    }
    public void swap(char[][]arr,int i,int j,int row){
        char ch=arr[row][i];
        arr[row][i]=arr[row][j];
        arr[row][j]=ch;
    }
    public char[][] transpose(char[][]arr){
        int r=arr.length;
        int c=arr[0].length;
        char[][]trans=new char[c][r];
        for(int i=0;i<r;i++){
            for(int j=c-1;j>=0;j--){
                trans[j][r-i-1]=arr[i][j];
            }
        }
        return trans;
    }
}
