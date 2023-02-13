*** Settings ***
Documentation  doing list operation here
Library  Collections
Library  C:\\Users\\Sivaram\\PycharmProjects\\Robot-Framework-Learn\\list_operand.py


*** Test Cases ***
list operand
    @{data}=  create list  ram  sam  tom  jhon
    ${val}=  create list

    FOR  ${f}    IN  ${data}
       run keyword if      '${f}' == 'sam'
        Append To List  ${val}   ${f}
        log to console  ${val}
        END
    END




