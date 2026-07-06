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

    tech_stack = {
        "Backend": "FastAPI",
        "Frontend": "React",
        "Database": "PostgreSQL",
        "Authentication": "JWT",
        "Deployment": "Docker"
    }

    feature_count = len(detected_features)

    if feature_count <= 2:
        timeline = "1 Week"

    elif feature_count <= 5:
        timeline = "2 Weeks"

    elif feature_count <= 8:
        timeline = "1 Month"

    else:
        timeline = "2 Months"

    return {
        "original_requirement": description,
        "detected_features": detected_features,
        "total_features": feature_count,
        "recommended_tech_stack": tech_stack,
        "estimated_timeline": timeline,
        "status": "Analysis Completed"
    }