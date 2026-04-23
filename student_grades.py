class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        pocet_bodu = self.get_by_index(index)
        if pocet_bodu >= 90:
            return "A"
        elif pocet_bodu >= 80:
            return "B"
        elif pocet_bodu >= 70:
            return "C"
        elif pocet_bodu >= 60:
            return "D"
        elif pocet_bodu >= 50:
            return "E"
        else:
            return "F"

    def find(self, score):
        scores = self.scores
        positions = []
        i = 0
        for number in scores:
            if number == score:
                positions.append(i)
            i += 1
        return positions

    def get_sorted(self):
        scores = self.scores.copy()
        for pocet_kol in range(len(scores)):
            for idx in range(0, len(scores) - pocet_kol - 1):
                if scores[idx] > scores[idx + 1]:
                    scores[idx], scores[idx + 1] = scores[idx + 1], scores[idx]
        return scores



def main():
    # results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    from sorting import random_numbers
    results = StudentsGrades(random_numbers(30, 0, 100))
    print(results.count())
    print(results.get_sorted())

    pocet_studentu = StudentsGrades.count(results)
    print(f"Pocet studentu kteri psali test: {pocet_studentu}")
    for i in range(results.count()):
        pocet_bodu = results.get_by_index(i)
        znamka = results.get_grade(i)
        print(f"Student {i}: {pocet_bodu} points - {znamka}")
    print(f"Students with 100 points: {results.find(100)}")
    print(f"Sorted: {results.get_sorted()}")


if __name__ == "__main__":
    main()