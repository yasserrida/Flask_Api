from orator.seeds import Seeder
from users_table_seeder import UsersTableSeeder
from api_credentials_table_seeder import ApiCredentialsTableSeeder
from types_table_seeder import typesTableSeeder
from keyswords_table_seeder import KeyswordsTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        self.call(UsersTableSeeder)
        self.call(ApiCredentialsTableSeeder)
        self.call(typesTableSeeder)
        self.call(KeyswordsTableSeeder)
        pass

