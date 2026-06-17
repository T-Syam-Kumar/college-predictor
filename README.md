## APEAMCET College & Branch Predictor

A Streamlit-based web application that predicts eligible colleges and branches for APEAMCET aspirants based on their rank, region, gender, and caste using previous year cutoff data.

Features

-  Predict expected colleges & branches

-  Check feasibility of a selected college + branch

-  Show Top 5 best colleges if not feasible

-  Dropdown inputs (no typing errors)

-  Uses previous year cutoff ranks

-  Clean Streamlit UI

-  Deployed online using Streamlit Cloud

🗂️ Project Structure

college_predictor/
│
├── app.py                  # Streamlit UI
├── predictor_logic.py      # Core prediction logic
├── data_loader.py          # Dataset loading & cleaning
├── APEAMCET2024_FINAL.csv  # Previous year cutoff dataset
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

## How It Works

User enters: Rank

Region (AU / SVU / SW)

Gender (BOYS / GIRLS)

Caste (OC / SC / ST / BCA / BCB / BCC / BCD / BCE / OC_EWS)

Preferred College (optional)

Preferred Branch (optional)

System:

Filters previous year cutoffs

Shows expected colleges & branches

Checks feasibility of selected college + branch

If not feasible → shows Top 5 alternatives
