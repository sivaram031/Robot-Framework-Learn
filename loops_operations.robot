*** Settings ***
Documentation  loop operation


*** Test Cases ***
loop operations create list
    ${list}=     Create List     one    two     three
    FOR     ${item}     IN  ${list}
        log to console  ${item}
    END

create list under loop
    FOR     ${item}     IN  one two three four
        log to console  ${item}
    END

print numbers 1 to 10
    FOR     ${range}    IN RANGE    10
        log to console  ${range}
    END

Nested loop
    ${alpha}=   create list  a b c
    ${num}=     create list  ${1} ${2} ${3}
    FOR     ${aplhabets}    IN  ${alpha}
        FOR     ${numbers}  IN  ${num}
            log to console  ${aplhabets}${numbers}
        END
    END
