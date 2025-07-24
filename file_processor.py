# Python script to read a file and summarize its content
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count, lines
    except FileNotFoundError:
        return 0, []

# Read week1_summary.txt
filename = "week1_summary.txt"
line_count, content = count_lines(filename)

# Print summary
print(f"Processing file: {filename}")
print(f"Number of lines: {line_count}")
print("Content:")
for line in content:
    print(line.strip())

# Write summary to a new file
with open("summary_report.txt", 'w') as report:
    report.write(f"Summary of {filename}\n")
    report.write(f"Total lines: {line_count}\n")
    report.write("Content:\n")
    for line in content:
        report.write(line)
print("Summary saved to summary_report.txt")
