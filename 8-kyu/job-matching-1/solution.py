def job_matching(candidate, job):
    if "min_salary" not in candidate or "max_salary" not in job:
        raise ValueError("Missing salary information")

    minimum = candidate["min_salary"] * 0.9

    return minimum <= job["max_salary"]