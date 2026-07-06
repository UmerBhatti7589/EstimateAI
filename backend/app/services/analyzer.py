def analyze_requirement(description: str):
    
    # Convert text to lowercase
    text = description.lower()

    # Store detected features
    detected_features = []

    # Feature Detection
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

    if "notification" in text:
        detected_features.append("Notification")

    if "email" in text:
        detected_features.append("Email")

    # AI Tech Stack Recommendation
    tech_stack = {
        "Backend": "FastAPI",
        "Frontend": "React",
        "Database": "PostgreSQL",
        "Authentication": "JWT",
        "Deployment": "Docker"
    }

    # Total Features
    feature_count = len(detected_features)

    # Timeline Estimation
    if feature_count <= 2:
        timeline = "1 Week"
    elif feature_count <= 5:
        timeline = "2 Weeks"
    elif feature_count <= 8:
        timeline = "1 Month"
    else:
        timeline = "2 Months"

    # Cost Estimation
    if feature_count <= 2:
        estimated_cost = "$2,000"
    elif feature_count <= 5:
        estimated_cost = "$5,000"
    elif feature_count <= 8:
        estimated_cost = "$8,000"
    else:
        estimated_cost = "$12,000"

    # Project Complexity
    if feature_count <= 2:
        project_complexity = "Simple"
    elif feature_count <= 5:
        project_complexity = "Medium"
    else:
        project_complexity = "Complex"

    # Recommended Team Size
    if feature_count <= 2:
        team_size = 2
    elif feature_count <= 5:
        team_size = 4
    else:
        team_size = 6

    # Final Response
    return {
        "original_requirement": description,
        "detected_features": detected_features,
        "total_features": feature_count,
        "recommended_tech_stack": tech_stack,
        "estimated_timeline": timeline,
        "estimated_cost": estimated_cost,
        "project_complexity": project_complexity,
        "recommended_team_size": team_size,
        "status": "Analysis Completed Successfully"
    }