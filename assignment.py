# You can remove 'pass' if you written code in the function
# Exercise 1

def save_scores(names, scores, filename):
    file = open(filename,"w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
# Exercise 2
def average_score(filename):
    file = open(filename, "r")
    total = 0
    count = 0
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            score = int(parts[1])
            total = total + score
            count = count + 1
    file.close()
    if count == 0:
        return 0
    return round(total / count, 1)

# Exercise 3
def filter_passed(source, destination, pass_mark):
    file = open(source, "r")
    new_file = open(destination, "w")
    count = 0
    for line in file:
        line = line.strip()
        parts = line.split(",")
        name = parts[0]
        score = int(parts[1])
        if score >= pass_mark:
            new_file.write(name + "," + str(score) + "\n")
            count = count + 1
    file.close()
    new_file.close()
    return count

# Exercise 4
def replace_word(filename, old_word, new_word):
    file = open(filename, "r")
    text = file.read()
    file.close()
    if old_word not in text:
        return
    text = text.replace(old_word, new_word)
    file = open(filename, "w")
    file.write(text)
    file.close()

# Exercise 5
def remove_line(filename, line_number):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    if line_number < 1 or line_number > len(lines):
        return
    lines.pop(line_number - 1)
    file = open(filename, "w")
    for line in lines:
        file.write(line)
    file.close()
