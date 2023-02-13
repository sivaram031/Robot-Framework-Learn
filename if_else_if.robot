*** Settings ***
Documentation  if / else if / else conditions

*** Test Cases ***
if condition true
    IF  1 == 1
        log to console  it's a valid condition
    END
if and else if condition "if" it will fail here
    IF  1 == 3
        log to console  1 is  not equal to 3
    ELSE IF     3 == 3
        log to console  3 is equal to 3
    END

if and else if / else conditions
    IF  1 == 3
        log to console  1 is eqal to 3
    ELSE IF     1 > 3
        log to console  1 is grether then 3
    ELSE
        log to console  1 is lessthen 3
    END