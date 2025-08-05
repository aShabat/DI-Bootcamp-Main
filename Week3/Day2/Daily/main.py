# Step 1: Create the Pagination Class
#
#     Define a class called Pagination to represent paginated content.
#     It should optionally accept a list of items and a page size when initialized.
#
#
# Step 2: Implement the __init__ Method
#
#     Accept two optional parameters:
#     items (default None): a list of items
#
#     page_size (default 10): number of items per page
#
#     Behavior:
#     If items is None, initialize it as an empty list.
#     Save page_size and set current_idx (current page index) to 0.
#     Calculate total number of pages using math.ceil.
#
#
# Step 3: Implement the get_visible_items() Method
#
#     This method returns the list of items visible on the current page.
#     Use slicing based on the current_idx and page_size.
#
#
# Step 4: Implement Navigation Methods
#
# These methods should help navigate through pages:
#
#     go_to_page(page_num)
#     → Goes to the specified page number (1-based indexing).
#     → If page_num is out of range, raise a ValueError.
#
#     first_page()
#     → Navigates to the first page.
#
#     last_page()
#     → Navigates to the last page.
#
#     next_page()
#     → Moves one page forward (if not already on the last page).
#
#     previous_page()
#     → Moves one page backward (if not already on the first page).
#
# 📝 Note:
#
#     Pages are indexed internally from 0, but user input is expected to start at 1.
#     All navigation methods (except go_to_page) should return self to allow method chaining.
#
#
# Step 5: Add a Custom __str__() Method
#
#     This magic method should return a string displaying the items on the current page, each on a new line.
#
#
# Step 6: Test Your Code
import math
from typing import override


class Pagination:
    def __init__(self, items=None, page_size=10):
        if items == None:
            self.items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.pages_count = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        return self.items[
            self.page_size * self.current_idx : self.page_size * (self.current_idx + 1)
        ]

    def go_to_page(self, page_num):
        if page_num <= 0:
            raise ValueError
        if page_num > self.pages_count:
            # raise ValueError -- this is what instruction ask for, but test cases in Step 6 show that expected behavior is to go to last page
            self.current_idx = self.pages_count - 1
        else:
            self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.pages_count - 1
        return self

    def next_page(self):
        if self.current_idx + 1 < self.pages_count:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    @override
    def __str__(self):
        out = ""
        for item in self.get_visible_items():
            out += str(item) + "\n"

        return out


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# Output: 7

p.go_to_page(0)
# Raises ValueError
