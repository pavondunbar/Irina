# Irina

Irina is a Python script that uses a rule-based system to generate life insurance recommendations based on user inputs. Irena leverages conditional statements to determine the appropriate recommendation and to generate reasons based on the inputs.

# Synopsis 

Irina begins by asking the user several questions regarding the user's personal, financial, and health details.

Irina's code consists of the following:

**Data Gathering (function gather_user_data):** This function prompts the user to input various details, including demographics, financial information, health status, life goals, existing insurance policies, risk factors, and budget. The inputs are stored in a dictionary.

**Insurance Prediction (function predict_insurance):** This function takes the dictionary generated from gather_user_data and uses a set of rule-based conditions to recommend an insurance type (whole or term) and estimate a coverage amount. It also generates a list of reasons behind the recommendations, based on the user's responses.

**Main Section (under if __name__ == "__main__":):** When Irina is initialized, it welcomes the user and asks them to input their details through the gather_user_data function. It then passes the gathered data to predict_insurance to get the recommendations and reasons, which are printed out for the user along with a disclaimer.

Irina offers these benefits to users:

**Personalized Recommendations:** Users receive insurance recommendations tailored to their individual circumstances and preferences, taking into account a wide range of factors including their financial situation, health status, and future plans.

**Explanation for Recommendations:** Users are provided with clear reasoning behind each recommendation, which can help them understand the factors influencing their insurance policy recommendations.

**Guided Process:** Irina's questions guide users step-by-step through the information needed, which can be particularly beneficial for individuals who are unfamiliar with the factors that can influence insurance policy recommendations.

**Quick and Easy:** Irina quickly generates recommendations without requiring users to conduct research or consult with an agent thereby saving time and effort.

# Requirements

A terminal window (for now until I get a frontend developed).

Python3.  You can check to see if Python3 is on your system by running the command below:

```
python3 --version
```

If a version number prints out, you are good to go.

# Clone This Repository

Run this command below to clone this repo and begin using it.

```
git clone https://github.com/pavondunbar/Irina && cd Irina
```


# Create a Python Virtual Environment

It is recommended to create a Python virtual environment to run Irina.  Running a virtual environment will prevent library conflicts with other Python projects or applications you may have on your system.

Create a virtual environment named IrinaEnv (or whatever you want to call it) by running the following command:

```
python3 -m venv IrinaEnv
```

If your virtual environment isn't created, you can use this command to create it:

```
virtualenv IrinaEnv
```

Next, type this into the terminal

```
ls
```

You should see IrinaEnv (or whatever name you gave your virtual environment) and Irina.py

If you see both of those items, your virtual environment has been set up.

# Activate the Virtual Environment

After you've created your Python virtual environment, activate it by running the command below:

```
source IrinaEnv/bin/activate
```

**NOTE:** You can turn off your virtual environment by typing this in the terminal

```
deactivate
```

# Initialize Irina

Now the fun begins!  Run the following command to Initialize Irina:

```
python3 Irina.py
```

Irina will initialize and ask you a series of insurance-based questions dealing with your demographics, financial information, health status, life goals, existing insurance policies, risk factors, and budget.

After you submit this information to Irina, Irina will make a determination on what type of life insurance policy you should pursue (Whole or Term), the estimated coverage amount, and the reasons for the determination. Irina will also print out a disclaimer. It is imperative that user heed and take into the account the disclaimer printed out by Irina after its determination.

# Closing Notes

1. Irina uses no libraries which makes the model lightweight since no libraries or modules need to be imported.
2. Irina, at this time, is **not an AI model** due to the lack of sufficient data to make predictions based on patterns and anomalies based on the dataset.

# Disclaimer

If you enjoy using Irina to give you a snapshot of your life insurance coverage options, that is awesome and I appreciate it.  But please...**do not use Irina as a "final decision maker".** 

As a human, you should still do your research and due diligence before you make any decisions regarding life insurance.  It is best to consult with your local life insurance agent after recieving a determination from Irina.

By using Irina, you agree to hold Irina, its creator Pavon Dunbar, or any affiliates or representatives of Baron harmless from any financial damages, errors, etc that may result from its use or misuse.

Irina is a **work in progress** and will be consistently updated.

# Let's Get Social!

Feel free to connect with me.  My Linktree is https://linktr.ee/pavondunbar
