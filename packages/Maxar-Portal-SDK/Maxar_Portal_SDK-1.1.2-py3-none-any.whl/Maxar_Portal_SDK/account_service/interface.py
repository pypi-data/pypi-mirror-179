from Maxar_Portal_SDK.account_service.users import Users
from Maxar_Portal_SDK.account_service.roles import Roles
from Maxar_Portal_SDK.account_service.accounts import Info, Account, Comment
from Maxar_Portal_SDK.account_service.activations import Activations
from Maxar_Portal_SDK.account_service.rate_tables import RateTables
from Maxar_Portal_SDK.account_service.rate_tables import Table_Info
from Maxar_Portal_SDK.account_service.addresses import Address
from Maxar_Portal_SDK.account_service.products import Products
from Maxar_Portal_SDK.account_service.usage import Usage


import warnings
warnings.filterwarnings("ignore")

class Interface:
    """
    The primary interface for interacting with the Account Services classes.
    Args:
        username (string) = The username if your connectId requires Auth
        password (string) = The password associated with your username
    """

    def __init__(self, auth):
        self.auth = auth
        self.account_info = Info(self.auth)
        self.accounts = Account(self.auth)
        self.comments = Comment(self.auth)
        self.users = Users(self.auth)
        self.roles = Roles(self.auth)
        self.rate_table_info = Table_Info(self.auth)
        self.rate_table = RateTables(self.auth)
        self.address = Address(self.auth)
        self.activations = Activations(self.auth)
        self.products = Products(self.auth)
        self.usage = Usage(self.auth)

    def Search(self, search_type, search_term):
        """
        Function searches through the desired search type (ex. account) and lists the details of the search type that
        match the search term
        Args:
            search_type (string) = Desired level to search through. Options are:
                account
                activation
                user
            search_term (string) = Desired search term that searchers through one of the following categories:
                account:
                    account numbers
                    account names
                    SAP license ids
                    sold to
                    licensees
                activation:
                    activation numbers
                    SAP contract identifiers
                    SAP line items
                    start dates
                    end dates
                    account numbers
                    account ids
                user:
                    usernames
                    roles
                    activation numbers
                    account numbers
        Returns:
            Dictionary of the found account(s), activation(s), or user(s)
        """

        if search_type.lower() == "activation":
            results = self.activations.Search(search_term)
        elif search_type.lower() == "user":
            results = self.users.Search(search_term)
        else:
            raise Exception("{} is not a valid search type. Please enter a valid search type".format(search_type))
        return results