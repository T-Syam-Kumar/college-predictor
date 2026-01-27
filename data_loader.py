import pandas as pd

def load_data():
    df = pd.read_csv("APEAMCET2024_FINAL.csv")

    cutoff_cols = [
        "OC_BOYS","OC_GIRLS","SC_BOYS","SC_GIRLS","ST_BOYS","ST_GIRLS",
        "BCA_BOYS","BCA_GIRLS","BCB_BOYS","BCB_GIRLS","BCC_BOYS","BCC_GIRLS",
        "BCD_BOYS","BCD_GIRLS","BCE_BOYS","BCE_GIRLS","OC_EWS_BOYS","OC_EWS_GIRLS"
    ]

    for col in cutoff_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

