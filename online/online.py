class Bug:
    def __init__(self, edge_id, bug_id, parent_bug_id, occurrences, percentage_contribution):
        self.edge_id = edge_id
        self.bug_id = bug_id
        self.parent_bug_id = parent_bug_id
        self.occurrences = occurrences
        self.percentage_contribution = percentage_contribution

    def is_leaf(self):
        return self.occurrences is not None


def read_bugs_from_file(filename):
    bugs = []
    with open(filename, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split('\t')

            edge_id = int(parts[0])
            bug_id = int(parts[1][3:])  # Remove 'bug' prefix
            parent_bug_id = -1 if parts[2] == 'null' else int(parts[2][3:])  # Remove 'bug' prefix
            occurrences = None if parts[3] == 'null' else int(parts[3])
            percentage_contribution = 0.0 if parts[4] == 'null' else float(parts[4])

            bug = Bug(edge_id, bug_id, parent_bug_id, occurrences, percentage_contribution)
            bugs.append(bug)
    return bugs




def calculate_occurrences(bugs, bug, bug_occurrences):
    if bug.bug_id in bug_occurrences:
        return

    if bug.is_leaf():
        bug_occurrences[bug.bug_id] = bug.occurrences
        return

    total_occurrences = 0
    for child in bugs:
        if child.parent_bug_id == bug.bug_id:
            calculate_occurrences(bugs, child, bug_occurrences)
            child_occurrences = bug_occurrences[child.bug_id]
            total_occurrences += (child_occurrences * child.percentage_contribution) / 100.0

    bug_occurrences[bug.bug_id] = total_occurrences


def main():
    filename = "Test_Case_Input.tsv"
    bugs = read_bugs_from_file(filename)

    bug_occurrences = {}

    for bug in bugs:
        if bug.is_leaf():
            calculate_occurrences(bugs, bug, bug_occurrences)

    most_abundant_bug = max(bug_occurrences, key=bug_occurrences.get)
    print("Most Abundant Root Bug:", most_abundant_bug)


if __name__ == "__main__":
    main()
