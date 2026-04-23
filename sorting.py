import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

# my_list[1], my_list[3] = my_list[3], my_list[1]   takto prohodit cisla

def selection_sort(number_list):
    for pozice in range(len(number_list)):
        idx_min = pozice
        for idx_prohledavany in range(pozice + 1, len(number_list)):
            minimum = min(number_list[idx_min:len(number_list)])
            if minimum == number_list[idx_prohledavany]:
                number_list[idx_min], number_list[idx_prohledavany] = number_list[idx_prohledavany], number_list[idx_min]
    return number_list


def bubble_sort(number_list):
    plt.ion()
    plt.show()
    for pocet_kol in range(len(number_list)):
        for idx in range(0, len(number_list)-pocet_kol-1):
            index_highlight1 = idx
            index_highlight2 = idx + 1
            colors = ["steelblue"] * len(number_list)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(number_list)), number_list, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if number_list[idx] > number_list[idx+1]:
                number_list[idx], number_list[idx+1] = number_list[idx+1], number_list[idx]
    plt.ioff()
    plt.show()
    return number_list

# je to hrozny a zbytecne slozity kod ale funguje to a prisla jsem na to sama


def main():
    listicecek = [5, 1, 4, 2, 8]
    print("Selection sort")
    print(f"puvodni list: {listicecek}"
          f"\nserazeny list: {selection_sort(listicecek)}")
    values = random_numbers(20)
    print(f"puvodni list: {values}"
          f"\nserazeny list: {selection_sort(values)}")

    listicecek = [5, 1, 4, 2, 8]
    values = random_numbers(100)
    print("Bubble sort")
    print(f"puvodni list: {listicecek}"
          f"\nserazeny list: {bubble_sort(listicecek)}")
    print(f"puvodni list: {values}"
          f"\nserazeny list: {bubble_sort(values)}")

if __name__ == "__main__":
    main()