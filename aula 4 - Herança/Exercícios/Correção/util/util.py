class Util:

    @staticmethod
    def bigger_number(n1:int, n2:int, n3:int):
        list_numbers = [n1, n2, n3]

        x = 0

        for n in list_numbers:
            if n > x:
                x = n

        return f"O número {x} é o maior."