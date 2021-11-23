# Stdlib imports
# Third-party app imports
from factory import Faker as FactoryFaker
from factory import SubFactory, lazy_attribute

# Imports from my app


class UserFactory:
    name = FactoryFaker("name")
    email = FactoryFaker("email")


class DatasetFactory:
    name = FactoryFaker("hexify", text="^^^^^^^^^^")


class GroupFactory:
    name = FactoryFaker("hexify", text="^^^^^^^^^^")


class ParametersFactory:
    def __init__(self):
        _ = {}
        grp = SubFactory(GroupFactory)
        user = SubFactory(UserFactory)
        ds = SubFactory(DatasetFactory)
        _["google_users"] = {grp.name: user.email}
        _["dataset_ids"] = {grp.name: ds.name}

        self.params = _
