# Dictionary to store candidate names and their votes
candidates = {}

# Voting process
while True:
    print("1. Add a candidate")
    print("2. Vote for a candidate")
    print("3. Display results")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        candidate_name = input("Enter candidate name: ")
        candidates[candidate_name] = 0
        print("Candidate", candidate_name, "added successfully.")

    elif choice == "2":
        candidate_name = input("Enter candidate name to vote for: ")
        if candidate_name in candidates:
            candidates[candidate_name] += 1
            print("Vote for", candidate_name, "recorded.")
        else:
            print("Candidate not found.")

    elif choice == "3":
        print("Candidate\tVotes")
        for candidate, votes in candidates.items():
            print(candidate + ":\t" + str(votes))

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
