from orator.seeds import Seeder


class UsersTableSeeder(Seeder):

    def run(self):
        self.db.table('users').insert({
            'email': 'Yasser@yasser.com',
            'password': '$2b$16$7QD5khQQ4L4QQ6VrHPGJYe5uXcOBcSsyulnisIa7fIiXUL42ctvzy',
        })

