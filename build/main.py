from pathlib import Path
from tkinter import *
import customtkinter,tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
import tkinter as tk
from ctypes import windll
import numpy as np
import pandas as pd
import io
import customtkinter
import gui

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Academics\AIML\Mini-Project\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

windll.shcore.SetProcessDpiAwareness(1)
window = Tk()

customtkinter.set_appearance_mode('light')

window.geometry("700x550")
window.configure(bg = "#FFFFFF")

l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)
# TESTING DATA
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)

# data2 = pd.read_csv('disease_riskFactors.csv')
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Replace 'your_dataset.csv' with the actual path to your dataset CSV file
file_path = 'disease_riskFactors.csv'
df_disease = pd.read_csv('disease_medicine.csv', encoding='iso-8859-1')

# List of possible encodings to try
encodings = ['utf-8', 'iso-8859-1', 'cp1252']

df1 = None

for encoding in encodings:
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            df1 = pd.read_csv(io.StringIO(content.decode(encoding)))
        break
    except UnicodeDecodeError:
        continue


predicted_d = ""
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def message():
    predicted_disease.configure(text="")
    if (symptom_1.get() == "Symptom 1" and  symptom_2.get() == "Symptom 2" and symptom_3.get() == "Symptom 3" and symptom_4.get() == "Symptom 4" and symptom_5.get() == "Symptom 5"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        NaiveBayes()
    symptom_1.set("Symptom 1")
    symptom_2.set("Symptom 2")
    symptom_3.set("Symptom 3")
    symptom_4.set("Symptom 4")
    symptom_5.set("Symptom 5")


def moreDetails():
    window1 = Toplevel()


    window1.geometry("700x550")
    window1.configure(bg = "#FFFFFF")

    canvas = Canvas(
        window1,
        bg = "#FFFFFF",
        height = 550,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        397.0,
        275.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        90.0,
        fill="#000D1E",
        outline="")

    canvas.create_rectangle(
        369.0,
        106.0,
        654.0,
        509.0,
        fill="#000D1E",
        outline="")

    canvas.create_rectangle(
        28.0,
        106.0,
        348.0,
        509.0,
        fill="#000D1E",
        outline="")


    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        60.0,
        45.0,
        image=image_image_2
    )

    canvas.create_text(
        109.0,
        16.0,
        anchor="nw",
        text="Automated Disease \nPrediction",
        fill="#FFFFFF",
        font=("Montserrat Bold", 24 * -1)
    )

    canvas.create_text(
        46.0,
        125.0,
        anchor="nw",
        text="Predicted Disease:",
        fill="#FFFFFF",
        font=("Montserrat Light", 30 * -1)
    )

    canvas.create_text(
        46.0,
        329.0,
        anchor="nw",
        text="Medicines.",
        fill="#FFFFFF",
        font=("Montserrat Light", 24 * -1)
    )

    canvas.create_text(
        405.0,
        125.0,
        anchor="nw",
        text="Precautions.",
        fill="#FFFFFF",
        font=("Montserrat Light", 24 * -1)
    )

    canvas.create_rectangle(
        654.0,
        7.0,
        692.3197937011719,
        45.31980895996094,
        fill="#000D1E",
        outline="")
    
    predicted_disease = customtkinter.CTkLabel(window1,text_color='#FFF', bg_color='#000D1E', text=str(desired_disease),
                                           font=('Montserrat SemiBold', 20), wraplength=200,
                                           anchor="w", justify="left")
    predicted_disease.place(relx =0.065, rely=0.29)
    # print(predicted_d)
    stringMedicine =""
    for i in range (0, len(medicines)):
        stringMedicine+= str(i+1)+".  "+medicines[i].capitalize()+"\n"
        print(medicines[i])

    display_medicine = customtkinter.CTkLabel(window1,text_color='#FFF', bg_color='#000D1E', text=str(stringMedicine),
                                           font=('Montserrat SemiBold', 12), wraplength=200,
                                           anchor="w", justify="left")
    display_medicine.place(relx =0.066, rely=0.65)

    stringPrecaution =""
    for i in range (0, len(precaution)):
        stringPrecaution+= precaution[i]+"\n"

    display_precautions = customtkinter.CTkLabel(window1,text_color='#FFF', bg_color='#000D1E', text=str(stringPrecaution),
                                           font=('Montserrat SemiBold', 12), wraplength=150,
                                           anchor="w", justify="left")
    display_precautions.place(relx =0.58, rely=0.29)


    window1.resizable(False, False)
    window1.mainloop()

def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb=gnb.fit(X,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [symptom_1.get(),symptom_2.get(),symptom_3.get(),symptom_4.get(),symptom_5.get()]

    l2 = [0] * len(l1)

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break

    if (h=='yes'):
        # predicted_disease.delete("1.0", END)
        # predicted_disease.insert(END, disease[a])
        # predicted_disease.clipboard_append(disease[a])
        predicted_disease.configure(text=disease[a])
        print(disease[a])
        global desired_disease
        global medicineList
        desired_disease= disease[a].strip()
        predicted_d = disease[a].strip()
        if df1 is not None:
            filtered_rows = df1[df1['DNAME'] == desired_disease]
            if not filtered_rows.empty:
                ids = filtered_rows['DID'].tolist()
                print(f"IDs for {desired_disease}: {', '.join(map(str, ids))}")
# ------------------------------------------------------------------------------------------------------------------------------
                desired_disease_ids = ids
                for desired_disease_id in desired_disease_ids:
    # Filter the second dataset to match the disease ID
                    filtered_medicines = df_disease[df_disease['Disease_ID'] == desired_disease_id]

                    if not filtered_medicines.empty:
        # Retrieve and display all medicines associated with the disease ID
                        global medicines 
                        medicines = filtered_medicines['Medicine_Name'].tolist()
                        print(f"Medicines for Disease ID {desired_disease_id}:")
                        for medicine in medicines:
                            print(medicine)
                            medicineList = medicine
                    else:
                        print(f"No medicines found for Disease ID {desired_disease_id}")
# ------------------------------------------------------------------------------------------------------------------------------
                if df1 is not None:
                    filtered_rows = df1[df1['DNAME'] == desired_disease]
                    if not filtered_rows.empty:
                        ids = filtered_rows['DID'].tolist()
                        print(type(ids))
                        global precaution
                        precaution = filtered_rows['PRECAU'].tolist()
                        print(f"IDs for {desired_disease}: {', '.join(map(str, ids))}")
                        print(f"IDs for {desired_disease}: {', '.join(map(str, precaution))}")
                    else:
                        print(f"No matching records found for {desired_disease} Please visit Clinic to know about the {desired_disease}")
                else:
                    print("Unable to read the CSV file with any of the specified encodings.")
# ------------------------------------------------------------------------------------------------------------------------------
            else:
                print(f"No matching records found for {desired_disease}")
        else:
            print("Unable to read the CSV file with any of the specified encodings.")


    else:
        # predicted_disease.delete("1.0", END)
        # predicted_disease.insert(END, "No Disease")
        predicted_disease.configure(text="No Disease")
        

# ------------------------------------------------------------




# Replace 'your_disease_name' with the disease name you want to search for

# desired_disease = 'AIDS'

# if df1 is not None:
#     filtered_rows = df1[df1['DNAME'] == desired_disease]
#     if not filtered_rows.empty:
#         ids = filtered_rows['DID'].tolist()
#         print(f"IDs for {desired_disease}: {', '.join(map(str, ids))}")
#     else:
#         print(f"No matching records found for {desired_disease}")
# else:
#     print("Unable to read the CSV file with any of the specified encodings.")
# ------------------------------------------------------------
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    397.0,
    275.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    90.0,
    fill="#000D1E",
    outline="")

canvas.create_text(
    109.0,
    16.0,
    anchor="nw",
    text="Automated Disease \nPrediction",
    fill="#FFFFFF",
    font=("Montserrat Bold", 24 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    60.0,
    45.0,
    image=image_image_2
)

canvas.create_rectangle(
    369.0,
    106.0,
    654.0,
    509.0,
    fill="#000D1E",
    outline="")

canvas.create_rectangle(
    28.0,
    106.0,
    348.0,
    509.0,
    fill="#000D1E",
    outline="")

canvas.create_text(
    47.0,
    122.0,
    anchor="nw",
    text="Predict any",
    fill="#FFFFFF",
    font=("Montserrat Light", 32 * -1)
)

canvas.create_text(
    46.0,
    318.0,
    anchor="nw",
    text="Steps:\n1. Select the symptoms.\n2. Click 'Predict'.",
    fill="#FFFFFF",
    font=("Montserrat Regular", 16 * -1)
)

canvas.create_text(
    46.0,
    244.0,
    anchor="nw",
    text="seconds.",
    fill="#FFFFFF",
    font=("Montserrat Light", 32 * -1)
)

canvas.create_text(
    47.0,
    162.0,
    anchor="nw",
    text="Disease",
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 36 * -1)
)

canvas.create_text(
    46.0,
    205.0,
    anchor="nw",
    text="in just few",
    fill="#FFFFFF",
    font=("Montserrat Light", 32 * -1)
)
OPTIONS = sorted(l1)
symptom_1= customtkinter.CTkComboBox(master=window, 
                                     values=[*OPTIONS],
                                     height=8, border_width=2,bg_color='#000D1E',
                                     font=('Montserrat Light', 12),
                                     dropdown_font=('Montserrat Light', 12),
                                     corner_radius=5)
symptom_1.set("Symptom 1")
symptom_1.place(relx =0.58, rely=0.25)

symptom_2= customtkinter.CTkComboBox(master=window, 
                                     values=[*OPTIONS],
                                     height=8, border_width=2, bg_color='#000D1E',
                                     font=('Montserrat Light', 12),
                                     dropdown_font=('Montserrat Light', 12),
                                     corner_radius=5)
symptom_2.set("Symptom 2")
symptom_2.place(relx =0.58, rely=0.35)

symptom_3= customtkinter.CTkComboBox(master=window, 
                                     values=[*OPTIONS],
                                     height=8, border_width=2, bg_color='#000D1E',
                                     font=('Montserrat Light', 12),
                                     dropdown_font=('Montserrat Light', 12),
                                     corner_radius=5)
symptom_3.set("Symptom 3")
symptom_3.place(relx =0.58, rely=0.45)

symptom_4= customtkinter.CTkComboBox(master=window, 
                                     values=[*OPTIONS],
                                     height=8, border_width=2, bg_color='#000D1E',
                                     font=('Montserrat Light', 12),
                                     dropdown_font=('Montserrat Light', 12),
                                     corner_radius=5)
symptom_4.set("Symptom 4")
symptom_4.place(relx =0.58, rely=0.55)

symptom_5= customtkinter.CTkComboBox(master=window, 
                                     values=[*OPTIONS],
                                     height=8, border_width=2, bg_color='#000D1E',
                                     font=('Montserrat Light', 12),
                                     dropdown_font=('Montserrat Light', 12),
                                     corner_radius=5)
symptom_5.set("Symptom 5")
symptom_5.place(relx =0.58, rely=0.65)

predict_button= customtkinter.CTkButton(window, text='PREDICT', text_color='#FFF',
                                        font=('Montserrat SemiBold',16),
                                        bg_color="#000D1E",command=message)
predict_button.place(relx =0.58, rely=0.75)

details_button= customtkinter.CTkButton(window, text='More Details', text_color='#FFF',
                                        font=('Montserrat SemiBold',16),
                                        bg_color="#000D1E",command=moreDetails)
details_button.place(relx =0.58, rely=0.85)

text_pred_disease = customtkinter.CTkLabel(window,text_color='#FFF', bg_color='#000D1E', text="Disease predicted :")
text_pred_disease.place(relx =0.065, rely=0.75)

predicted_disease = customtkinter.CTkLabel(window,text_color='#FFF', bg_color='#000D1E', text="",
                                           font=('Montserrat SemiBold', 18), wraplength=200,
                                           anchor="w", justify="left")
predicted_disease.place(relx =0.0658, rely=0.81)

window.resizable(False, False)
window.mainloop()