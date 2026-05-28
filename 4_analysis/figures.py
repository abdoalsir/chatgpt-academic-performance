"""
Project  : Evaluation of the Effect of ChatGPT Use on Learning and Academic Performance
Among Medical Students at Omdurman Islamic University, Sudan – 2025
Script   : Figure Generation
Author   : Abdulrahman Sirelkhatim
Date     : September 2025
Input    : data/cleaned/cleaned_coded_data.xlsx
Output   : figures/ directory (PNG, 300 DPI)

Figures produced:
fig01_gender_distribution.png
fig02_age_distribution.png
fig03_academic_year_distribution.png
fig04_family_income_distribution.png
fig05_chatgpt_usage_frequency.png
fig06_challenges_with_chatgpt.png
fig07_perceptions_score_by_user_status.png
fig08_perceptions_likert_diverging.png
fig09_purposes_of_chatgpt_use.png
fig10_correlation_heatmap.png
fig11_perceptions_by_internet_use.png
fig12_perceptions_by_institutional_training.png
fig13_perceptions_by_prior_knowledge.png
fig14_year_by_usage_frequency.png
fig15_logistic_regression_forest_plot.png
fig16_frequency_vs_perceptions_scatter.png
"""

import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from pathlib import Path

warnings.filterwarnings("ignore")

DATA_PATH = Path("../1_data/cleaned/cleaned_data.xlsx")
FIGURES_DIR = Path("../5_figures/")

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 12
plt.rcParams["figure.dpi"] = 200

PALETTE = sns.color_palette("Set2")
DIVERGING_COLORS = ["#d73027", "#fc8d59", "#cccccc", "#91bfdb", "#4575b4"]

PERCEPTION_NUM_COLS = [
    "Perception_Understanding_num",
    "Perception_Exam_Prep_num",
    "Perception_Accuracy_num",
    "Perception_Verification_num",
    "Perception_Confidence_num",
    "Perception_Time_Saving_num",
    "Perception_Study_Encouragement_num",
    "Perception_Replacement_num",
    "Perception_Enjoyment_num",
    "Perception_Recommendation_num",
]
PERCEPTION_SHORT_LABELS = [
    "Improves Understanding",
    "Prepares for Exams",
    "Provides Accurate Info",
    "Verify Answers (Textbooks)",
    "Boosts Confidence",
    "Saves Study Time",
    "Encourages Regular Study",
    "Replaced Traditional Sources",
    "Makes Learning Enjoyable",
    "Recommends to Peers",
]
PERCEPTION_CORR_LABELS = [
    "Understanding",
    "Exam Prep",
    "Accuracy",
    "Verification",
    "Confidence",
    "Time Saving",
    "Study Encouragement",
    "Replacement",
    "Enjoyment",
    "Recommendation",
]


def save_fig(fig, filename):
    fig.savefig(FIGURES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {filename}")


# --- Load and prepare data ---
df = pd.read_excel(DATA_PATH)

for col in PERCEPTION_NUM_COLS:
    df[col] = pd.to_numeric(df[col], errors="coerce")

if "Perceptions_Score" not in df.columns:
    df["Perceptions_Score"] = df[PERCEPTION_NUM_COLS].mean(axis=1)

freq_map = {"Rarely": 1, "Weekly": 2, "Several times a week": 3, "Daily": 4}
if "ChatGPT_Freq_num" not in df.columns:
    df["ChatGPT_Freq_num"] = df["ChatGPT_Academic_Frequency"].map(freq_map)

df["User_Status"] = df["ChatGPT_Academic_Frequency"].isin(
    ["Daily", "Several times a week"]
)
df["User_Status"] = df["User_Status"].map(
    {True: "Frequent User", False: "Infrequent User"}
)

df["ChatGPT_Main_Purposes"] = (
    df["ChatGPT_Main_Purposes"]
    .astype(str)
    .str.split(",")
    .apply(lambda x: [i.strip().replace("()", "").strip() for i in x])
)
df["Challenges_with_ChatGPT"] = (
    df["Challenges_with_ChatGPT"]
    .astype(str)
    .str.split(",")
    .apply(lambda x: [i.strip() for i in x])
)


# --- Figures 1–4: Demographics (pie charts) ---
demo_configs = [
    ("Gender", "fig01_gender_distribution.png", "Gender Distribution"),
    ("Age", "fig02_age_distribution.png", "Age Distribution"),
    (
        "Year_in_Medical_School",
        "fig03_academic_year_distribution.png",
        "Academic Year Distribution",
    ),
    (
        "Family_Income_Level",
        "fig04_family_income_distribution.png",
        "Family Income Level Distribution",
    ),
]
for col, filename, title in demo_configs:
    fig, ax = plt.subplots()
    counts = df[col].value_counts()
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%", colors=PALETTE)
    ax.set_title(title)
    save_fig(fig, filename)


# --- Figure 5: ChatGPT academic usage frequency ---
freq_order = ["Daily", "Several times a week", "Weekly", "Rarely"]
fig, ax = plt.subplots(figsize=(7, 4))
freq_counts = df["ChatGPT_Academic_Frequency"].value_counts().reindex(freq_order)
sns.barplot(x=freq_counts.index, y=freq_counts.values, palette="dark", ax=ax)
ax.set_ylabel("Number of Students")
ax.set_xlabel("Frequency")
ax.set_title(f"ChatGPT Academic Usage Frequency (N={len(df)})")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "fig05_chatgpt_usage_frequency.png")


# --- Figure 6: Challenges with ChatGPT ---
fig, ax = plt.subplots(figsize=(8, 4))
challenges_df = df.explode("Challenges_with_ChatGPT").dropna(
    subset=["Challenges_with_ChatGPT"]
)
challenge_counts = challenges_df["Challenges_with_ChatGPT"].value_counts()
challenge_counts.plot(kind="barh", ax=ax, color=sns.color_palette("dark"))
ax.set_xlabel("Number of Respondents")
ax.set_title(f"Reported Challenges with ChatGPT (N={len(df)})")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "fig06_challenges_with_chatgpt.png")


# --- Figure 7: Perceptions score by user status (boxplot) ---
fig, ax = plt.subplots(figsize=(6, 5))
sns.boxplot(x="User_Status", y="Perceptions_Score", data=df, palette="coolwarm", ax=ax)
ax.set_xlabel("User Status")
ax.set_ylabel("Overall Perceptions Score")
ax.set_title("Perceptions Score by ChatGPT Usage Frequency")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "fig07_perceptions_score_by_user_status.png")


# --- Figure 8: Diverging Likert chart for perceptions scale ---
# Compute response percentages per item directly from the data
likert_map = {1: "SD", 2: "D", 3: "N", 4: "A", 5: "SA"}
likert_pct = {}
for col in PERCEPTION_NUM_COLS:
    counts = df[col].value_counts(normalize=True) * 100
    likert_pct[col] = {
        likert_map.get(k, str(k)): counts.get(k, 0.0) for k in range(1, 6)
    }

df_likert = pd.DataFrame(likert_pct).T
df_likert.index = PERCEPTION_SHORT_LABELS

df_likert["N_Right"] = df_likert["N"] / 2
df_likert["N_Left_Plot"] = -df_likert["N"] / 2
df_likert["D_Plot"] = -df_likert["D"]
df_likert["SD_Plot"] = -df_likert["SD"]
df_likert["left_D"] = df_likert["N_Left_Plot"]
df_likert["left_SD"] = df_likert["N_Left_Plot"] + df_likert["D_Plot"]
df_likert["left_A"] = df_likert["N_Right"]
df_likert["left_SA"] = df_likert["N_Right"] + df_likert["A"]

legend_labels = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
fig, ax = plt.subplots(figsize=(12, 7))
ax.barh(df_likert.index, df_likert["N_Left_Plot"], left=0, color=DIVERGING_COLORS[2])
ax.barh(
    df_likert.index,
    df_likert["D_Plot"],
    left=df_likert["left_D"],
    color=DIVERGING_COLORS[1],
    label=legend_labels[1],
)
ax.barh(
    df_likert.index,
    df_likert["SD_Plot"],
    left=df_likert["left_SD"],
    color=DIVERGING_COLORS[0],
    label=legend_labels[0],
)
ax.barh(
    df_likert.index,
    df_likert["N_Right"],
    color=DIVERGING_COLORS[2],
    label=legend_labels[2],
)
ax.barh(
    df_likert.index,
    df_likert["A"],
    left=df_likert["left_A"],
    color=DIVERGING_COLORS[3],
    label=legend_labels[3],
)
ax.barh(
    df_likert.index,
    df_likert["SA"],
    left=df_likert["left_SA"],
    color=DIVERGING_COLORS[4],
    label=legend_labels[4],
)
ax.set_xlim(-60, 60)
ax.xaxis.set_major_formatter(lambda x, pos: f"{abs(x):.0f}%")
ax.axvline(0, color="black", linewidth=1.0)
ax.set_xlabel("Percentage of Respondents")
ax.tick_params(axis="y", length=0)
ax.legend(
    loc="upper center", bbox_to_anchor=(0.5, 1.07), ncol=5, frameon=False, fontsize=10
)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.invert_yaxis()
plt.tight_layout(rect=[0, 0, 1, 0.98])
save_fig(fig, "fig08_perceptions_likert_diverging.png")


# --- Figure 9: Purposes of ChatGPT use ---
fig, ax = plt.subplots(figsize=(8, 5))
purposes_df = df.explode("ChatGPT_Main_Purposes").dropna(
    subset=["ChatGPT_Main_Purposes"]
)
purposes_df = purposes_df[purposes_df["ChatGPT_Main_Purposes"].str.strip() != ""]
purpose_counts = purposes_df["ChatGPT_Main_Purposes"].value_counts()
bars = ax.barh(
    purpose_counts.index[::-1], purpose_counts.values[::-1], color="steelblue"
)
for bar in bars:
    w = bar.get_width()
    ax.text(
        w + 2, bar.get_y() + bar.get_height() / 2, str(int(w)), va="center", fontsize=9
    )
ax.set_xlabel("Number of Students")
ax.set_title(f"Purposes of ChatGPT Use Among Medical Students (N={len(df)})")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
save_fig(fig, "fig09_purposes_of_chatgpt_use.png")


# --- Figure 10: Correlation heatmap for perceptions scale ---
corr_df = df[PERCEPTION_NUM_COLS].corr()
corr_df.index = PERCEPTION_CORR_LABELS
corr_df.columns = PERCEPTION_CORR_LABELS

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="viridis", linewidths=0.5, ax=ax)
ax.set_title(
    f"Inter-Item Correlation Heatmap – ChatGPT Perceptions Scale (N={len(df)})",
    fontsize=11,
)
plt.tight_layout()
save_fig(fig, "fig10_correlation_heatmap.png")


# --- Figures 11–13: Perceptions score by grouping variables (boxplots) ---
grouping_configs = [
    (
        "Regular_Internet_Use_for_Study",
        "fig11_perceptions_by_internet_use.png",
        f"Perceptions Score by Regular Internet Use for Study (N={len(df)})",
    ),
    (
        "Institution_Training_on_AI",
        "fig12_perceptions_by_institutional_training.png",
        f"Perceptions Score by Institutional AI Training (N={len(df)})",
    ),
    (
        "Prior_Knowledge_of_ChatGPT",
        "fig13_perceptions_by_prior_knowledge.png",
        f"Perceptions Score by Prior Knowledge of ChatGPT (N={len(df)})",
    ),
]
for col, filename, title in grouping_configs:
    fig, ax = plt.subplots(figsize=(7, 5))
    order = df[col].value_counts().index.tolist()
    sns.boxplot(
        x=col, y="Perceptions_Score", data=df, palette="Set2", order=order, ax=ax
    )
    ax.set_xlabel(col.replace("_", " "))
    ax.set_ylabel("Perceptions Score")
    ax.set_title(title)
    ax.tick_params(axis="x", rotation=15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    save_fig(fig, filename)


# --- Figure 14: ChatGPT usage frequency by academic year (grouped bar) ---
year_order = ["Second year", "Third year", "Fourth year", "Fifth year"]
freq_order_short = ["Daily", "Several times a week", "Weekly", "Rarely"]

df_year = df[df["Year_in_Medical_School"].isin(year_order)]
ct = pd.crosstab(
    df_year["Year_in_Medical_School"], df_year["ChatGPT_Academic_Frequency"]
)
ct = ct.reindex(index=year_order, columns=freq_order_short, fill_value=0)

fig, ax = plt.subplots(figsize=(9, 5))
ct.plot(kind="bar", ax=ax, color=sns.color_palette("Set2", 4))
ax.set_ylabel("Number of Students")
ax.set_xlabel("Academic Year")
ax.set_title("ChatGPT Usage Frequency by Academic Year (p=0.004)")
ax.legend(title="Frequency", bbox_to_anchor=(1.01, 1), loc="upper left")
plt.xticks(rotation=0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
save_fig(fig, "fig14_year_by_usage_frequency.png")


# --- Figure 15: Forest plot from logistic regression on frequent use ---
# Encode binary outcome: frequent = Daily or Several times a week
df_reg = df.copy()
df_reg["Frequent_Use"] = (
    df_reg["ChatGPT_Academic_Frequency"]
    .isin(["Daily", "Several times a week"])
    .astype(int)
)

# Encode predictors
le = LabelEncoder()
predictor_cols = [
    "Prior_Knowledge_of_ChatGPT",
    "Age",
    "Financial_Constraints_for_ChatGPT",
    "Lecturers_Encouragement",
]
for col in predictor_cols:
    df_reg[col + "_enc"] = le.fit_transform(df_reg[col].astype(str))

enc_cols = [c + "_enc" for c in predictor_cols]
mask = df_reg[enc_cols + ["Frequent_Use"]].notnull().all(axis=1)
X = df_reg.loc[mask, enc_cols].values
y = df_reg.loc[mask, "Frequent_Use"].values

model = LogisticRegression(max_iter=500)
model.fit(X, y)
coefs = model.coef_[0]
ors = np.exp(coefs)

# 95% CI via bootstrap (n=500)
rng = np.random.default_rng(42)
boot_ors = []
for _ in range(500):
    idx = rng.integers(0, len(X), len(X))
    try:
        m = LogisticRegression(max_iter=200).fit(X[idx], y[idx])
        boot_ors.append(np.exp(m.coef_[0]))
    except Exception:
        continue
boot_ors = np.array(boot_ors)
ci_lower = np.percentile(boot_ors, 2.5, axis=0)
ci_upper = np.percentile(boot_ors, 97.5, axis=0)

short_labels = [
    "Prior Knowledge",
    "Age",
    "Financial Constraints",
    "Lecturer Encouragement",
]
fig, ax = plt.subplots(figsize=(7, 4))
ax.errorbar(
    ors,
    short_labels,
    xerr=[ors - ci_lower, ci_upper - ors],
    fmt="o",
    color="steelblue",
    capsize=5,
    markersize=7,
)
ax.axvline(1, color="red", linestyle="--", linewidth=1)
ax.set_xlabel("Odds Ratio (95% CI)")
ax.set_title("Predictors of Frequent ChatGPT Use – Logistic Regression")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
save_fig(fig, "fig15_logistic_regression_forest_plot.png")


# --- Figure 16: Usage frequency vs perceptions score (scatter + regression line) ---
plot_df = df[["ChatGPT_Freq_num", "Perceptions_Score"]].dropna()
fig, ax = plt.subplots(figsize=(7, 5))
sns.regplot(
    x="ChatGPT_Freq_num",
    y="Perceptions_Score",
    data=plot_df,
    ax=ax,
    scatter_kws={"alpha": 0.4},
    line_kws={"color": "red"},
)
r = plot_df["ChatGPT_Freq_num"].corr(plot_df["Perceptions_Score"])
ax.set_xlabel("ChatGPT Academic Frequency (1=Rarely → 4=Daily)")
ax.set_ylabel("Perceptions Score")
ax.set_title(
    f"ChatGPT Usage Frequency vs Overall Perceptions Score\n(r={r:.3f}, N={len(plot_df)})"
)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "fig16_frequency_vs_perceptions_scatter.png")

print("\nAll figures saved to:", FIGURES_DIR)
