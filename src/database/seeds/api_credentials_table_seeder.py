from orator.seeds import Seeder


class ApiCredentialsTableSeeder(Seeder):

    def run(self):
        self.db.table('api_credentials').insert({
            'title': 'Yasser',
            'app_key': '08xkUvyOeRSLfvW-AlzdSQ',
            'app_secret': 'yemys44jdhKblZIezZRnC1PgcwkqkJ8H4eJYYfqRGP5QQsxb'
        })

