print("Login Page")
username = 'Rohan912'
password = '@rohann89895'
usrnm = input("Enter username: ")
ps = input("Enter password: ")

if usrnm == username and ps == password:
    print("Login successful")
    
    options = {
        "1": "Contact a Doctor",
        "2": "Improve your Health ",
        "3": "Get Medications",
    }

    # Display options to the user
    print("Select an option:")
    for key, option in options.items():
        print(f"{key}. {option}")

    # Get user input
    choice = input("Enter the key of your choice: ")

    # Validate user input
    selected_option = options.get(choice)
    if selected_option == "Contact a Doctor":
        print(f"You selected: {selected_option}")
        print('''Here are contact details of India's best 
        Doctors
        with their speciality
        1. Allergy and immunology = 9873448987
        2. Anesthesiology = 287498924
        3. Dermatology = 279847988
        4. Diagnostic radiology = 87987897799
        5. Emergency medicine = 9887789799
        6. Family medicine = 9889897897
        7. Internal medicine = 80980800988
        8. Medical genetics = 98797979798
        9. Neurology = 098988809809
        10. Nuclear medicine = 0899809808
        11. Obstetrics and gynecology = 98908809809
        12. Ophthalmology = 7655654679
        13. Pathology = 9880980980   
        ''')
    if selected_option == "Improve your Health ":
        print(f"You selected: {selected_option}")
        print('''Improving the health of elderly individuals requires a comprehensive approach that encompasses physical, mental, and social well-being. Here are some tips and a sample schedule to help elderly people maintain and improve their health:

**Physical Health:**

1. **Regular Exercise:**
   - Schedule at least 150 minutes of moderate-intensity aerobic activity per week, or consult a healthcare provider for a personalized exercise plan.
   - Include strength training exercises at least twice a week to maintain muscle mass and strength.

2. **Balanced Diet:**
   - Eat a variety of fruits, vegetables, whole grains, lean proteins, and dairy products.
   - Limit processed foods, added sugars, and sodium intake.

3. **Stay Hydrated:**
   - Drink plenty of water throughout the day to prevent dehydration.

4. **Adequate Sleep:**
   - Aim for 7-9 hours of quality sleep each night to support overall health.

5. **Regular Check-ups:**
   - Visit healthcare professionals regularly for check-ups, vaccinations, and screenings.

6. **Medication Management:**
   - Take prescribed medications as directed and inform healthcare providers about any side effects or concerns.

7. **Fall Prevention:**
   - Modify the home environment to reduce fall risks, such as installing handrails and removing tripping hazards.

8. **Vision and Hearing Care:**
   - Get regular eye and hearing exams and use corrective devices as needed.

**Mental Health:**

1. **Social Engagement:**
   - Stay socially active by participating in community events, clubs, or volunteering.
   - Maintain contact with friends and family members.

2. **Mind Exercises:**
   - Engage in mentally stimulating activities like puzzles, crosswords, or learning new skills.

3. **Manage Stress:**
   - Practice relaxation techniques like deep breathing, meditation, or yoga.
   - Seek professional help if experiencing persistent anxiety or depression.

4. **Maintain a Positive Outlook:**
   - Cultivate a positive attitude and focus on gratitude and mindfulness.

**Social Health:**

1. **Stay Connected:**
   - Schedule regular visits or calls with loved ones.
   - Join social clubs or organizations of interest.

2. **Community Engagement:**
   - Participate in community events, local senior centers, or volunteer opportunities.

**Sample Weekly Schedule:**

- **Monday:**
  - Morning: 30 minutes of light stretching or yoga.
  - Afternoon: Attend a local seniors' club meeting or engage in a hobby.
  - Evening: Relaxation exercises or meditation.

- **Tuesday:**
  - Morning: Walk for 20 minutes.
  - Afternoon: Prepare a healthy meal or attend a cooking class.
  - Evening: Visit or call a friend or family member.

- **Wednesday:**
  - Morning: Strength training exercises for 20 minutes.
  - Afternoon: Visit a healthcare provider or attend a health education class.
  - Evening: Engage in a mentally stimulating activity.

- **Thursday:**
  - Morning: 30 minutes of chair yoga or tai chi.
  - Afternoon: Volunteer at a local organization or charity.
  - Evening: Enjoy a leisurely walk.

- **Friday:**
  - Morning: Complete balance exercises for 15 minutes.
  - Afternoon: Join a book club or engage in reading.
  - Evening: Watch a movie or attend a cultural event.

- **Saturday:**
  - Morning: Explore a new hobby or interest.
  - Afternoon: Cook and share a healthy meal with a friend or family member.
  - Evening: Socialize with neighbors or attend a local event.

- **Sunday:**
  - Morning: Rest and relaxation.
  - Afternoon: Attend a religious or spiritual gathering if desired.
  - Evening: Plan for the upcoming week and set goals.

Remember that this schedule is just a template and should be adjusted to individual preferences, capabilities, and medical needs. Consult with a healthcare provider before starting any new exercise or dietary regimen, and seek professional help for specific health concerns or conditions.''')
    if selected_option == "Get Medications":
        print(f"You selected: {selected_option}")  
        print(''''''Here is the contact number of Medical 
        store,you can order your medicines from here=> 898769786''')
    else:
        print("Invalid choice.")
else:
    print("Username or password is wrong. Please try again.")
