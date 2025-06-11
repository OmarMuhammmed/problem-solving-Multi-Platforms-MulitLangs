function solve(arr) {
  let result = [];

  arr.forEach(word => {
    let count = 0;

    for (let i = 0; i < word.length; i++) {
      let char = word[i].toLowerCase();
      if (char.charCodeAt(0) - 97 === i) {
        count++;
      }
    }

    result.push(count);
  });

  return result;
}

// Example usage:
console.log(solve(["abode", "ABc", "xyzD"])); // Output: [4, 3, 1]
