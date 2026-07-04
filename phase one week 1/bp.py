def classify_bp(systolic, diastolic):
    if systolic >= 180 or diastolic >= 120:
        return "🚨 Hypertensive Crisis — Seek emergency care immediately!"
    elif systolic >= 140 or diastolic >= 90:
        return "🔴 Stage 2 Hypertension — See a doctor, medication likely needed."
    elif systolic >= 130 or diastolic >= 80:
        return "🟠 Stage 1 Hypertension — Lifestyle changes + consult a physician."
    elif systolic >= 120 and diastolic < 80:
        return "🟡 Elevated — Monitor closely and improve lifestyle habits."
    elif systolic < 120 and diastolic < 80:
        return "🟢 Normal — Keep it up!"
    else:
        return "⚠️ Unable to classify — check your values."

# --- Input ---
try:
    sys_bp = int(input("Enter Systolic BP (mmHg): "))
    dia_bp = int(input("Enter Diastolic BP (mmHg): "))
    print("\nResult:", classify_bp(sys_bp, dia_bp))
except ValueError:
    print("Invalid input. Please enter numbers only.")
