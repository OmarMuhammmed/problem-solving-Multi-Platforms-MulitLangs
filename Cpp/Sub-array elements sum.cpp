#include<vector>
using namespace std;

long elementsSum(const vector<vector<int>>& arr, int d = 0) {
    long result = 0;
    int arrSize = arr.size();

    if (arrSize == 0) 
    {
        return result;
    }

    for(int subArr = 0; subArr < arrSize; subArr++) 
    {
        int index = (arrSize - 1) - subArr;
        
        if (index < arr[subArr].size()) 
        {
            result += arr[subArr][index];
        }
        else 
        {
            result += d;
        }
    }

    return result;
}
