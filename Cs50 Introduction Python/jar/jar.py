class Jar:
    def __init__(self, capacity=12):
        # I want check if capacity is a positivi integer
        if not isinstance(capacity,int) or capacity < 0 :
            raise ValueError("capacity should be an integer")
        # I want to refer the istance capacity to class Jar
        self._capacity = capacity
        # initialization about the numbers of coockies
        self._size = 0
        ...

    def __str__(self):
        # i want to return the number of cookies emoji * size number
        return self._size * "🍪"

        ...

    def deposit(self, n):

        if self.size + n > self.capacity:
            raise ValueError(f"n is to much, Maximum n = {self.capacity-self.size }")
        elif n > self.capacity:
            raise ValueError(f"n is exced the capacity of {capacity}")
        # if I passed all checks I add at size n biscuits
        self._size += n


        ...


    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Nom nom nom")
        # I update the self.size if the check is okay
        self._size -=n
        ...


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


        ...


# python jar.py

#if __name__ == "__main__:
#    main()


jar = Jar()
jar.deposit(3)
jar.withdraw(2)
print(jar)

