# Goal: Implement dunder methods for a Currency class to handle string representation, integer conversion, addition, and in-place addition.


from typing import override


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    @override
    def __str__(self) -> str:
        if self.amount == 1:
            return f"1 {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    @override
    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
        else:
            raise TypeError(f"Cannot add Currency and <{type(other)}>")

    def __iadd__(self, other):
        return Currency(self.currency, self + other)

    # Your code starts HERE


# Using the code above, implement the relevant methods and dunder methods which will output the results below.


c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

# the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1)
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>
