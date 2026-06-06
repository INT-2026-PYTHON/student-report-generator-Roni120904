"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    students ={}
    for record in records:
        name=record["name"]
        score=record["score"]

        students.setdefault(name,[]).append(score) #setdefault() is a dictionary method. It checks whether a key exists in the dictionary. If the key exists, it returns the value of that key. If the key does not exist, it creates the key with a default value and then returns that value.
    
    averages = {}

    for name,scores in students.items():
        averages[name] = round(sum(scores)/len(scores),2)
    
    return averages


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    
    return {r["subject"] for r in records}  # it is a set and returns only unique


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    
    averages= average_per_student(records)
    return max(averages.items(), key=lambda kv: kv[1]) # it finds the tuple with largest value at index 1(the average score)


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    averages=average_per_student(records)

    result=[]

    for name,avg in averages.items():
        if avg>= threshold:
            result.append(name)
    
    return sorted(result)
