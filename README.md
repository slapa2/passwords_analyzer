# Passwords Analyzer

This script has two password validators
* basic password validation
    * validate if password has mor then 8 characters
    * validate if password has lowercase and uppercase letters
    * validate if password has any special character
* haveibeenpwned.com api based validation
  * validate if password has been pwned

You can check single password or batch passwords form csv file

If you want to validate batch passwords write them to csv file in var/passwords.csv
correct password will be written to var/correct_passwords.csv file
 
To run script main.py 

```python3 main.py```


---
project inspired by [pycamp.pl](https://www.pycamp.pl/)
