# --- 5168b125faced29f66000005 --- 

# 'abcdeb','b'), 2
# abc','b'), 1
# 'ccddeeccddeecc', 'cc'), 3) 

def solution(full_text, search_text):
    count = 0
    i = 0
    search_length = len(search_text)

    while i <= len(full_text) - search_length:
        if full_text[i:i+search_length] == search_text:
            count += 1
            i += search_length  # step whole the word (Non-overlap)
        else:
            i += 1  # move 1 index only

    return count

solution('abc','b')  
