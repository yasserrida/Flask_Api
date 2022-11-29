from orator.migrations import Migration


class CreateApiCredentialsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('api_credentials') as table:
            table.increments('id')
            table.string('title')
            table.string('app_key')
            table.string('app_secret')
            table.integer('is_valide').default(1)
            table.integer('user_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('api_credentials')
