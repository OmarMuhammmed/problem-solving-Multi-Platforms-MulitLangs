// https://www.codewars.com/kata/56582133c932d8239900002e/train/cpp

#include <bits/stdc++.h>
#include <vector>
using namespace std;

unsigned int most_frequent_item_count(const vector<int>& collection) {
    int result = 0;

    for (int i = 0; i < collection.size(); i++) {
        int counter = 0;

        for (int j = 0; j < collection.size(); j++) {
            if (collection[i] == collection[j]) {
                counter++;
            }
        }

        if (counter > result) {
            result = counter;
        }
    }

    return result;
}
