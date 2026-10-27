import numpy as np


# q1. sensor readings[cite: 1]
print("--- q1. sensor readings ---")
temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

# a. add 2°c to every reading using vectorization[cite: 1]
temp_corrected = temperature + 2
print(f"a. corrected temperatures: {temp_corrected}")

# b. convert all temperatures from celsius to fahrenheit[cite: 1]
temp_f = (9/5) * temp_corrected + 32
print(f"b. temperatures in fahrenheit: {temp_f}")

# c. identify all readings greater than 32°c using boolean indexing[cite: 1]
high_temps = temp_corrected[temp_corrected > 32]
print(f"c. temperatures > 32°c: {high_temps}")

# d. count how many readings exceed 32°c[cite: 1]
count_high = np.sum(temp_corrected > 32)
print(f"d. count of temperatures > 32°c: {count_high}")

# e. explain how vectorization and boolean indexing make data processing efficient[cite: 1]
print("e. explanation: vectorization applies math to whole arrays at once, skipping slow python loops. boolean indexing acts as a fast filter to extract data without manual if-conditions.")


# ==========================================
# q2. daily steps[cite: 1]
# ==========================================
print("\n--- q2. daily steps ---")
steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

# a. calculate the total steps recorded[cite: 1]
print(f"a. total steps: {steps.sum()}")

# b. calculate the mean number of steps[cite: 1]
print(f"b. mean steps: {steps.mean()}")

# c. find the maximum and minimum values[cite: 1]
print(f"c. max steps: {steps.max()}, min steps: {steps.min()}")

# d. calculate the total steps for each day using axis=0[cite: 1]
print(f"d. total steps per day (axis=0): {steps.sum(axis=0)}")

# e. calculate the total steps for each user using axis=1[cite: 1]
print(f"e. total steps per user (axis=1): {steps.sum(axis=1)}")

# f. find the user/day position containing the maximum number of steps using argmax()[cite: 1]
max_pos = np.unravel_index(steps.argmax(), steps.shape)
print(f"f. position of max steps (user index, day index): {max_pos}")


# q3. numpy array operations[cite: 2]

print("\n--- q3. numpy array operations ---")

# a. create the original array[cite: 2]
original = np.array([1, 2, 3, 4, 5, 6])

# b. create a slice containing elements from index 1 to 4[cite: 2]
subset = original[1:4]

# c. modify the first element of subset to 999 and display both[cite: 2]
subset[0] = 999
print(f"c. modified subset: {subset}")
print(f"   original array after modifying subset: {original}")

# d. create another slice using .copy(), modify, and display[cite: 2]
copy_subset = original[1:4].copy()
copy_subset[0] = 500
print(f"d. copied subset after modification: {copy_subset}")
print(f"   original array after modifying copy: {original}")

# e. create an array 1 to 12 and reshape it into a 3x4 matrix[cite: 2]
matrix = np.arange(1, 13).reshape(3, 4)
print(f"e. 3x4 matrix:\n{matrix}")

# f. extract specific elements using slicing[cite: 2]
print(f"f. first row: {matrix[0]}")
print(f"   last row: {matrix[-1]}")
print(f"   second column: {matrix[:, 1]}")
print(f"   elements from rows 1-2 and columns 2-3:\n{matrix[1:3, 2:4]}")

# g. create flattened versions using flatten() and ravel()[cite: 2]
flat_arr = matrix.flatten()
ravel_arr = matrix.ravel()

# h. modify element in ravel() array and observe original[cite: 2]
ravel_arr[0] = -99
print(f"h. after modifying ravel() array, matrix[0,0] is: {matrix[0, 0]} (original is affected because ravel returns a view)")

# i. modify element in flatten() array and observe original[cite: 2]
flat_arr[1] = -88
print(f"i. after modifying flatten() array, matrix[0,1] is: {matrix[0, 1]} (original is not affected because flatten returns a copy)")

# j. display the shape, ndim, size, and dtype[cite: 2]
print(f"j. shape: {matrix.shape}, ndim: {matrix.ndim}, size: {matrix.size}, dtype: {matrix.dtype}")



# q4. cognitive-assistive system (ols)[cite: 3]

print("\n--- q4. cognitive-assistive system ---")
x = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])
y = np.array([40, 65, 30, 85])

# a. display the shape and dimensions of x[cite: 3]
print(f"a. shape of x: {x.shape}, dimensions of x: {x.ndim}")

# b. calculate transpose of x and explain it[cite: 3]
# note: using np.transpose(x) instead of x.T to keep everything strictly lowercase
x_t = np.transpose(x)
print(f"b. transpose of x:\n{x_t}")
print("   explanation: the transpose swaps rows and columns, turning our 4 users into columns and 3 features into rows.")

# c. calculate the matrix product: transpose(x) @ x[cite: 3]
xtx = x_t @ x
print(f"c. x transpose @ x:\n{xtx}")

# d. calculate the matrix inverse[cite: 3]
xtx_inv = np.linalg.inv(xtx)
print(f"d. inverse of (x transpose @ x):\n{xtx_inv}")

# e. implement the ordinary least squares equation[cite: 3]
beta = xtx_inv @ x_t @ y
print(f"e. ols coefficients (beta): {beta}")

# f. explain the resulting coefficients[cite: 3]
print("f. explanation: these coefficients show the weight of each feature (sleep, activity, stress). a positive number means if that feature goes up, the final score goes up.")

# g. calculate predicted assistance score for a new user[cite: 3]
new_user = np.array([5, 40, 7])
predicted_score = new_user @ beta
print(f"g. predicted assistance score for the new user: {predicted_score:.2f}")
