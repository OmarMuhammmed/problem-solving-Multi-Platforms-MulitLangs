// https://www.codewars.com/kata/559760bae64c31556c00006b/train/cpp

#include <iostream>
#include <vector>
using namespace std; 


vector<int> climb(int n)
{
    vector<int> result;  // 13 -> { 1, 3, 6, 13 }
    while(n > 1)
    {
        result.insert(result.begin(), n); 
        n = n / 2;
    }
    result.insert(result.begin(), n);
    return result ; 
}