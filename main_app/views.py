from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def welcome_page(request):
    return render(request, 'welcome.html')  # Remove the app-specific folder to test



def login_page(request):
    return render(request, 'login.html')


def role_selection(request):
    return render(request, 'role_selection.html')

def patient_registration(request):
    return render(request, 'patient_registration.html')


def questionnaire(request):
    return render(request, 'questionnaire.html')


from django.shortcuts import render

# Other views you may already have, like welcome_page, login_page, role_selection, etc.

# Function to handle the results page for patient recommendations
def results(request):
    # Retrieve form data from questionnaire (or any other context data)
    # Example: hypothetical data processing to generate recommendations
    recommendations = {
        "food": "Maintain a balanced diet rich in fruits and vegetables.",
        "exercise": "Engage in at least 30 minutes of physical activity daily.",
        "consultation": "Consider consulting a nutritionist if needed."
    }
    return render(request, 'results.html', {"recommendations": recommendations})


# Function to handle the doctor interface page
def doctor_interface(request):
    # Fetch doctor-specific data, such as patient records or appointment schedules
    # For now, return a basic placeholder response
    doctor_data = {
        "patients": [
            {"name": "John Doe", "condition": "Hypertension", "appointment": "2024-11-15"},
            {"name": "Jane Smith", "condition": "Diabetes", "appointment": "2024-11-16"},
        ],
        "working_hours": "9:00 AM - 5:00 PM"
    }
    return render(request, 'doctor_interface.html', {"doctor_data": doctor_data})


# Function to handle the pharmacy interface page
def pharmacy_interface(request):
    # Fetch pharmacy data like available medicines, essentials, cart, etc.
    # Placeholder for pharmacy items and a cart simulation
    pharmacy_data = {
        "medicines": [
            {"name": "Paracetamol", "price": "$5", "quantity": 10},
            {"name": "Ibuprofen", "price": "$8", "quantity": 5},
        ],
        "cart": []
    }
    return render(request, 'pharmacy_interface.html', {"pharmacy_data": pharmacy_data})
