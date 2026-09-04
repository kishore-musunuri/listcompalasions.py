# 1. Squares for even numbers and cubes for odd numbers
result1 = [x**2 if x % 2 == 0 else x**3 for x in range(1, 11)]
print("Squares/Cubes:", result1)


# 2. Multiplication table (1-3 x 1-3)
result2 = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplication Table:", result2)


# 3. Extract vowels from "Python"
result3 = [ch for ch in "Python" if ch.lower() in "aeiou"]
print("Vowels:", result3)


# 4. ASCII values of "ABC"
result4 = [ord(ch) for ch in "ABC"]
print("ASCII Values:", result4)


# 5. Generate uppercase alphabets A-Z
result5 = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print("Alphabets:", result5)


# 6. Capitalize every word
text = "hello world python"
result6 = [word.capitalize() for word in text.split()]
print("Capitalized Words:", result6)


# 7. Print Even or Odd for numbers 1-10
result7 = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 11)]
print("Even/Odd:", result7)
