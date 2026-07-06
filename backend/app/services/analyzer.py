def analyze_requirement(description: str):
    
    text = description.lower()

    detected_features = []

    if "login" in text:
        detected_features.append("Login")

    if "dashboard" in text:
        detected_features.append("Dashboard")

    if "payment" in text:
        detected_features.append("Payment Gateway")

    if "admin" in text:
        detected_features.append("Admin Panel")

    if "chat" in text:
        detected_features.append("Chat")

    if "attendance" in text:
        detected_features.append("Attendance")

    if "report" in text:
        detected_features.append("Reports")

    return {
        "original_requirement": description,
        "detected_features": detected_features,
        "total_features": len(detected_features),
        "status": "Analysis Completed"
    }