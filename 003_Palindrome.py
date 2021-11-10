is_palindrome = input()
is_palindrome = is_palindrome.lower().replace(' ', '')

print("Palindrome") if is_palindrome == is_palindrome[::-1] else print("Not Palindrome")
