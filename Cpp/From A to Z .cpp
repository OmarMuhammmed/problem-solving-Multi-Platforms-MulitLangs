// https://www.codewars.com/kata/6512b3775bf8500baea77663/train/cpp

#include <string>

using namespace std;

string gimme_the_letters(const string& sp)
{
    string result = "";

    for (int i = sp[0] ; i<=sp[2] ; i++)
    {
        result.push_back(char(i));
    }
    
    return result;
}
