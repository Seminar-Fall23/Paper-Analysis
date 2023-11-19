from tabulate import tabulate
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import json


# Read JSON file
def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def extract_all_keywords(data):
    all_keywords = []

    for entry in data:
        if "keywords" in entry:
            keyword_groups = entry["keywords"].values()
            for keyword_list in keyword_groups:
                all_keywords.extend(keyword_list)

    return all_keywords


def paper_analysis(data):
    # Print the count of papers
    print(f"Total number of papers: {len(data)}")
    assigned = [entry.get("assigned", "") for entry in data]
    assigned_counter = Counter(assigned)
    
    for assigned, count in assigned_counter.items():
        print(f"\nAssigned Name: {assigned}")
        print(f"Number of Papers: {count}")

        # List of titles for the current assigned name
        titles_for_assigned = [entry["title"] for entry in data if entry.get("assigned", "Not Assigned") == assigned]
        
        # Print the list of titles
        print("List of Titles:")
        for title in titles_for_assigned:
            print(f"- {title}")


def keyword_analysis(array):
    keyword_counts = {}
    for keyword in array:
        keyword = keyword.lower()
        if keyword in keyword_counts:
            keyword_counts[keyword] += 1
        else:
            keyword_counts[keyword] = 1
    # Convert the dictionary to a list of tuples for tabulate
    # table = [(k, v) for k, v in keyword_counts.items() if v > 2]
    # print(tabulate(table, headers=["Keyword", "Count"], tablefmt="orgtbl"))

    count_less_than_2 = sum(1 for v in keyword_counts.values() if v < 2)
    print(f"Number of items where count is less than 2: {count_less_than_2}")
    for (
        k,
        v,
    ) in keyword_counts.items():
        if v > 2:
            print(f"[{k}], [{v}],")


def plot_publications_by_year(data):
    sns.set_theme()
    # Extract the published years from the data
    published_years = [entry["published_year"] for entry in data]

    # Count the occurrences of each year
    year_counts = Counter(published_years)

    # Sort the years for plotting
    sorted_years = sorted(year_counts.keys())

    # Prepare data for plotting
    years = [str(year) for year in sorted_years]
    counts = [year_counts[year] for year in sorted_years]

    # Create bar chart
    plt.bar(years, counts, color="blue")
    plt.xlabel("Published Year")
    plt.ylabel("Number of Publications")
    plt.title("Publications Count by Year")
    plt.show()


def create_year_analysis():
    # Improve aesthetics with seaborn
    sns.set_theme()

    # Create a bar graph
    plt.bar(published_year.keys(), published_year.values(), color="blue")

    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.title("Paper Published Year Counts")

    # Add grid
    plt.grid(True)
    plt.savefig("year_analysis.jpg", dpi=300)
    plt.show()


if __name__ == "__main__":
    data = read_json("papers.json")
    paper_analysis(data)
    all_keywords = extract_all_keywords(data)
    keyword_analysis(all_keywords)
    plot_publications_by_year(data)
    # create_year_analysis()
