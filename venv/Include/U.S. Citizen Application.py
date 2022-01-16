# Kaden Franklin
# Project #1

Question0 = str (input('How old are you?'))
x = int(Question0)
while x != 18 :
    if x >= 18 :
        print(Question1)
    elif x < 18 :
        print("You need to be atleast 18 years old to apply for citizenship.")
        quit()
    else:
        Question1 = str(input('How old are you?'))

Question1 = str (input('Are you already a United States Citizen? '\
                       '(Please respond with "Yes" or "No")'))

while Question1 != 'No' :
    if Question1 == 'No' :
        print(Question2)
    elif Question1 == 'Yes' :
        print("Congratulations! You do not need to apply for the'\
        ' naturalization process if yo are already a Citizen.")
        quit()
    else:
        Question1 = str(input('Are you already a United States Citizen?'\
                              ' (Please respond with "Yes" or "No")'))

Question2 = str (input('Have you reviewed the Naturalization'\
                       ' Eligibility Worksheet, and made sure'\
                       ' you are eligible to apply for citizenship'\
                       '? (Please respond with "Yes" or "No")'))

while Question2 != 'Yes' :
    if Question2 == 'Yes' :
        print(Question3)
    elif Question2 == 'No' :
        print('Please review the Naturalization and Eligibility Worksheet'\
              ' here : https://www.uscis.gov/sites/default/files'\
              '/USCIS/Resources/Citizenship%20&%20'\
              'Naturalization%20Based%20Resour'\
              'ces/A%20Guide%20to%20Naturalization/PDFs/M-480.pdf')
        quit()
    else:
        Question2 = str (input('Have you reviewed the Naturalization'\
                               ' Eligibility Worksheet, and made sure you'\
                               ' are eligible to apply for citizenship? '\
                               '(Please respond with "Yes" or "No")'))

Question3 = str (input('Have you completed your N-400 Application '\
                       'for naturalization? '\
                       '(Please respond with "Yes" or "No")'))

while Question3 != 'Yes' :
    if Question3 == 'Yes' :
        print(Question4)
    elif Question3 == 'No' :
        print('Please complete your N-400, Application'\
              ' for naturalization here: https://www.uscis.gov/n-400')
        quit()
    else:
        Question3 = str(input('Have you completed your'\
                              ' N-400 Application for '\
                              'naturalization? '\
                              '(Please respond with "Yes" or "No")'))

Question4 = str (input('Have you completed your USCIS'\
                       ' scheduled interview? (Please '\
                       'respond with "Yes" or "No")'))

while Question4 != 'Yes' :
    if Question4 == 'Yes' :
        print(Question5)
    elif Question4 == 'No' :
        print('Please wait for your scheduled time and '\
              'complete your USCIS interview.')
        quit()
    else:
        Question4 = str(input('Have you completed your USCIS scheduled'\
                              ' interview? '\
                              '(Please respond with "Yes" or "No")'))

Question5 = str (input('What decision have you recieved from USCIS on your'\
                       ' application for naturalization? (Please'\
                       'respond with "Denied", "Continued" or "Granted")'))

while Question5 != 'Granted' :
    if Question5 == 'Denied' :
        print('We apologize, but you are not eligible for U.S. citizenship.')
        quit()
    elif Question5 == 'Continued' :
        print('USCIS may continue your application if you need to provide'\
              ' additional evidence/documentation, fail to provide USCIS'\
              ' the correct documents, or fail'\
              ' the English and/or civics test'\
              ' the first time.')
        quit()
    elif Question5 == 'Granted' :
        print(Question6)
    else:
        Question5 = str(input('What decision have you recieved'\
                              ' from USCIS on your application '\
                              'for naturalization? '\
                              '(Please respond with "Denied", "Continued"'\
                              ' or "Granted")'))

Question6 = str (input('Have you taken your Oath of '\
                       'Allegiance to the United States?'\
                       ' (Please respond with "Yes" or "No")'))

while Question6 != 'Yes' :
    if Question6 == 'Yes' :
        print('Congratulations on completing the '\
              'Naturalization process! You are now a U.S. citizen!')
    elif Question6 == 'No' :
        print('Please sow up at your scheduled time'\
              ' for your naturalization ceremony.')
        quit()
    else:
        Question6 = str(input('Have you taken your Oath of '\
                              'Allegiance to the United States? '\
                              '(Please respond with "Yes" or "No")'))
