# ChatGPT Use and Academic Performance Among Medical Students

## Omdurman Islamic University, Sudan – 2025

**Study type:** Cross-sectional descriptive study
**Degree level:** MBBS
**Institution:** Faculty of Medicine, Omdurman Islamic University
**Sample size:** N = 295 medical students (2nd–5th year)
**Data analyst:** Abdulrahman Sirelkhatim

---

## Background

The rapid adoption of AI tools like ChatGPT has reached medical education
globally, yet its actual impact on student learning and academic performance
remains poorly studied — particularly in low-resource settings. In Sudan, where
traditional educational infrastructures were further disrupted by conflict
beginning in 2023, medical students increasingly rely on digital tools to fill
instructional gaps.

This study was conducted at Omdurman Islamic University's Faculty of Medicine to
evaluate how ChatGPT use relates to learning behaviors and perceived academic
benefit, and to identify the factors that drive or limit its adoption among
Sudanese medical students.

## Objectives

- Assess levels of ChatGPT awareness, usage frequency, and purpose among medical
students
- Identify sociodemographic, economic, and institutional factors influencing
adoption
- Examine the relationship between ChatGPT use and students' perceived academic
benefit
- Determine predictors of being a frequent ChatGPT user

## Study Design & Methods

| Component | Detail |
|-----------|--------|
| Design | Cross-sectional, facility-based |
| Setting | Omdurman Islamic University, Faculty of Medicine |
| Population | Medical students, academic years 2–5, 2025 |
| Sampling | Stratified by academic year and gender |
| Sample size calculation | 95% CI, 5% margin, population = 1,241 → n = 294 |
| Data collection | Self-administered online questionnaire via Google Forms |
| Data entry | Microsoft Excel |

**Technical suite:**

| Tool | Purpose |
|------|---------|
| Python (pandas, re) | Data cleaning, column renaming, Arabic text stripping |
| IBM SPSS Statistics v26 | Full statistical analysis |
| Python (matplotlib, seaborn) | Figure generation |
| Jupyter Notebook | Exploratory data analysis |

**Statistical methods:**

- **Reliability analysis:** Cronbach's Alpha for the 10-item perceptions scale
- **Descriptive statistics:** Frequencies, percentages, means, standard
deviations
- **Bivariate analysis:** Independent samples t-tests, one-way ANOVA, Chi-square
 tests
- **Correlation:** Pearson correlation (frequency vs. perceptions score);
inter-item correlation matrix
- **Multivariate analysis:** Multiple linear regression (predictors of
perceptions score); binary logistic regression (predictors of frequent use)

## Dataset

| File | Description |
|------|-------------|
| `1_data/raw/ChatGPT_raw_data.xlsx` | Raw survey responses (bilingual Arabic/English) |
| `1_data/cleaned/cleaned_coded_data.xlsx` | Cleaned data with recoded numeric variables and binary dummy columns |

The questionnaire captured demographics, institutional factors, ChatGPT usage
patterns, a 10-item Likert perceptions scale, and open-ended challenges and
suggestions.

> **Note:** No individual identifiers are present in either dataset. The raw
file contains Arabic-language column headers; the cleaning script standardizes
these to English.

## Repository Structure

```text
chatgpt-academic-performance/
│
├── README.md
├── .gitignore
├── .ls-lint.yml
├── .markdownlint.yml
├── .markdownlintignore
│
├── .github/
│   └── workflows/
│       └── ci-checks.yml
│
├── 1_data/
│   ├── raw/            ← excluded from version control (privacy)
│   └── cleaned/
│       └── cleaned_coded_data.xlsx
│
├── 2_cleaning/
│   └── cleaning.py
│
├── 3_notebooks/
│   └── exploratory_analysis.ipynb
│
├── 4_analysis/
│   ├── full_analysis.sps
│   └── figures.py
│
├── 5_figures/
│   ├── fig01_gender_distribution.png
│   ├── fig02_age_distribution.png
│   └── ... (16 figures total)
│
└── 6_docs/
    └── results_chapter.docx
```

## Key Results

### Reliability

The 10-item perceptions scale demonstrated excellent internal consistency
(Cronbach's α = 0.919), well above the 0.70 threshold, supporting its use as a
composite outcome measure.

### Who uses ChatGPT and how

- 80% of students were frequent users (daily: 45.8%; several times/week: 34.2%)
- 93.2% reported being "well acquainted" with ChatGPT before the study
- 82% preferred using it independently rather than in study groups
- Primary purposes: explaining difficult concepts (85.1%), language support
(65.4%), and answering clinical questions (57.3%)
- Most common challenges: accuracy doubts (73.9%) and over-reliance concerns
(63.4%)

### Institutional context

- 83.4% of students reported no official university guidance on ChatGPT use
- 93.2% had never received institutional training on AI tools
- Nearly half (49.2%) said their lecturers had never encouraged ChatGPT use

### Perceptions of academic benefit

Students generally viewed ChatGPT positively (mean perceptions score: 3.44 ±
0.88 on a 5-point scale). The strongest agreement was for
*"ChatGPT improves my understanding of medical topics"* (mean 3.82).
Students were most cautious about *"ChatGPT provides accurate medical
information"* (mean 3.10), suggesting appropriate critical thinking about
reliability.

### Bivariate findings

- Students with regular internet use for studying had significantly higher
perceptions scores than those without (mean 3.52 vs. 2.95, p < 0.001)
- Students who received institutional AI training actually reported *lower*
perceptions scores (mean 2.99 vs. 3.47, p = 0.016) — suggesting formal training
may emphasize limitations and ethical concerns
- Second-year students showed the highest rate of daily ChatGPT use (72.0%),
with significant differences across academic years (χ² = 24.315, p = 0.004)

### Correlation

ChatGPT usage frequency correlated positively with overall perceptions score
(r = 0.283, p < 0.001): students who use it more frequently perceive greater
academic benefit.

### Multiple linear regression — predictors of perceptions score

**Model fit:** R² = 0.106 (p < 0.001)

| Predictor | β | Direction | p-value |
|-----------|---|-----------|---------|
| ChatGPT Academic Frequency | 0.243 | Positive | < 0.001 |
| Regular Internet Use | 0.164 | Positive | 0.004 |
| Gender | −0.018 | — | 0.746 |
| Year in Medical School | −0.014 | — | 0.853 |

### Binary logistic regression — predictors of frequent use

**Model fit:** χ²(9) = 35.915, p < 0.001; Nagelkerke R² = 0.181; correctly
classified 82.0%

| Predictor | OR | 95% CI | Interpretation |
|-----------|----|--------|----------------|
| Prior Knowledge | 7.113 | 2.587–19.016 | Well-acquainted students are >7× more likely to be frequent users |
| Age | 0.140 | 0.034–0.584 | Older students less likely to be frequent users |
| Financial challenges for internet | 0.435 | 0.258–0.910 | Financial barriers reduce odds of frequent use by ~56% |
| Lecturer encouragement | 1.516 | 1.063–2.249 | Encouragement increases odds by ~52% |

## Selected Figures

**Perceptions Scale – Likert Distribution**
![Perceptions Likert Chart](figures/fig08_perceptions_likert_diverging.png)

**Correlation Heatmap – 10-Item Perceptions Scale**
![Correlation Heatmap](figures/fig10_correlation_heatmap.png)

**Predictors of Frequent ChatGPT Use – Forest Plot**
![Forest Plot](figures/fig15_logistic_regression_forest_plot.png)

## Limitations

- **No objective performance data:** GPA and exam scores were unavailable.
The study relied on a validated perceptions composite as a proxy for academic
benefit. Findings reflect subjective perceptions, not confirmed performance
changes.
- **Self-report bias:** Students may over- or under-report ChatGPT use and its
perceived effects.
- **Convenience sampling:** Despite stratification, results may not generalize
beyond OIU students.
- **Cross-sectional design:** Causal relationships between ChatGPT use and
academic outcomes cannot be established.

## Files

| Script | Purpose |
|--------|---------|
| `cleaning/cleaning.py` | Data cleaning and recoding |
| `analysis/figures.py` | Figure generation |
| `analysis/Full_Analysis.sps` | Full SPSS syntax |
| `notebooks/exploratory_analysis.ipynb` | EDA |

---

**Data analyst:** Abdulrahman Sirelkhatim | Analysis conducted September 2025
