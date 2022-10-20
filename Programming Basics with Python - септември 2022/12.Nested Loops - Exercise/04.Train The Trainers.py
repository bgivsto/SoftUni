jury = int(input())
presentation_count = 0
total_scores = 0

while True:
    name = input()
    if name == 'Finish':
        break

    presentation_count += 1
    current_scores = 0
    for i in range(jury):
        current_scores += float(input())

    avg_score = current_scores / jury
    total_scores += current_scores

    print(f"{name} - {avg_score:.2f}.")


total_avg_score = total_scores / presentation_count / jury
print(f"Student's final assessment is {total_avg_score:.2f}.")
