// https://www.codewars.com/kata/5168b125faced29f66000005/solutions/javascript

function solution(fullText, searchText) {
    let count = 0;
    let i = 0;
    const searchLength = searchText.length;

    while (i <= fullText.length - searchLength) {
        if (fullText.slice(i, i + searchLength) === searchText) {
            count++;
            i += searchLength; // Skip entire searchText (non-overlapping)
        } else {
            i += 1;
        }
    }

    return count;
}
