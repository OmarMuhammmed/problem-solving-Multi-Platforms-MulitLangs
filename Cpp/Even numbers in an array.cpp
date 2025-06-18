// https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c
#include <vector>
using namespace std;
#include <iostream>

vector<int> evenNumbers(vector<int> arr, int n) {
  
    vector<int> beforeResult = {};
    for (int i = 0 ; i < arr.size() ; i++)
    {
        if (arr[i] % 2 == 0) 
        {
            beforeResult.push_back(arr[i]);
        }
    }
    
    vector<int> result(beforeResult.end() - n, beforeResult.end());
    return result;
}