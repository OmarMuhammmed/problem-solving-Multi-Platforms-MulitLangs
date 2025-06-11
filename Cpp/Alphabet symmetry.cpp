// https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/cpp


#include <vector>
#include <string>
using namespace std;

vector<int> solve(const vector<string>& arr) {
    vector <int> result ;  
    
    for(string word : arr)
    {
        int counter = 0 ; 
        for(int i = 0 ; i<word.size(); i++ )
        {
            if(word[i] == i + 97 || word[i] == i + 65)
            {
                counter++;
            }

        }
        result.push_back(counter);
    }
    return result ; 
};