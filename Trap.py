import random
import concurrent.futures
import time


class Trap:
    def __init__(self, gv1, gv2, height):
        self.gv1 = gv1
        self.gv2 = gv2
        self.height = height

    def __str__(self):
        return f"ტრაპეციის სიმაღლეა{self.height} ფუძე1: {self.gv1} ფუძე2 {self.gv2}"

    def area(self):
        return 0.5 * (self.gv2 + self.gv1) / self.height

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __mod__(self, other):
        return self.area() / other.area()


class Rec(Trap):
    def __init__(self, length, width):
        super().__init__(length, length, width)

    def area(self):
        return self.gv1 * self.height

    def __str__(self):
        return f"ოთხკუთხედის სიგრძეა {self.height} და სიგანეა {self.gv1}"


class Kvadrati(Rec):
    def __init__(self, gv):
        super().__init__(gv, gv)

    def area(self):
        return self.gv1 ** 2

    def __str__(self):
        return f"კვადრატის გვერდია {self.gv1}"


def fartobis_gamotvla(figura):
    figura.area()


def threading_(figura):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor1:
        executor1.submit(fartobis_gamotvla, figura)


def main():
    start = time.time()
    digit_list = [[random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)] for _ in range(10)]
    lst = [Trap(*random.choice(digit_list)) for _ in range(50)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(threading_, lst)

    end = time.time()

    print(f"time {end - start}")


if __name__ == "__main__":
    main()

    # მხოლოდ პროცესით დაჭირდა  0.9650840759277344
    # ორივეს ერთად 0.18441438674926758
    # მხოლოდ ნაკადებით 0.0010001659393310547
