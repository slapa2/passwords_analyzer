# Passwords Analyzer

This program has two password validators
* basic password validation
    * validate if password has mor then 8 characters
    * validate if password has lowercase and uppercase letters
    * validate if password has any special character
* haveibeenpwned.com api based validation
  * validate if password has been pwned

If you want to check your passwords put them to csv file in var/passwords.csv
next run script main.py 

```python3 main.py```

correct password will be written to var/correct_passwords.csv file 