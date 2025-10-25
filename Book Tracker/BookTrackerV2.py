import datetime

all_contributors = set()
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_valid_score(prompt):
    while True:
        try:
            score = int(input(prompt))
            if 1 <= score <= 10:
                return score
            else:
                print("Please enter a valid score (1 to 10)")
        except ValueError:
            print("Please enter a valid number (1 to 10)")

def get_number_of_pages():
    while True:
        try:
            pages = int(input("Please enter the page number: "))
            if pages > 0:
                return pages
            else:
                print("Please enter a positive page number!")
        except ValueError:
            print("Please enter a valid number!")

def get_daily_goal_pages():
  try:
    daily_pages_goal = int(input("Enter your daily reading goal (pages per day): "))
    if daily_pages_goal <= 0:
      daily_pages_goal = 50
      print("Invalid goal. Using default of 50 pages per day.")
    return daily_pages_goal
  except ValueError:
    daily_pages_goal = 50  # Default value
    print("Invalid input. Using default of 50 pages per day.")
    return daily_pages_goal

def get_contributors(main_author):
    global all_contributors
    # Add main author first
    all_contributors.add(main_author)

    # Get co-authors
    co_authors_input = input("Enter co-authors (comma-separated, or leave blank): ").strip()

    if co_authors_input:
        co_author_list = co_authors_input.split(',')
        for name in co_author_list:
            clean_name = name.strip().title()
            if clean_name:
                all_contributors.add(clean_name)
def calculate_days_recursively(pages_left, daily_goal):
    if daily_goal <= 0:
        return float('inf')

    if pages_left <= 0:
        return 0
    else:
        return 1 + calculate_days_recursively(pages_left - daily_goal, daily_goal)

# Main code
genre = input("Enter the Genre: ")

Challenge_rules = {
    "Fantasy": {"min_pages": 400, "required_tag": "magic"},
    "Sci-Fi": {"min_pages": 350, "required_tag": "future"},
    "Thriller": {"min_pages": 300, "required_tag": "climax"},
}
def get_load_history(filename):
    history_set = set()
    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    if "|" in line:
                        book_title = line.split("|")[0].replace("Book Title: ", "").strip()
                        history_set.add(book_title)
                except IndexError:
                    continue
    except FileNotFoundError:
        print(f"No history file found at {filename}. Starting fresh.")
    except Exception as e:
        print(f"Error reading history: {e}")
    return history_set

genre_criteria = Challenge_rules.get(genre)

if genre_criteria is not None:
    book_title = input("Enter the book title: ").capitalize()
    authors_name = input("Enter the author's name: ").title()
    number_of_pages = get_number_of_pages()
    goal_pages = get_daily_goal_pages()
    days_needed = calculate_days_recursively(number_of_pages, goal_pages)
    mini_review = input("Enter a single-sentence: ")

    # Get contributors (including main author and co-authors)
    get_contributors(authors_name)

    # Get ratings
    plot_pacing_rating = get_valid_score("Plot Pacing score(1 to 10): ")
    char_depth_score = get_valid_score("Character Depth score(1 to 10): ")
    intellectual_insight = get_valid_score("Intellectual Insight score(1 to 10): ")

    ratings = (plot_pacing_rating + char_depth_score + intellectual_insight) / 3

    score = [plot_pacing_rating, char_depth_score, intellectual_insight]
    score.sort()

    goal_difference = number_of_pages - genre_criteria["min_pages"]
    author_book = authors_name[:5] + ":" + book_title
    History = get_load_history("BookTracker.txt")

    # Print results...
    print("\nBook: ", author_book)
    print(f"Loaded {len(History)} previous reviews.")
    print(f"Page Difference from Goal ({genre_criteria['min_pages']}): {goal_difference} pages.")
    print(f"Is this book longer than the {genre_criteria['min_pages']}-page goal?", number_of_pages >= genre_criteria["min_pages"])
    print(f"At {goal_pages} pages/day, you'll need {days_needed} days to finish.")
    print("It is a highly rated book? ", ratings >= 8.0)
    print("Length of the title: ", len(book_title))
    print("Searching word find? ", genre_criteria["required_tag"] in mini_review)
    print("Individual Ratings: ", score)
    print("Lowest score: ", score[0])
    print("Highest score: ", score[-1])
    print("Total Unique Contributors: ", all_contributors)
    print("Total number of unique people involved: ", len(all_contributors))

    if ratings >= 8.0:
      final_verdict = " CRITICAL HIT! This is a high-rated, challenge-worthy read."
    elif ratings >= 6.0:
      final_verdict = " Solid Read. Meets challenge requirements, but review your weak point."
    else:
      if number_of_pages >= 400:
        final_verdict = " DANGER! Low rating + a massive book (>=400 pages). Consider skipping!"
      else:
        final_verdict = " LOW RATING WARNING. Your final score is below the threshold. Commit carefully."

    print(final_verdict)

    log_entry = f"""
    Time: {current_time}
    Book: {book_title}
    Author: {authors_name}
    Genre: {genre}
    Pages: {number_of_pages}
    Rating: {ratings:.2f}
    Days Needed: {days_needed}
    Scores: {score}
    Contributors: {', '.join(sorted(all_contributors))}
    Verdict: {final_verdict}
    {'='*50}
    """

    with open("./BookTracker.txt", "a") as file:
      file.write(log_entry)
      print("✅ Data successfully saved to BookTracker.txt!")

else:
    print("Enter a valid genre!")
