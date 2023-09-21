#include<iostream>

using namespace std;

vector<int> inc_ind(vector<int> vec,int ind, ind flag);
vector<int> add_last(vector<int> vect);

int main() {
    vector<int> list_{1,2,3};
    list_ = add_last(list_);
    int lent = list_.size();

    for (int i = 0; i<=lent; i++) {
        cout << list_[i]<<endl;
    }
    std::cin.get();
}

vector<int> inc_ind(vector<int> vec, int ind, int flag) {
    if (flag == 1) {vec[ind] += 1;}

    if (vec[ind] == 10) {
        vec[ind]=0;
        if (ind==0) vec.insert(0,1);
        else vec[ind-1] += 1;
    }
    return vec;
}

vector<int> add_last(vector<int> vect) {
    int flag = 1;
    int i = vect.size() - 1;
    while (i>0) {
        vect = inc_ind(vect,i,flag);
        flag = 0;
        i-=1;
    }
    return vect;
}


// def add_last(vect):
//     flag = 1
//     i = len(vect) - 1    
//     while i>=0:
//         vect = inc_ind(vect,i,flag)
//         flag = 0
//         i -= 1

//     return vect