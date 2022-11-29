from orator.seeds import Seeder


class KeyswordsTableSeeder(Seeder):

    def run(self):
        FEUILLE_DE_SOIN={
            'Word 1',
            'Word 2',
            'Word 3',
            'Word 4',
            'Word 5',
            'Word 6',
        }

        FACTURE={ 'Word 1',
            'Word 7',
            'Word 8',
            'Word 9',
            'Word 10',
            'Word 11'
        }
        for s in FEUILLE_DE_SOIN:
            self.db.table('keywords').insert({
                'keyword': s,
                'type_id': 2,
            })

        for f in FACTURE:
            self.db.table('keywords').insert({
                'keyword': f,
                'type_id': 2,
            })
        pass

