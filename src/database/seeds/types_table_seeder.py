from orator.seeds import Seeder


class typesTableSeeder(Seeder):

    def run(self):
        self.db.table('types').insert({
            'name': 'FEUILLE_DE_SOIN',
            'integer': 2,
            'select_order': 1
        })

        self.db.table('FACTURE').insert({
            'name': '',
            'integer': 2,
            'select_order': 1
        })

