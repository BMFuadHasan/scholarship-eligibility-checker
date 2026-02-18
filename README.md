# Scholarship Eligibility Checker

A simple, rule-based Python program that determines whether a student qualifies for a scholarship based on academic performance and eligibility criteria. The system follows **priority-based decision logic**, where GPA is evaluated before other conditions to ensure accurate and fair results.

## Features

* Automatic qualification for students with **GPA 4.0**
* GPA-first evaluation to avoid incorrect disqualification
* Attendance validation with minimum threshold rules
* Considers:

  * Extracurricular participation
  * Low-income family background
  * Disciplinary records
* Clear qualification and disqualification messages

## Eligibility Rules

A student qualifies if:

1. **GPA is 4.0** → Automatically qualified
2. Otherwise:

   * GPA must be **at least 3.5**
   * Attendance must be **60% or higher**
   * No disciplinary action
   * Attendance **80% or higher**, and at least one of:

     * Participated in extracurricular activities
     * Comes from a low-income family

## Why GPA Comes First

In earlier logic structures, low attendance could disqualify a student even if their GPA was already below the minimum requirement.
This project fixes that flaw by enforcing **GPA as the highest-priority condition**, ensuring the output reflects the correct reason for disqualification.

## How to Run

1. Make sure Python 3 is installed
2. Clone the repository
3. Run the script:

```bash
python scholarship-eligibility-checker.py
```

4. Enter the required inputs when prompted

## Example Input

```
Enter GPA: 3.2
Enter Attendance (%): 55
Participated in extracurricular activities? (yes/no): no
Low-income family? (yes/no): yes
Any disciplinary action? (yes/no): no
```

## Example Output

```
Not Qualified (GPA below 3.5)
```

## Project Structure

```
scholarship-eligibility-checker/
│
├── main.py
└── README.md
```

## Future Improvements

* Input validation
* Configurable rules using JSON or YAML
* Unit tests
* Web or GUI interface

## License

This project is open-source and free to use for educational purposes.
