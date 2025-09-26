# Texas Industry Analysis (CLI)

A simple, menu-driven Python program that presents Texas census and health-industry data, lets the user modify values, and calculates the impact of those changes. The app writes a clear text report to `output.txt` so results can be reviewed or shared.

## What it does
- Displays baseline Texas data:
  - Census: total population, age groups, gender, education levels, employment by industry (as percentages)
  - Health: cancer & heart disease death rates, and key industry stats (workers, revenue, hospitals, annual patients, obesity rate)
- Prompts the user to choose a category and enter a new (hypothetical) value
- Computes **difference** and **percentage change** vs. the stored value
- Appends the result to `output.txt` with a short “Impact” message
- Option to view the final report and exit

## Why I built it
This project helped me practice:
- Writing **modular code** (separate `main` and a module of functions)
- **User input** and guided prompts
- **Basic calculations** and **defensive programming** (e.g., divide-by-zero)
- **File I/O** for persistent, human-readable output
