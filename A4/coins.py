#name: Kheir Eddine Nizar
#mcgill id: 261104927
import requests

def dict_to_query(dic):
    """
    (dict)->str
    a function dict_to_query that takes a dictionary as input, and returns a string containing the keys and values of the dictionary with
    the format 'key=value', and ampersands ('&') separating each.
    >>> dict_to_query({'email': 'jonathan.campbell@mcgill.ca', 'token': 'ABC'})
    'email=jonathan.campbell@mcgill.ca&token=ABC'
    
    >>> dict_to_query({'name':'Nizar','last name':'Kheir Eddine'})
    'name=Nizar&last name=Kheir Eddine'
    
    >>> dict_to_query({'class':'comp202'})
    'class=comp202'
    """
    string=''
    for key in dic:
        string+=str(key)+'='+str(dic[key])+'&'
    return string[:-1]
    

class Account:
    """
    A class to represent a student's account.
    instance attributes:
    * email: str
    * token: str
    class attributes:
    * API_URL: str
    * valid_endpoints: str
    """
    API_URL='https://coinsbot202.herokuapp.com/api/'
    valid_endpoints=['balance','transfer']
    def __init__(self,email,token):
        """
        (str,str)->Nonetype
        Creates an object of type Account.
        >>> my_acct = Account("nizar.kheireddine@gmail.ca", "uTTAkCR3XCPuKY4u")
        Traceback (most recent call last):
        AssertionError: The email or token you used are not valid!
        
        >>> my_acct = Account("nizar.kheireddine@mail.mcgill.ca", "uTTAkCR3XCPuKY4u")
        >>> my_acct.email
        nizar.kheireddine@mail.mcgill.ca
        
        >>> acct = Account("jonathan.campbell@mcgill.ca", "ABC")
        >>> acct.token
        'ABC'
        """
        if type(email)!=str or email[-9:]!='mcgill.ca' or  type(token)!=str:
            raise AssertionError("The email or token you used are not valid!")
        self.email=email
        self.token=token
        self.balance=-1
        self.request_log=[]
    
    
    def __str__(self):
        """
        ()->str
        returns a string of the format 'EMAIL has balance BALANCE' where EMAIL and BALANCE refer to the appropriate instance attributes.
        >>> print(Account("nizar.kheireddine@gmail.ca", "uTTAkCR3XCPuKY4u"))
        Traceback (most recent call last):
        AssertionError: The email or token you used are not valid!
        
        >>> my_acct = Account("nizar.kheireddine@mail.mcgill.ca", "uTTAkCR3XCPuKY4u")
        >>> my_acct.retrieve_balance()
        1450
        >>> print(my_acct)
        nizar.kheireddine@mail.mcgill.ca has balance 1450
        
        >>> acct = Account("jonathan.campbell@mcgill.ca", "ABC")
        >>> print(acct)
        jonathan.campbell@mcgill.ca has balance -1
        """
        return self.email+' has balance '+str(self.balance)
    
    
    def call_api(self,endpoint,dic):
        """
        (string,dict)->dict
        takes an endpoint (string) and request dictionary as explicitinputs. If the types of the inputs are incorrect or the endpoint is
        not valid, raise anAssertionError. The method should add the key 'token' into the dictionary with value givenby the instance
        attribute of the same name. It should then construct an API request URL andsend the request as indicated on the previous page. If
        the 'status' in the result dictionaryis not 'OK', raise an AssertionError with the value for the 'message' key as error message.
        Otherwise, return the result dictionary.
        >>> my_acct = Account("jonathan.campbell@mcgill.ca", "ABC")
        >>> my_acct.call_api("balance", {'email': my_acct.email})
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sentover Slack.
        
        >>> my_acct = Account("nizar.kheireddine@mail.mcgill.ca", "uTTAkCR3XCPuKY4u")        
        >>> my_acct.call_api("balance", {'email': "nizar.kheireddine@gmail.com"})
        Traceback (most recent call last):
        AssertionError: The API cannot be called, pleave verify that your dictionnary and endpoint are valid.
        
        >>> my_acct = Account("nizar.kheireddine@mail.mcgill.ca", "uTTAkCR3XCPuKY4u")        
        >>> my_acct.call_api("somethingggg", {'email': my_acct.email})
        Traceback (most recent call last):
        AssertionError: The API cannot be called, pleave verify that your dictionnary and endpoint are valid.

        """
        if type(endpoint)!=str or type(dic)!=dict or not endpoint in self.valid_endpoints :
            raise AssertionError("The API cannot be called, pleave verify that your dictionnary and endpoint are valid")
        dic['token']=self.token
        request_url=self.API_URL+endpoint+'?'+dict_to_query(dic)
        request_dict=requests.get(url=request_url).json()
        if not request_dict['status']=='OK':
            raise AssertionError(request_dict['message'])
        return request_dict
    
    
    def retrieve_balance(self):
        """
        ()->int
        >>> my_acct = my_acct = Account("nizar.kheireddine@mail.mcgill.ca", "uTTAkCR3XCPuKY4u")
        >>> my_acct.retrieve_balance()
        1450
        
        >>> my_acct = Account("jonathan.campbell@mcgill.ca", "ABCD")
        >>> my_acct.retrieve_balance()
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sent over Slack.
        
        >>> my_acct = my_acct = Account("nizar.kheireddine@gmail.com", "uTTAkCR3XCPuKY4u")
        >>> my_acct.retrieve_balance()
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sent over Slack.
        """
        self.balance=self.call_api('balance',{'email':self.email})['message']
        return self.balance
    
    
    def transfer(self,coins,email_receiver):
        """
        (int,string)->int
        >>> my_acct = Account("nizar.kheireddine@mail.mcgill.ca", "uTTAkCR3XCPuKY4u")
        >>> my_acct.retrieve_balance()
        1475
        >>> my_acct.transfer(25, "alexa.infelise@mail.mcgill.ca")
        'You have transferred 25 coins of your balance of 25 coins to alexa.infelise@mail.mcgill.ca. Your balance is now 1450.'
        
        >>> my_acct = Account("nizar.kheireddine@mail.mcgill.ca", "uTTAkCR3XCPuKY4u")
        >>> my_acct.retrieve_balance()
        1475
        >>> my_acct.transfer(5000000, "alexa.infelise@mail.mcgill.ca")
        Traceback (most recent call last):
        AssertionError: The transfer cannot happen, please verify that the amount of coins and and email are valid for this operation.
        
        >>> my_acct = Account("nizar.kheireddine@mail.mcgill.ca", "uTTAkCR3XCPuKY4u")
        >>> my_acct.retrieve_balance()
        1475
        >>> my_acct.transfer(50, my_acct.email)
        Traceback (most recent call last):
        AssertionError: The transfer cannot happen, please verify that the amount of coins and and email are valid for this operation.
        
        """
        
        if type(email_receiver)!=str or type(coins)!=int or email_receiver[-9:]!='mcgill.ca' or self.email==email_receiver or coins<25 or \
        coins> self.balance:
            raise AssertionError("The transfer cannot happen, please verify that the amount of coins and and email are valid for this operation.")
        dic={'balance':self.balance,'withdrawal_email':self.email,'deposit_email':email_receiver,'amount':coins}
        return self.call_api('transfer',dic)['message']








