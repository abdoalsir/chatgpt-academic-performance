"""
Project  : Evaluation of the Effect of ChatGPT Use on Learning and Academic Performance
Among Medical Students at Omdurman Islamic University, Sudan – 2025
Script   : Data Cleaning & Recoding
Author   : Abdulrahman Sirelkhatim
Date     : September 2025
Input    : ChatGPT_raw_data.xlsx
Output   : cleaned_data.xlsx
"""

import pandas as pd
import re
from pathlib import Path

RAW_DATA_PATH = Path("../1_data/raw/ChatGPT_raw_data.xlsx")
OUTPUT_PATH = Path("../1_data/cleaned/cleaned_data.xlsx")

df = pd.read_excel(RAW_DATA_PATH)

# Drop timestamp and consent columns
df = df.drop(
    columns=[
        "Timestamp",
        "هل أنت موافق للمشاركه في البحث— Are you agree to participate in this research؟ ",
        "Reason for avoiding ChatGPT — سبب تجنبه: ",
        "Suggestions —اقتراحات",
    ],
    errors="ignore",
)

# Rename columns to standardized English names
column_map = {
    "1. Gender — الجنس:": "Gender",
    "2. Age — العمر:": "Age",
    "3. Year in medical school — في أي سنة دراسية أنت الآن في كلية الطب؟": "Year_in_Medical_School",
    '4.أين تقيم حاليًا؟ (اختر واحدة من الخيارات التالية) / Where do you currently reside? (Choose one of the following options)"': "Current_Residency",
    ". كيف تصف مستوى دخل أسرتك الشهري؟ / How would you describe your family’s monthly income level?": "Family_Income_Level",
    "كم مرة تقيّدك القيود المالية من الوصول إلى الأجهزة أو الإنترنت المطلوبة لاستخدام ChatGPT؟ / How often do financial constraints limit your access to devices or internet required to use ChatGPT?": "Financial_Constraints_for_ChatGPT",
    "هل تواجه تحديات مالية في الحفاظ على الوصول المستقر إلى الإنترنت لأغراض الدراسة؟ / Do you face financial challenges in maintaining stable internet access for study purposes?": "Financial_Challenges_Internet_Study",
    "هل قدمت جامعتك أي توجيه رسمي حول استخدام ChatGPT للتعلم؟ / Has your university provided any official guidance on the use of ChatGPT for learning": "University_Guidance_on_ChatGPT",
    "هل يشجعك المحاضرون على استخدام ChatGPT كأداة تعليمية؟ / Do your lecturers encourage the use of ChatGPT as a learning tool?": "Lecturers_Encouragement",
    "هل توفر مؤسستك التدريب أو ورش العمل حول أدوات الذكاء الاصطناعي مثل ChatGPT؟ / Does your institution provide training or workshops on AI tools such as ChatGPT?": "Institution_Training_on_AI",
    " Do you have prior knowledge of ChatGPT? — هل لديك معرفة سابقة بـ ChatGPT؟": "Prior_Knowledge_of_ChatGPT",
    " Do you regularly use the internet for studying? — هل تستخدم الإنترنت بانتظام للدراسة؟9": "Regular_Internet_Use_for_Study",
    "Frequency of ChatGPT use for academic purposes – معدل استخدامه للأغراض الأكاديمية:": "ChatGPT_Academic_Frequency",
    " Main purposes for using ChatGPT — أهم الأغراض (اختر ما ينطبق):": "ChatGPT_Main_Purposes",
    " Do you prefer to use ChatGPT alone or with your study group? — هل تفضل استخدامه وحدك أم مع زملائك؟": "ChatGPT_Usage_Preference",
    " Devices used – الأجهزة المستخدمة:": "Devices_Used",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [ChatGPT improves my understanding of medical topics — يحسن فهمي للمواضيع الطبية]": "Perception_Understanding",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [ChatGPT helps me prepare better for exams — يساعدني على التحضير للامتحانات]": "Perception_Exam_Prep",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [ChatGPT provides accurate medical information — يقدم معلومات دقيقة]": "Perception_Accuracy",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [I verify ChatGPT answers with textbooks — أتحقق من الإجابات بالكتب]": "Perception_Verification",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [ChatGPT boosts my confidence in answering clinical questions — يزيد ثقتي في الإجابة الإكلينيكية]": "Perception_Confidence",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [     ChatGPT saves me study time — يوفر وقت المذاكرة]": "Perception_Time_Saving",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [ChatGPT encourages regular study — يشجع على المذاكرة المنتظمة]": "Perception_Study_Encouragement",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [I replaced some traditional sources with ChatGPT — استبدلت بعض المصادر التقليدية به]": "Perception_Replacement",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [ChatGPT makes learning enjoyable — يجعل التعلم ممتعاً]": "Perception_Enjoyment",
    "(Scale 1 = Strongly Disagree, 5 = Strongly Agree) [  I recommend ChatGPT to peers — أوصي زملائي باستخدامه]": "Perception_Recommendation",
    "Challenges with ChatGPT — التحديات مع ChatGPT :": "Challenges_with_ChatGPT",
}
df.rename(columns=column_map, inplace=True)


def clean_text(cell):
    """Remove Arabic script, formatting artifacts, and normalize whitespace."""
    if not isinstance(cell, str):
        return cell

    cell = re.sub(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF☐]", "", cell)
    cell = re.sub(r"[—–-]", "", cell)
    cell = re.sub(r"\s*/\s*", "", cell)
    cell = re.sub(r"\s+", " ", cell).strip(" /")

    # Preserve known multi-word categories exactly
    if "Yes, supportive" in cell:
        return "Yes, supportive"
    if "Yes, discouraging" in cell:
        return "Yes, discouraging"
    if "No official guidance" in cell:
        return "No official guidance"

    return cell.strip()


for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].apply(clean_text)

df["Challenges_with_ChatGPT"] = (
    df["Challenges_with_ChatGPT"].str.replace(r",?\s*None", "", regex=True).str.strip()
)
df["Challenges_with_ChatGPT"] = df["Challenges_with_ChatGPT"].replace(
    "", "No Challenges"
)

likert_map = {
    "Strongly Disagree": 1,
    "Strongly Disagree.": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5,
}

perception_cols = [c for c in df.columns if c.startswith("Perception_")]

for col in perception_cols:
    df[col + "_num"] = df[col].map(likert_map)

df["Perceptions_Score"] = df[[c + "_num" for c in perception_cols]].mean(axis=1)

df.to_excel(OUTPUT_PATH, index=False)
print(f"Cleaned data saved to: {OUTPUT_PATH}")
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
