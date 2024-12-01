#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

struct Bug {
    int edgeId;
    int bugId;
    int parentBugId;
    int occurrences;
    double percentageContribution;

    Bug(int edgeId, int bugId, int parentBugId, int occurrences, double percentageContribution)
        : edgeId(edgeId), bugId(bugId), parentBugId(parentBugId), occurrences(occurrences), percentageContribution(percentageContribution) {}

    bool isLeaf() {
        return occurrences != -1;
    }
};

vector<Bug> readBugsFromFile(const string& filename) {
    vector<Bug> bugs;
    ifstream file(filename);
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            if (line.find("edge_id") != string::npos) {
                continue;
            }

            istringstream iss(line);
            string token;
            vector<string> parts;
            while (getline(iss, token, '\t')) {
                parts.push_back(token);
            }

            int edgeId = stoi(parts[0]);
            int bugId = stoi(parts[1].substr(3)); // Remove "bug" prefix
            int parentBugId = (parts[2] == "null") ? -1 : stoi(parts[2].substr(3)); // Remove "bug" prefix
            int occurrences = (parts[3] == "null") ? -1 : stoi(parts[3]);
            double percentageContribution = (parts[4] == "null") ? 0.0 : stod(parts[4]);

            bugs.push_back(Bug(edgeId, bugId, parentBugId, occurrences, percentageContribution));
        }
        file.close();
    }
    return bugs;
}

void calculateOccurrences(const vector<Bug>& bugs, Bug& bug, map<int, int>& bugOccurrences) {
    if (bugOccurrences.count(bug.bugId)) {
        return;
    }

    if (bug.isLeaf()) {
        bugOccurrences[bug.bugId] = bug.occurrences;
        return;
    }

    int totalOccurrences = 0;
    for (const Bug& child : bugs) {
        if (child.parentBugId == bug.bugId) {
            calculateOccurrences(bugs, child, bugOccurrences);
            int childOccurrences = bugOccurrences[child.bugId];
            totalOccurrences += (childOccurrences * child.percentageContribution) / 100.0;
        }
    }
    bugOccurrences[bug.bugId] = totalOccurrences;
}

int main() {
    string filename = "Test_Case_Input.tsv";
    vector<Bug> bugs = readBugsFromFile(filename);

    map<int, int> bugOccurrences;
    for (const Bug& bug : bugs) {
        if (bug.isLeaf()) {
            calculateOccurrences(bugs, bug, bugOccurrences);
        }
    }

    int maxOccurrences = 0;
    int mostAbundantBug = -1;
    for (const auto& entry : bugOccurrences) {
        int bugId = entry.first;
        int occurrences = entry.second;
        if (occurrences > maxOccurrences) {
            maxOccurrences = occurrences;
            mostAbundantBug = bugId;
        }
    }

    cout << "Most Abundant Root Bug: " << mostAbundantBug << endl;

    return 0;
}
