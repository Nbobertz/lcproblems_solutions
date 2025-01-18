#Here we are given 3 strings and we have to capture beautiful indexes

# List to store the beautiful indices
ans = []
# Lists to store starting indices of occurrences of strings 'a' and 'b'
indices_a, indices_b = [], []

# Step 2: Find indices of occurrences of string 'a'
for i in range(len(s) - len(a) + 1):
    if s[i:i + len(a)] == a:
        indices_a.append(i)

# Step 3: Find indices of occurrences of string 'b'
for j in range(len(s) - len(b) + 1):
    if s[j:j + len(b)] == b:
        indices_b.append(j)

# Step 4: Check conditions and add beautiful indices to 'ans'
for i in indices_a:
    for j in indices_b:
        # Check if substrings match and absolute difference <= k
        if abs(i - j) <= k:
            ans.append(i)
            break

# Step 5: Sort the beautiful indices in ascending order
ans.sort()

# Step 6: Return the final result
return ans