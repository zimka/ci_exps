"""
FooBar of example_pack
"""
class FooBar:
    """
    For every multiple of 5 print "Foo", for every multiple of n_bar print "Bar" and
    for every multiple of both 5 and n_bar print "FooBar" instead of the number
    """

    def __init__(self, n_bar: int):
        self.n_bar = n_bar

    def __call__(self, x: int) -> str:
        """FooBar result"""
        is_mult_5 = x % 5 == 0
        is_mult_n = x % self.n_bar == 0

        if is_mult_n and is_mult_5:
            return "FooBar"
        if is_mult_5:
            return "Foo"
        if is_mult_n:
            return "Bar"
        return str(x)

    def __repr__(self) -> str:
        return f"<FooBar|{self.n_bar}>"
