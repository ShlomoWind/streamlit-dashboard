from collections import Counter
import csv

from urllib3.filepost import writer

#תרגיל 2
try:
    with open("my_text.txt","w") as f:
        f.write("Hello, World!\n")
        f.write("It’s the first exercise in I/O\n")
        f.write("That mean it is number 1\n")
        f.write("Not 2\n")
        f.write("Not three\n")
        f.write("It is exciting\n")
        f.write("And i am all 4 it\n")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")

#תרגיל 3
try:
    with open("my_text.txt","r")as f:
        for line in f:
            for word in line.split():
                try:
                    int(word)
                    print(line.strip())
                    break
                except ValueError:
                    continue
except IOError as e:
    print(f"An error occurred while reading the file: {e}")

#תרגיל 4
def is_number(w):
    try:
        int(w)
        return True
    except ValueError:
        return False

even_lines = 0
sum_words = 0
sum_letters = 0
all_word = []

try:
    with open("my_text.txt","r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            words = line.split()
            if len(words) % 2 == 0:
                even_lines += 1
            word_list = [word.lower() for word in words if not is_number(word)]
            sum_words += len(word_list)
            all_word.extend(word_list)
            letter_list = [ch for ch in line if ch.isalpha()]
            sum_letters += len(letter_list)
        counter = Counter(all_word)
        popular_word, _ = counter.most_common(1)[0]
        print(f"Number of even lines: {even_lines}")
        print(f"Total number of words: {sum_words}")
        print(f"Total number of letters: {sum_letters}")
        print(f"Most popular word: {popular_word}")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")

#תרגיל 5
with open("my_text.txt","r") as f:
    with open("summary.txt","w",encoding="utf-8")as s:
        for line in f:
            line = line.strip()
            if not line:
                continue
            words_number = len(line.split())
            s.write(f"{line} ({words_number} words)\n")

#תרגיל 7
with open("sample_names.csv","r")as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        name = row[0]
        gender = row[1]
        work = row[3]
        address = row[4]
        if gender == "female":
            print(f"קוראים לי: {name} ואני גרה ב: {address} ועובדת ב: {work}")
        elif gender == "male":
            print(f"קוראים לי: {name} ואני גר ב: {address} ועובד ב: {work}")
        else:
            print("somthing went wrong")

#תרגיל 8
def get_input():
    name = input("enter your name: ").strip()
    while not name:
        name = input("name cannot be empty. please enter your name: ").strip()
    gender = input("enter your gender: ").strip()
    while gender not in ["male","female"]:
        gender = input("gender must be male or female. please enter your gender: ").strip()
    t = input("enter your title (Mr., Mrs., Ms., Dr.): ")
    while t not in ["Mr.", "Mrs.", "Ms.", "Dr."]:
        t = input("title must be Mr., Mrs., Ms., or Dr. please enter your title: ")
    work = input("enter your work: ")
    while not work:
        work = input("work cannot be empty. please enter your work: ")
    address = input("enter your address: ")
    while not address:
        address = input("address cannot be empty. please enter your address: ")
    return[name,gender,t,work,address]
def write_to_csv():
    data = get_input()
    with open("sample_names.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(data)
        print("successfull!")
write_to_csv()

#תרגיל 9
city_dict = {}
with open("sample_names.csv","r")as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        city = row[4]
        titl = row[2]
        if city not in city_dict:
            city_dict[city] = {}
        if titl not in city_dict[city]:
            city_dict[city][titl] = 0
        city_dict[city][titl] += 1
with open("city_summary.csv","w")as c:
    writer = csv.writer(c)
    writer.writerow(["City","Subject","Count"])
    for city, titles in city_dict.items():
        for title,count in titles.items():
            writer.writerow([city, title, count])




