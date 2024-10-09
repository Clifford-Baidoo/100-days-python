#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"Total number of pages is: {pages}")
print(f"Total number of words per page is: {word_per_page}")
print(total_words)