# Irina, Your Personal Life Insurance Assistant
# Developed By Pavon Dunbar

# Gathering Information On The User
def gather_user_data():
    user_data = {}

    # Basic Demographics
    user_data['age'] = int(input("What is your age? "))
    user_data['gender'] = input("What is your gender (Male/Female/Other)? ").lower()
    user_data['marital_status'] = input("What is your marital status (Single/Married/Divorced/Widowed)? ").lower()
    user_data['num_of_dependents'] = int(input("How many dependents do you have (children, elderly parents, etc)? If none, enter 0: "))

    # Financial Information
    user_data['annual_income'] = float(input("What is your annual income? "))
    user_data['total_debt'] = float(input("Do you have any outstanding debts? If yes, enter the amount. If no, enter 0: "))
    user_data['monthly_expenses'] = float(input("What are your average monthly expenses? If none, enter 0: "))
    user_data['savings_and_investments'] = float(input("How much do you have in savings and investments? If none, enter 0: "))

    # Health Information
    user_data['smoker'] = input("Do you smoke or consume tobacco in any form (Yes/No)? ").lower()
    user_data['major_illnesses'] = input("Have you had any major illnesses in the past (Yes/No)? ").lower()
    user_data['hereditary_diseases'] = input("Is there a history of hereditary diseases in your family (Yes/No)? ").lower()

    # Life Goals and Future Plans
    user_data['insurance_purpose'] = input("What is the primary purpose of getting life insurance (income replacement, pay off debts, leave inheritance, etc.)? ").lower()
    user_data['coverage_duration'] = int(input("How many years would you want your family's financial needs covered if something were to happen to you? "))
    user_data['more_children'] = input("Are you planning to have more children in the future (Yes/No)? ").lower()
    user_data['future_expenses'] = input("Are there any future major expenses you're foreseeing (Yes/No)? ").lower()

    # Current Insurance and Retirement Plans
    user_data['existing_life_insurance'] = input("Do you currently have any life insurance policies (Yes/No)? ").lower()
    user_data['retirement_plan_type'] = input("Do you have a retirement plan? If so, what type (None/401k/IRA/etc.)? ").lower()
    user_data['investment_policy'] = input("Are you looking for a policy that also serves as an investment or savings vehicle (Yes/No)? ").lower()

    # New Questions
    user_data['specific_company'] = input("Do you have a specific life insurance company in mind (Yes/No)? ").lower()
    user_data['lapsed_policy'] = input("Have you previously held a life insurance policy that has lapsed (Yes/No)? ").lower()
    user_data['high_risk_hobbies'] = input("Do you have any hobbies or activities that could be considered high-risk (e.g., skydiving) (Yes/No)? ").lower()
    user_data['high_risk_profession'] = input("Are you employed in a profession that is considered high-risk (Yes/No)? ").lower()
    user_data['high_risk_travel'] = input("Do you travel frequently to high-risk regions (Yes/No)? ").lower()

    # Risk Tolerance and Investment Perspective
    user_data['risk_tolerance'] = input("Are you comfortable with policies that have variable rates or would you prefer a fixed premium (Variable/Fixed)? ").lower()

    # Duration of Coverage
    user_data['coverage_years'] = int(input("For how many years are you looking to be covered by life insurance? "))

    # Budget
    user_data['budget'] = float(input("How much can you afford to pay for life insurance premiums monthly or annually? "))
    
    return user_data    

# Predicting What Type Of Life Insurance The User Needs
def predict_insurance(user_data):
    # Rule-based decision for insurance type
    if user_data['age'] > 55 or user_data['investment_policy'] == 'yes':
        insurance_type = 'WHOLE'
    else:
        insurance_type = 'TERM'
    
    # Rule-based decision for coverage amount
    coverage_amount = (user_data['annual_income'] - user_data['monthly_expenses'] * 12) + (user_data['coverage_duration'] * user_data['annual_income']) - user_data['total_debt']
    
    # Generate reasoning - This is a rule-based system
    reasons = []
    
    # Reasoning for choosing 'WHOLE' or 'TERM'
    if insurance_type == 'WHOLE':
        reasons.append("Whole life insurance provides lifetime coverage.")
        if user_data['investment_policy'] == 'yes':
            reasons.append("You're looking for an investment component, and whole life insurance builds cash value over time.")
        if user_data['age'] > 55:
            reasons.append("Given your age, whole life insurance might offer more long-term benefits.")
    else:
        reasons.append("Term life insurance provides coverage for a specified term.")
        if user_data['coverage_years'] <= 30:
            reasons.append("You're looking for coverage for a defined period, and term insurance can be a cost-effective choice for that.")
    
    # Reasoning based on health
    if user_data['smoker'] == 'yes':
        reasons.append("As a smoker, your premium might be higher.")
    if user_data['major_illnesses'] == 'yes':
        reasons.append("Having had major illnesses in the past could influence your premium and policy options.")
    if user_data['hereditary_diseases'] == 'yes':
        reasons.append("A family history of hereditary diseases may affect the policy's terms and conditions.")
    
    # Reasoning based on finances
    if user_data['total_debt'] > 0:
        reasons.append("The outstanding debts have been considered to ensure they're covered.")
    if user_data['savings_and_investments'] < user_data['annual_income']:
        reasons.append("Your savings and investments are less than your annual income, influencing the coverage recommendation.")
    
    # Reasoning based on life goals and future plans
    if user_data['more_children'] == 'yes':
        reasons.append("Since you're planning for more children, this can influence the duration and amount of coverage you might need.")
    if user_data['future_expenses'] == 'yes':
        reasons.append("Future major expenses have been factored into the recommendation.")
    
    # Reasoning based on risk factors
    if user_data['high_risk_hobbies'] == 'yes':
        reasons.append("Engaging in high-risk hobbies can impact premium rates and policy terms.")
    if user_data['high_risk_profession'] == 'yes':
        reasons.append("Being in a high-risk profession may lead to higher premium rates.")
    if user_data['high_risk_travel'] == 'yes':
        reasons.append("Frequent travels to high-risk regions may affect your insurance policy options and rates.")
    
    # Reasoning based on other considerations
    if user_data['lapsed_policy'] == 'yes':
        reasons.append("Having a lapsed policy in the past might influence available policy options and terms.")
    if user_data['risk_tolerance'] == 'variable':
        reasons.append("You're comfortable with variable rates, allowing for potential growth in policy value.")
    else:
        reasons.append("You prefer fixed premiums, which offers predictability in costs.")

    return insurance_type, coverage_amount, reasons

# Putting It All Together
if __name__ == "__main__":
    print("Hello there. I'm Irina, your personal insurance agent.")
    print("Before I can give you a customized insurance type, estimated amount, and reason, please answer a few questions")
    print("Enter all numbers as WHOLE numbers with no decimal places (ex: $100,000.00 would be 100000).\n")
    
    user_data = gather_user_data()
    insurance_type, coverage_amount, reasons = predict_insurance(user_data)

    print("\nIrina's Recommended Insurance Type:", insurance_type)
    print("Irina's Estimated Coverage Amount: ${:,.2f}".format(coverage_amount))  # This line formats the amount
    print("Irina's Reasons For The Above:")
    for reason in reasons:
        print("-", reason)
    
    print("\nDisclaimer: The above recommendations are based on the information provided and are for informational purposes only. "
          "Please consult with a licensed insurance agent before making any decisions regarding your insurance coverage.")
