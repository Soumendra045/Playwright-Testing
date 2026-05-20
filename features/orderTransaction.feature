Feature: Order Transaction
    Tests related to order Transaction

    Scenario Outline: verify order success message shown in details page
        Given Place the item order with <username> and <password>
        And the user is on landing page
        When  I login to portal with <username> and <password>
        And navigate to orders page
        And select the OrderId
        Then order message is successfully displayed
        Examples: 
            | username                  | password   |    
            | rsoumendra15@gmail.com    | Silu@0045  |
            
       
        
    
    
