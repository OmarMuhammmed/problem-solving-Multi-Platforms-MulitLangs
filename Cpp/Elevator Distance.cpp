#include <vector>
#include <iostream>
using namespace std ; 

int elevator_distance(vector<int> array) {
  
    int result = 0 ; 
    // array = [2, 5 , 3, 4]
    for(int i = 0 ; i<array.size()-1 ; i++)
    {
        result +=  abs(array[i]-array[i+1]) ; 
    }   
    return result ;
    
}