# -*- coding: utf-8 -*-

"""
    foulefactoryapilib.models.account_writer_service_model
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 09/16/2016
"""
import dateutil.parser
from .base_model import BaseModel

class AccountWriterServiceModel(BaseModel):

    """Implementation of the 'AccountWriterServiceModel' model.

    TODO: type model description here.

    Attributes:
        id_gender (int): TODO: type description here.
        first_name (string): TODO: type description here.
        name (string): TODO: type description here.
        email (string): TODO: type description here.
        phone (string): TODO: type description here.
        birthday (DateTime): TODO: type description here.
        address_1 (string): TODO: type description here.
        city (string): TODO: type description here.
        postal_code (string): TODO: type description here.
        country_code (string): TODO: type description here.
        nationality (string): TODO: type description here.
        optin (bool): TODO: type description here.
        company (string): TODO: type description here.
        address_2 (string): TODO: type description here.
        bill_address_1 (string): TODO: type description here.
        bill_address_2 (string): TODO: type description here.
        bill_city (string): TODO: type description here.
        bill_postal_code (string): TODO: type description here.

    """

    def __init__(self, 
                 id_gender = None,
                 first_name = None,
                 name = None,
                 email = None,
                 phone = None,
                 birthday = None,
                 address_1 = None,
                 city = None,
                 postal_code = None,
                 country_code = None,
                 nationality = None,
                 optin = None,
                 company = None,
                 address_2 = None,
                 bill_address_1 = None,
                 bill_address_2 = None,
                 bill_city = None,
                 bill_postal_code = None):
        """Constructor for the AccountWriterServiceModel class"""
        
        # Initialize members of the class
        self.id_gender = id_gender
        self.first_name = first_name
        self.name = name
        self.email = email
        self.phone = phone
        self.birthday = birthday
        self.address_1 = address_1
        self.city = city
        self.postal_code = postal_code
        self.country_code = country_code
        self.nationality = nationality
        self.optin = optin
        self.company = company
        self.address_2 = address_2
        self.bill_address_1 = bill_address_1
        self.bill_address_2 = bill_address_2
        self.bill_city = bill_city
        self.bill_postal_code = bill_postal_code

        # Create a mapping from Model property names to API property names
        self.names = {
            "id_gender" : "IdGender",
            "first_name" : "FirstName",
            "name" : "Name",
            "email" : "Email",
            "phone" : "Phone",
            "birthday" : "Birthday",
            "address_1" : "Address1",
            "city" : "City",
            "postal_code" : "PostalCode",
            "country_code" : "CountryCode",
            "nationality" : "Nationality",
            "optin" : "Optin",
            "company" : "Company",
            "address_2" : "Address2",
            "bill_address_1" : "BillAddress1",
            "bill_address_2" : "BillAddress2",
            "bill_city" : "BillCity",
            "bill_postal_code" : "BillPostalCode",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            id_gender = dictionary.get("IdGender")
            first_name = dictionary.get("FirstName")
            name = dictionary.get("Name")
            email = dictionary.get("Email")
            phone = dictionary.get("Phone")
            birthday = dateutil.parser.parse(dictionary.get("Birthday")) if dictionary.get("Birthday") else None
            address_1 = dictionary.get("Address1")
            city = dictionary.get("City")
            postal_code = dictionary.get("PostalCode")
            country_code = dictionary.get("CountryCode")
            nationality = dictionary.get("Nationality")
            optin = dictionary.get("Optin")
            company = dictionary.get("Company")
            address_2 = dictionary.get("Address2")
            bill_address_1 = dictionary.get("BillAddress1")
            bill_address_2 = dictionary.get("BillAddress2")
            bill_city = dictionary.get("BillCity")
            bill_postal_code = dictionary.get("BillPostalCode")
            # Return an object of this model
            return cls(id_gender,
                       first_name,
                       name,
                       email,
                       phone,
                       birthday,
                       address_1,
                       city,
                       postal_code,
                       country_code,
                       nationality,
                       optin,
                       company,
                       address_2,
                       bill_address_1,
                       bill_address_2,
                       bill_city,
                       bill_postal_code)
