"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students
from .stats import(
    average_per_student,subjects_offered,
    top_scorer,passing_students
) # DOT(.) MEANS IMPORT FROM CURRENT PACKAGE

def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    averages= average_per_student(records)
    
    subjects=sorted(subjects_offered(records))
    
    top_name,top_avg=top_scorer(records)

    passing=passing_students(records)

    report = "=== Gradebook Report ===\n"

    report += f"Total records: {len(records)}\n"

    report += "Subjects offered: "

    report +=", ".join(subjects)

    report +="\n\nAverages: \n"

    for name in sorted(averages):
        report +=f" {name} : {averages[name]}\n"
        
    report +=f"\nTop scorer: {top_name} ({top_avg})\n"

    report +="Passing students (>=60.0): "
    report +=", ".join(passing)

    return report