import os
import google.generativeai as genai
import logging
import json
from flask import current_app

logger = logging.getLogger(__name__)

def configure_gemini():
    """Configures the Gemini API with the key from the app config."""
    api_key = current_app.config.get('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("Gemini API key is missing.")
    genai.configure(api_key=api_key)
    logger.info("Gemini AI SDK configured successfully.")

def get_master_analysis(report_text: str) -> dict:
    """
    Analyzes medical report text and generates a single, comprehensive JSON object
    containing all data needed for every feature page.
    """
    if not report_text or not report_text.strip():
        return {"error": "Input text for AI analysis is empty or invalid."}

    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
    except Exception as e:
        logger.error(f"Could not initialize Gemini model: {e}")
        return {"error": "Gemini AI model is not available or configured."}

    # ------------------------
    # Strong Prompt Enforcement
    # ------------------------
    prompt = f"""
    You are a master medical analysis AI for the "MediGuide AI" project.

    Analyze the medical report text below and generate a JSON object 
    with **exactly 3 top-level keys**:
    - "dashboardData"
    - "insightsData"
    - "dietData"

    ⚠️ Rules (must follow):
    - Do NOT leave any array empty.
    - If the report lacks data, create **realistic placeholder data**.
    - Always include **all required fields** as described in the schema.
    - Return only valid JSON, without extra commentary or markdown.

    ------------------------
    JSON Schema (must follow)
    ------------------------

    {{
      "dashboardData": {{
        "patientInformation": {{
          "name": "string",
          "age": "string",
          "gender": "string",
          "advisedDate": "string"
        }},
        "keyMetrics": [ {{ "title": "string", "value": "string", "change": "string", "description": "string", "target": "string" }} ],
        "recentReports": [ {{ "name": "string", "date": "string", "doctor": "string", "status": "string", "score": "string" }} ],
        "alerts": [ {{ "message": "string", "time": "string", "level": "high|medium|low" }} ],
        "healthTrends": [ {{ "period": "string", "metric": "string", "value": "string", "change": "string" }} ],
        "upcomingAppointments": [ {{ "type": "string", "doctor": "string", "dateTime": "string", "location": "string" }} ],
        "testResults": [ {{ "testName": "string", "result": "string", "unit": "string", "range": "string" }} ]
      }},
      "insightsData": {{
        "healthMetrics": [ {{ "name": "string", "value": "string", "trend": "string", "color": "string" }} ],
        "insightsDashboard": [ {{ "id": "string", "title": "string", "count": "number", "items": ["string"] }} ],
        "riskAssessment": [ {{ "factor": "string", "risk": "string", "description": "string" }} ],
        "personalizedActionPlan": {{
          "shortTerm": ["string"],
          "longTerm": ["string"]
        }}
      }},
      "dietData": {{
        "healthConditions": [ {{ "name": "string", "level": "string", "color": "string", "recommendations": ["string"] }} ],
        "foodRecommendations": {{
          "recommended": [{{ "food": "string" }}],
          "limit": [{{ "food": "string" }}],
          "caution": [{{ "food": "string" }}]
        }},
        "mealPlans": {{
          "balanced": {{
            "title": "string",
            "description": "string",
            "summary": {{
              "dailyCalories": "string",
              "macronutrients": {{ "carbs": "string", "protein": "string", "fat": "string" }},
              "mealCount": "string"
            }},
            "meals": [ {{ "mealType": "string", "time": "string", "calories": "string", "items": ["string"], "highlight": "string" }} ]
          }},
          "diabeticFriendly": {{
            "title": "string",
            "description": "string",
            "summary": {{
              "dailyCalories": "string",
              "macronutrients": {{ "carbs": "string", "protein": "string", "fat": "string" }},
              "mealCount": "string"
            }},
            "meals": [ {{ "mealType": "string", "time": "string", "calories": "string", "items": ["string"], "highlight": "string" }} ]
          }}
        }},
        "nutritionalGoals": [ {{ "goal": "string" }} ],
        "weeklyMenu": [ {{ "day": "string", "theme": "string", "mealSuggestion": "string" }} ],
        "mealPrepTips": {{
          "sundayPrep": ["string"],
          "storageTips": ["string"]
        }},
        "progressSummary": {{
          "goalsImproving": "string",
          "averageProgress": "string",
          "areasNeedAttention": "string"
        }}
      }}
    }}

    ------------------------
    Medical Report to Analyze:
    ------------------------
    {report_text}
    """

    try:
        logger.info("Sending request to Gemini API for MASTER analysis...")
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}  # ✅ force JSON
        )

        raw_text = response.text.strip()
        logger.debug(f"Raw Gemini response: {raw_text[:200]}...")  # only log first 200 chars

        analysis_data = json.loads(raw_text)
        logger.info("Successfully received and parsed MASTER analysis from Gemini API.")
        return analysis_data

    except json.JSONDecodeError:
        logger.error(f"Failed to decode JSON from Gemini response. Raw text: {response.text}")
        return {"error": "Failed to parse AI analysis. The response was not valid JSON."}
    except Exception as e:
        logger.error(f"An error occurred while communicating with the Gemini API: {e}")
        return {"error": f"An unexpected error occurred with the AI service: {str(e)}"}
