from orator.migrations import Migration


class CreateTypesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('types') as table:
            table.increments('id')
            table.string('name')
            table.integer('rule')
            table.integer('select_order')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('types')
