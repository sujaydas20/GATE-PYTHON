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














class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    """Reverses the linked list iteratively."""
    prev = None
    current = head
    
    while current:
        # 1. Store the next node before changing the pointer
        next_node = current.next
        
        # 2. Reverse the current node's pointer
        current.next = prev
        
        # 3. Move pointers one step forward
        prev = current
        current = next_node
        
    # 'prev' will be the new head (the last node of the original list)
    return prev

# Helper function to create and print the list (for testing)
def print_list(head):
    output = []
    temp = head
    while temp:
        output.append(str(temp.val))
        temp = temp.next
    return " -> ".join(output)

# --- Test Case Setup ---
# Original List: 1 -> 2 -> 3 -> 4
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)











def binary_search(arr: list[int], target: int) -> int:
    """Finds the index of the target in a sorted array using Binary Search."""
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        # Calculate mid index (prevents overflow)
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            # Target found
            return mid
        elif arr[mid] < target:
            # Target must be in the right half
            low = mid + 1
        else:
            # Target must be in the left half
            high = mid - 1
            
    # If loop finished, the target was not found
    return -1

# --- Test Cases ---
sorted_array = [2, 5, 8, 12, 16, 23, 38]
target_found = 16
target_not_found = 10
