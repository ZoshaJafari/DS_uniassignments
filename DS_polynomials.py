#import os

class Node:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = Node(None, None)
        self.head.next = self.head
        self.head.prev = self.head
        self.n = 0

    def get(self, ind):
        if ind >= self.size():
            raise Exception('Out of list')
        x = self.head.next
        for _ in range(ind):
            x = x.next
        return x

    def insert_after(self, x, data1, data2):
        y = Node(data1, data2)
        self.n += 1
        y.prev = x
        y.next = x.next
        x.next = y
        y.next.prev = y
        return y

    def delete(self, x):
        if self.size() == 0:
            raise Exception('List is empty')
        self.n -= 1
        x.prev.next = x.next
        x.next.prev = x.prev
        return x

    def find(self, val):
        x = self.head.next
        for _ in range(self.size()):
            if x.data1 == val:
                return x
            x = x.next
        return None

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0

def parse_polynomial(poly):
    terms = poly.replace('-', '+-').split('+')
    parsed_terms = {}
    for term in terms:
        if 'x' in term:
            if '^' in term:
                coeff, exp = term.split('x^')
                exp = int(exp)
            else:
                coeff, exp = term.split('x')
                exp = 1
            coeff = int(coeff) if coeff not in ['', '+'] else 1
            coeff = -1 if coeff == '-' else coeff
        else:
            coeff = int(term)
            exp = 0
        parsed_terms[exp] = parsed_terms.get(exp, 0) + coeff
    return parsed_terms

def sum_polynomials_in_dict(poly_dicts):
    result = {}
    for poly in poly_dicts:
        for exp, coeff in poly.items():
            result[exp] = result.get(exp, 0) + coeff
    return result

def multiply_polynomials_in_dict(poly_dicts):
    result = {}
    for poly in poly_dicts:
        if not result:
            result = poly
        else:
            temp_result = {}
            for exp1, coeff1 in result.items():
                for exp2, coeff2 in poly.items():
                    exp = exp1 + exp2
                    coeff = coeff1 * coeff2
                    temp_result[exp] = temp_result.get(exp, 0) + coeff
            result = temp_result
    return result

def polynomial_to_string(poly):
    terms = []
    for exp in sorted(poly.keys(), reverse=True):
        coeff = poly[exp]
        if coeff == 0:
            continue
        if exp == 0:
            terms.append(f'{coeff}')
        elif exp == 1:
            terms.append(f'{coeff}x' if coeff != 1 else 'x')
        else:
            terms.append(f'{coeff}x^{exp}' if coeff != 1 else f'x^{exp}')
    return ' + '.join(terms).replace(' + -', ' - ')

def input_polynomials(polynum_list):
    inp_num = int(input("How many polynomials would you like to add?: "))
    for _ in range(inp_num):
        inp_polynum = input("Please enter polynomial: ")
        polynum_list.insert_after(polynum_list.head.prev, inp_polynum, None)
        print("Polynomial is added!")

def sum_polynomials(polynum_list):
    if polynum_list.is_empty():
        print("No polynomials available to sum.")
        return

    print_polynomials(polynum_list)
    sum_num = int(input("Enter numbers of polynomials to calculate sum: "))
    if sum_num > polynum_list.size():
        print(f"Cannot sum {sum_num} polynomials, only {polynum_list.size()} available.")
        return

    indices = []
    for _ in range(sum_num):
        while True:
            poly_index = int(input("Enter desired polynomial number (1-based index): "))
            if 1 <= poly_index <= polynum_list.size():
                indices.append(poly_index - 1)
                break
            else:
                print("Invalid index, please try again.")

    selected_polynomials = [parse_polynomial(polynum_list.get(i).data1) for i in indices]
    result = sum_polynomials_in_dict(selected_polynomials)
    result_string = polynomial_to_string(result)
    print("Sum of selected polynomials: ", result_string)

def multiply_polynomials(polynum_list):
    if polynum_list.is_empty():
        print("No polynomials available to multiply.")
        return

    print_polynomials(polynum_list)
    mult_num = int(input("Enter numbers of polynomials to calculate product: "))
    if mult_num > polynum_list.size():
        print(f"Cannot multiply {mult_num} polynomials, only {polynum_list.size()} available.")
        return

    indices = []
    for _ in range(mult_num):
        while True:
            poly_index = int(input("Enter desired polynomial number (1-based index): "))
            if 1 <= poly_index <= polynum_list.size():
                indices.append(poly_index - 1)
                break
            else:
                print("Invalid index, please try again.")

    selected_polynomials = [parse_polynomial(polynum_list.get(i).data1) for i in indices]
    result = multiply_polynomials_in_dict(selected_polynomials)
    result_string = polynomial_to_string(result)
    print("Product of selected polynomials: ", result_string)

def print_polynomials(polynum_list):
    if not polynum_list.is_empty():
        print("Polynomials in list:")
        x = polynum_list.head.next
        while x != polynum_list.head:
            print(x.data1)
            x = x.next
    else:
        print("No polynomials in the list.")


#def clear_screen():
#    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    polynum_list = List()
    operation_list = ["1.INPUT", "2.SUM", "3.MULTIPLY", "4.PRINT", "5.EXIT"]
    print(operation_list)

    while True:
        op_entry = input("Enter number of desired operation: ")
        if op_entry == "1":
            input_polynomials(polynum_list)
        elif op_entry == "2":
            sum_polynomials(polynum_list)
        elif op_entry == "3":
            multiply_polynomials(polynum_list)
        elif op_entry == "4":
            print_polynomials(polynum_list)
        elif op_entry == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid operation, please try again.")

if __name__ == "__main__":
    main()

