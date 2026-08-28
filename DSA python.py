def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome."""
    # Convert to lowercase and remove non-alphanumeric characters for robust checking
    processed_s = "".join(char for char in s if char.isalnum()).lower()
    
    # Initialize two pointers: one at the start, one at the end
    left = 0
    right = len(processed_s) - 1
    
    while left < right:
        # If characters at the pointers do not match, it's not a palindrome
        if processed_s[left] != processed_s[right]:
            return False
        # Move the pointers inward
        left += 1
        right -= 1
        
    # If the loop completes, all pairs matched
    return True

# --- Test Cases ---
input_1 = "A man, a plan, a canal: Panama"
input_2 = "race a car"
















def two_sum(nums: list[int], target: int) -> list[int]:
    """Finds indices of two numbers that sum to the target."""
    # Hash map to store: {number: index}
    num_map = {} 
    
    for i, num in enumerate(nums):
        # Check if the complement (target - num) is already in our map
        complement = target - num
        
        if complement in num_map:
            # Found the pair! Return the indices
            return [num_map[complement], i]
        
        # If not found, add the current number and its index to the map
        num_map[num] = i
        
    # Should theoretically not be reached if a solution is guaranteed
    return []

# --- Test Cases ---
nums = [2, 7, 11, 15]
target = 9
print("hello")








def is_valid_parentheses(s: str) -> bool:
    """Checks if the given string of brackets is balanced."""
    # Stack to hold opening characters
    stack = []
    
    # Map closing characters to their required opening counterparts
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in s:
        if char in mapping.values():
            # It's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in mapping.keys():
            # It's a closing bracket
            if not stack:
                # Stack is empty, but we found a closing bracket (e.g., "}")
                return False
            
            # Pop the top element and check if it matches the required opener
            top_element = stack.pop()
            if mapping[char] != top_element:
                return False
        else:
            # Handle non-bracket characters if necessary, though not required by the prompt
            continue
    
    # If the stack is empty, all opened brackets were correctly closed
    return not stack

# --- Test Cases ---
input_1 = "([]{})"
input_2 = "{[()]}(" 
