from data_loader import load_data

df = load_data()

def get_cutoff_column(caste, gender):
    return f"{caste}_{gender.upper()}"

# -------------------------------
# Expected colleges & branches
# -------------------------------
def get_expected_colleges(user_rank, caste, gender, region):
    cutoff_col = get_cutoff_column(caste, gender)

    filtered = df[
        (df["INST_REG"] == region) &
        (df[cutoff_col] >= user_rank)
    ]

    result = filtered.sort_values(by=cutoff_col)

    return result[["NAME OF THE INSTITUTION", "branch_code", cutoff_col]]

# -------------------------------
# Check selected college + branch
# -------------------------------
def check_selected_college(user_rank, caste, gender, college_name, branch_code):
    cutoff_col = get_cutoff_column(caste, gender)

    row = df[
        (df["NAME OF THE INSTITUTION"] == college_name) &
        (df["branch_code"] == branch_code)
    ]

    if row.empty:
        return False, "❌ College or branch not found in dataset."

    cutoff = row.iloc[0][cutoff_col]

    if user_rank <= cutoff:
        return True, f"✅ YES! You CAN get {branch_code} in {college_name} (Last Rank: {cutoff})"
    else:
        return False, f"❌ NO! You CANNOT get {branch_code} in {college_name} (Last Rank: {cutoff})"

# -------------------------------
# Top 5 colleges + branches
# -------------------------------
def get_top5_colleges(user_rank, caste, gender, region):
    cutoff_col = get_cutoff_column(caste, gender)

    filtered = df[
        (df["INST_REG"] == region) &
        (df[cutoff_col] >= user_rank)
    ]

    top5 = filtered.sort_values(by=cutoff_col).head(5)

    return top5[["NAME OF THE INSTITUTION", "branch_code", cutoff_col]]
