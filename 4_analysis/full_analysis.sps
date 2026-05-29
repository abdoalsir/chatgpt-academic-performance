* Encoding: UTF-8.
* Update files paths before running.

GET DATA
  /TYPE=XLSX
  /FILE='C:\Users\Abdulrhman Alsir\Desktop\portfolio\chatgpt-academic-performance\1_data\cleaned\cleaned_data.xlsx'
  /SHEET=name 'Sheet1'
  /READNAMES = ON.
CACHE.
EXECUTE.

RECODE Gender ('Male' = 1) ('Female' = 2) INTO Gender_num.
VARIABLE LABELS Gender_num 'Gender (Recoded)'.
VALUE LABELS Gender_num 1 'Male' 2 'Female'.

RECODE Age ('Under 20 years 20' = 1) ('Between 20 and 24 years 20 24' = 2) ('30 years or older 30' = 3) INTO Age_num.
VARIABLE LABELS Age_num 'Age (Recoded)'.
VALUE LABELS Age_num 1 'Under 20 years' 2 'Between 20 and 24 years' 3 '30 years or older'.

RECODE Year_in_Medical_School ('Second year' = 2) ('Third year' = 3) ('Fourth year' = 4) ('Fifth year' = 5) INTO Year_num.
VARIABLE LABELS Year_num 'Year in Medical School (Recoded)'.
VALUE LABELS Year_num 2 'Second year' 3 'Third year' 4 'Fourth year' 5 'Fifth year'.

RECODE Current_Residency ('Khartoum' = 1) ('Omdurman' = 2) ('Another city in Sudan' = 3) ('Outside Sudan' = 4) INTO Residency_num.
VARIABLE LABELS Residency_num 'Current Residency (Recoded)'.
VALUE LABELS Residency_num 1 'Khartoum' 2 'Omdurman' 3 'Another city in Sudan' 4 'Outside Sudan'.

RECODE Family_Income_Level ('High' = 3) ('Moderate' = 2) ('Low' = 1) INTO Income_num.
VARIABLE LABELS Income_num 'Family Income Level (Recoded)'.
VALUE LABELS Income_num 1 'Low' 2 'Moderate' 3 'High'.

RECODE Financial_Constraints_for_ChatGPT ('Frequently' = 4) ('Occasionally' = 3) ('Rarely' = 2) ('Never' = 1) INTO ChatGPT_Fin_Constraints_num.
VARIABLE LABELS ChatGPT_Fin_Constraints_num 'Financial Constraints for ChatGPT (Recoded)'.
VALUE LABELS ChatGPT_Fin_Constraints_num 4 'Frequently' 3 'Occasionally' 2 'Rarely' 1 'Never'.

RECODE Financial_Challenges_Internet_Study ('Yes' = 1) ('No' = 0) INTO Internet_Fin_Challenges_num.
VARIABLE LABELS Internet_Fin_Challenges_num 'Financial Challenges for Internet (Recoded)'.
VALUE LABELS Internet_Fin_Challenges_num 1 'Yes' 0 'No'.

RECODE University_Guidance_on_ChatGPT ('Yes, supportive' = 1) ('Yes, discouraging' = 2) ('No official guidance' = 3) INTO Uni_Guidance_num.
VARIABLE LABELS Uni_Guidance_num 'University Guidance on ChatGPT (Recoded)'.
VALUE LABELS Uni_Guidance_num 1 'Supportive' 2 'Discouraging' 3 'No official guidance'.

RECODE Lecturers_Encouragement ('Always' = 4) ('Sometimes' = 3) ('Rarely' = 2) ('Never' = 1) INTO Lecturers_Encouragement_num.
VARIABLE LABELS Lecturers_Encouragement_num 'Lecturers Encouragement (Recoded)'.
VALUE LABELS Lecturers_Encouragement_num 4 'Always' 3 'Sometimes' 2 'Rarely' 1 'Never'.

RECODE Institution_Training_on_AI ('Yes' = 1) ('No' = 0) INTO Institution_Training_num.
VARIABLE LABELS Institution_Training_num 'Institution Training on AI (Recoded)'.
VALUE LABELS Institution_Training_num 1 'Yes' 0 'No'.

RECODE Prior_Knowledge_of_ChatGPT ('Yes, I am well acquainted with it' = 3) ('I have only heard about it' = 2) ('No, I do not know anything about it' = 1) INTO Prior_Knowledge_num.
VARIABLE LABELS Prior_Knowledge_num 'Prior Knowledge of ChatGPT (Recoded)'.
VALUE LABELS Prior_Knowledge_num 3 'Well Acquainted' 2 'Heard About it' 1 'No Knowledge'.

RECODE Regular_Internet_Use_for_Study ('Yes' = 1) ('No' = 0) INTO Reg_Internet_Use_num.
VARIABLE LABELS Reg_Internet_Use_num 'Regular Internet Use (Recoded)'.
VALUE LABELS Reg_Internet_Use_num 1 'Yes' 0 'No'.

RECODE ChatGPT_Academic_Frequency ('Daily' = 4) ('Several times a week' = 3) ('Weekly' = 2) ('Rarely' = 1) INTO ChatGPT_Freq_num.
VARIABLE LABELS ChatGPT_Freq_num 'ChatGPT Academic Frequency (Recoded)'.
VALUE LABELS ChatGPT_Freq_num 4 'Daily' 3 'Several times a week' 2 'Weekly' 1 'Rarely'.

RECODE ChatGPT_Usage_Preference ('Alone' = 1) ('With group' = 2) INTO ChatGPT_Pref_num.
VARIABLE LABELS ChatGPT_Pref_num 'ChatGPT Usage Preference (Recoded)'.
VALUE LABELS ChatGPT_Pref_num 1 'Alone' 2 'With group'.

RECODE Perception_Understanding ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Understanding_num.
RECODE Perception_Exam_Prep ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Exam_Prep_num.
RECODE Perception_Accuracy ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Accuracy_num.
RECODE Perception_Verification ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Verification_num.
RECODE Perception_Confidence ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Confidence_num.
RECODE Perception_Time_Saving ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Time_Saving_num.
RECODE Perception_Study_Encouragement ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Study_Encouragement_num.
RECODE Perception_Replacement ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Replacement_num.
RECODE Perception_Enjoyment ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Enjoyment_num.
RECODE Perception_Recommendation ('Strongly Disagree.' = 1) ('Disagree' = 2) ('Neutral' = 3) ('Agree' = 4) ('Strongly Agree' = 5) INTO Perception_Recommendation_num.

COMPUTE Perceptions_Score = MEAN(Perception_Understanding_num, Perception_Exam_Prep_num, Perception_Accuracy_num, Perception_Verification_num, 
Perception_Confidence_num, Perception_Time_Saving_num, Perception_Study_Encouragement_num, Perception_Replacement_num, Perception_Enjoyment_num, 
Perception_Recommendation_num).
VARIABLE LABELS Perceptions_Score 'Overall Perceptions Score'.
EXECUTE.

DO REPEAT a= 'Summarizing lectures' 'Explaining difficult concepts' 'Answering clinical questions' 'Creating revision notes' 'Preparing for OSCE' 
'Research assistance' 'Language support' 'To prepare for exams' / b= ChatGPT_Purpose_1 to ChatGPT_Purpose_8.
RECODE ChatGPT_Main_Purposes (a=1) (ELSE=0) INTO b.
END REPEAT.
EXECUTE.

DO REPEAT a= 'Overreliance' 'Accuracy doubts' 'Plagiarism risk' 'Poor internet' 'None' / b= ChatGPT_Challenge_1 to ChatGPT_Challenge_5.
RECODE Challenges_with_ChatGPT (a=1) (ELSE=0) INTO b.
END REPEAT.
EXECUTE.

RELIABILITY
  /VARIABLES=Perception_Understanding_num Perception_Exam_Prep_num Perception_Accuracy_num Perception_Verification_num Perception_Confidence_num 
  Perception_Time_Saving_num Perception_Study_Encouragement_num Perception_Replacement_num Perception_Enjoyment_num Perception_Recommendation_num
  /SCALE('Perceptions Scale') ALL
  /MODEL=ALPHA
  /STATISTICS=SCALE.

FREQUENCIES VARIABLES=Gender_num Age_num Year_num Residency_num Income_num ChatGPT_Fin_Constraints_num 
  Internet_Fin_Challenges_num Uni_Guidance_num Lecturers_Encouragement_num Institution_Training_num Prior_Knowledge_num Reg_Internet_Use_num 
  ChatGPT_Freq_num ChatGPT_Pref_num ChatGPT_Purpose_1 to ChatGPT_Purpose_8 ChatGPT_Challenge_1 to ChatGPT_Challenge_5
  /STATISTICS=MODE
  /BARCHART.

DESCRIPTIVES VARIABLES=Perception_Understanding_num Perception_Exam_Prep_num Perception_Accuracy_num Perception_Verification_num 
  Perception_Confidence_num Perception_Time_Saving_num Perception_Study_Encouragement_num Perception_Replacement_num Perception_Enjoyment_num 
  Perception_Recommendation_num Perceptions_Score
  /STATISTICS=MEAN STDDEV.

CROSSTABS
  /TABLES=Gender_num BY ChatGPT_Freq_num
  /CELLS=COUNT ROW TOTAL
  /STATISTICS=CHISQ.

CROSSTABS
  /TABLES=Year_num BY Perception_Accuracy_num
  /CELLS=COUNT ROW TOTAL
  /STATISTICS=CHISQ.

CROSSTABS
  /TABLES=Gender_num BY Prior_Knowledge_num
  /CELLS=COUNT ROW TOTAL
  /STATISTICS=CHISQ.

CROSSTABS
  /TABLES=Gender_num BY ChatGPT_Pref_num
  /CELLS=COUNT ROW TOTAL
  /STATISTICS=CHISQ.

CROSSTABS
  /TABLES=Year_num BY ChatGPT_Freq_num
  /CELLS=COUNT ROW TOTAL
  /STATISTICS=CHISQ.

CROSSTABS
  /TABLES=Residency_num BY ChatGPT_Freq_num
  /CELLS=COUNT ROW TOTAL
  /STATISTICS=CHISQ.

CROSSTABS
  /TABLES=Uni_Guidance_num BY ChatGPT_Freq_num
  /CELLS=COUNT ROW TOTAL
  /STATISTICS=CHISQ.

T-TEST GROUPS=Reg_Internet_Use_num(0 1)
  /VARIABLES=Perceptions_Score
  /MISSING=ANALYSIS
  /CRITERIA=CI(.95).

T-TEST GROUPS=Internet_Fin_Challenges_num(0 1)
  /VARIABLES=Perceptions_Score
  /MISSING=ANALYSIS
  /CRITERIA=CI(.95).

T-TEST GROUPS=Institution_Training_num(0 1)
  /VARIABLES=Perceptions_Score
  /MISSING=ANALYSIS
  /CRITERIA=CI(.95).

T-TEST GROUPS=Reg_Internet_Use_num(0 1)
  /VARIABLES=Perceptions_Score
  /MISSING=ANALYSIS
  /CRITERIA=CI(.95).

T-TEST GROUPS=ChatGPT_Pref_num(1 2)
  /VARIABLES=Perceptions_Score
  /MISSING=ANALYSIS
  /CRITERIA=CI(.95).

ONEWAY Perceptions_Score BY Year_num
  /STATISTICS DESCRIPTIVES
  /MISSING ANALYSIS
  /POSTHOC=SCHEFFE ALPHA(0.05).

ONEWAY Perceptions_Score BY Income_num
  /STATISTICS DESCRIPTIVES
  /MISSING ANALYSIS
  /POSTHOC=SCHEFFE ALPHA(0.05).

ONEWAY Perceptions_Score BY Age_num
  /STATISTICS DESCRIPTIVES
  /MISSING ANALYSIS
  /POSTHOC=SCHEFFE ALPHA(0.05).

ONEWAY Perceptions_Score BY Year_num
  /STATISTICS DESCRIPTIVES
  /MISSING ANALYSIS
  /POSTHOC=SCHEFFE ALPHA(0.05).

ONEWAY Perceptions_Score BY Income_num
  /STATISTICS DESCRIPTIVES
  /MISSING ANALYSIS
  /POSTHOC=SCHEFFE ALPHA(0.05).

ONEWAY Perceptions_Score BY Residency_num
  /STATISTICS DESCRIPTIVES
  /MISSING ANALYSIS
  /POSTHOC=SCHEFFE ALPHA(0.05).

ONEWAY Perceptions_Score BY Uni_Guidance_num
  /STATISTICS DESCRIPTIVES
  /MISSING ANALYSIS
  /POSTHOC=SCHEFFE ALPHA(0.05).

ONEWAY Perceptions_Score BY Lecturers_Encouragement_num
  /STATISTICS DESCRIPTIVES
  /MISSING ANALYSIS
  /POSTHOC=SCHEFFE ALPHA(0.05).

ONEWAY Perceptions_Score BY Prior_Knowledge_num
  /STATISTICS DESCRIPTIVES
  /MISSING ANALYSIS
  /POSTHOC=SCHEFFE ALPHA(0.05).

CORRELATIONS
  /VARIABLES=Perceptions_Score ChatGPT_Freq_num
  /PRINT=TWOTAIL NOSIG.

CORRELATIONS
  /VARIABLES=Perception_Understanding_num Perception_Exam_Prep_num Perception_Accuracy_num Perception_Verification_num 
  Perception_Confidence_num Perception_Time_Saving_num Perception_Study_Encouragement_num Perception_Replacement_num Perception_Enjoyment_num 
  Perception_Recommendation_num
  /PRINT=TWOTAIL NOSIG.

REGRESSION
  /DESCRIPTIVES=MEAN STDDEV CORR
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS R ANOVA COLLIN TOL CHANGE
  /CRITERIA=PIN(.05) POUT(.10)
  /DEPENDENT Perceptions_Score
  /METHOD=ENTER ChatGPT_Freq_num Gender_num Year_num Reg_Internet_Use_num.

REGRESSION
  /DEPENDENT Perceptions_Score
  /METHOD=ENTER ChatGPT_Freq_num Gender_num Year_num Reg_Internet_Use_num
  /SAVE RESID(Unstandardized_Residuals) PREDICTED(Predicted_Scores)
  /SCATTERPLOT (*ZRESID, *ZPRED).

RECODE ChatGPT_Freq_num (1 2 = 0) (3 4 = 1) INTO Frequent_User_num.
VARIABLE LABELS Frequent_User_num 'Frequent ChatGPT User (1=Yes, 0=No)'.
VALUE LABELS Frequent_User_num 0 'Infrequent User' 1 'Frequent User'.
EXECUTE.

LOGISTIC REGRESSION VAR=Frequent_User_num
  /METHOD=ENTER Gender_num Age_num Year_num Income_num Internet_Fin_Challenges_num Uni_Guidance_num Institution_Training_num Prior_Knowledge_num Lecturers_Encouragement_num.
EXECUTE.

SAVE OUTFILE='C:\Users\Abdulrhman Alsir\Desktop\portfolio\chatgpt-academic-performance\1_data\cleaned\cleaned_and_coded_data.sav' /COMPRESSED.
EXECUTE.
