import random


def generate_landmarks(id_number, count):
    with open("landmark_data/landmark{}.txt".format(id_number), "w") as lf:
        lf.write(str(count))
        lf.write("\n")
        for _ in range(count):
            lf.write(str(random.randint(0, 100)) + " " + str(random.randint(0, 100)))
            lf.write("\n")


if __name__ == '__main__':
    for i in range(3):
        generate_landmarks(i, random.choice([4, 7, 10]))
