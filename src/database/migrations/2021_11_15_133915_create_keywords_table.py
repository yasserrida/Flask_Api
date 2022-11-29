from orator.migrations import Migration


class CreateKeywordsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('keywords') as table:
            table.increments('id')
            table.string('keyword')
            table.integer('poid').default(1)
            table.integer('type_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('keywords')
