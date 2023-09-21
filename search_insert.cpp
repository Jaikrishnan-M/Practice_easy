#include<iostream>
 
using namespace std;

double searchInsert(int arr[], int target, int size) {
    int i, flag = 0;  
    int al = size;     

    for (i = 0; i < al; i++) {
        if (arr[i] == target){
            flag = 1;
            return i, flag;
        } else if (arr[i]>target) {
            flag = 0;
            return i, flag;
        } else if ((i== al-1) & (flag == 0)) {
            return i+1, flag;
        }
    }
}


int main() {
    int nums[4] = {1,3,5,6};
    int targ = 5;
    int ind;
    bool flg;

   // pass pointer to the array as an argument.
    ind, flg = searchInsert(nums, targ, 4);

    if (flg) {
        cout << "The number should be inserted at:"<<ind<<endl;
    } else {
        cout << "The number is present at: "<<ind<<endl;
    }
    return cin.get();
}