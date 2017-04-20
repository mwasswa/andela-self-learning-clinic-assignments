class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b

        for i in range(self.a):
            list.append(self, self.b)
            self.b += b
            i += 1

        self.length = i

    def search(self, required_number):
        found = False
        count = 0
        number_in_list = False
        first_index = 0
        last_index = self.length - 1
        try:
            index = self.index(required_number)
            in_list = True
        except ValueError:
            index = -1
            number_in_list = False

        while first_index <= last_index and not found and number_in_list and required_number != self[last_index]:
            mid_index = (first_index + last_index) // 2
            mid_value = self[mid_index]
            if mid_value == required_number:
                found = True
                count += 1
                index = mid_index
            else:
                if required_number < mid_value:
                    last_index = mid_index - 1
                    count += 1
                else:
                    first_index = mid_index + 1
                    count += 1

        return {"count": count, "index": index}