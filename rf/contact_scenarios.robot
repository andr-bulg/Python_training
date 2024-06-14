*** Settings ***
Library    rf.AddressBook
Library    Collections
Suite Setup    Init Fixtures
Suite Teardown    Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list} =    Get Contact List
    ${contact} =    New Contact  Ivan  Ivanov  Moscow
    Create Contact  ${contact}
    ${new_list} =    Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}


Delete contact
    ${old_list} =    Get Contact List
    ${len} =    Get Length  ${old_list}
    ${index} =    Evaluate    random.randrange(${len})    random
    ${contact}    Get From List    ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list} =    Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}


Modify contact
    ${old_list} =    Get Contact List
    ${len} =    Get Length  ${old_list}
    ${index} =    Evaluate    random.randrange(${len})    random
    ${modified_contact}    Get From List    ${old_list}  ${index}
    ${contact} =    New Contact  Petr  Petrov  Omsk
    Modify Contact  ${modified_contact}   ${contact}
    ${new_list} =    Get Contact List
    Remove Values From List  ${old_list}  ${modified_contact}
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

