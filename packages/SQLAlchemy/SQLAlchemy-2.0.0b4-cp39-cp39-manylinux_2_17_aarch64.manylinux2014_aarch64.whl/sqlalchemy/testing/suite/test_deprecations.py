# mypy: ignore-errors

from .. import fixtures
from ..assertions import eq_
from ..schema import Column
from ..schema import Table
from ... import Integer
from ... import select
from ... import testing
from ... import union


class DeprecatedCompoundSelectTest(fixtures.TablesTest):
    __backend__ = True

    @classmethod
    def define_tables(cls, metadata):
        Table(
            "some_table",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("x", Integer),
            Column("y", Integer),
        )

    @classmethod
    def insert_data(cls, connection):
        connection.execute(
            cls.tables.some_table.insert(),
            [
                {"id": 1, "x": 1, "y": 2},
                {"id": 2, "x": 2, "y": 3},
                {"id": 3, "x": 3, "y": 4},
                {"id": 4, "x": 4, "y": 5},
            ],
        )

    def _assert_result(self, conn, select, result, params=()):
        eq_(conn.execute(select, params).fetchall(), result)

    def test_plain_union(self, connection):
        table = self.tables.some_table
        s1 = select(table).where(table.c.id == 2)
        s2 = select(table).where(table.c.id == 3)

        u1 = union(s1, s2)
        with testing.expect_deprecated(
            "The SelectBase.c and SelectBase.columns "
            "attributes are deprecated"
        ):
            self._assert_result(
                connection, u1.order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)]
            )

    # note we've had to remove one use case entirely, which is this
    # one.   the Select gets its FROMS from the WHERE clause and the
    # columns clause, but not the ORDER BY, which means the old ".c" system
    # allowed you to "order_by(s.c.foo)" to get an unnamed column in the
    # ORDER BY without adding the SELECT into the FROM and breaking the
    # query.  Users will have to adjust for this use case if they were doing
    # it before.
    def _dont_test_select_from_plain_union(self, connection):
        table = self.tables.some_table
        s1 = select(table).where(table.c.id == 2)
        s2 = select(table).where(table.c.id == 3)

        u1 = union(s1, s2).alias().select()
        with testing.expect_deprecated(
            "The SelectBase.c and SelectBase.columns "
            "attributes are deprecated"
        ):
            self._assert_result(
                connection, u1.order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)]
            )

    @testing.requires.order_by_col_from_union
    @testing.requires.parens_in_union_contained_select_w_limit_offset
    def test_limit_offset_selectable_in_unions(self, connection):
        table = self.tables.some_table
        s1 = select(table).where(table.c.id == 2).limit(1).order_by(table.c.id)
        s2 = select(table).where(table.c.id == 3).limit(1).order_by(table.c.id)

        u1 = union(s1, s2).limit(2)
        with testing.expect_deprecated(
            "The SelectBase.c and SelectBase.columns "
            "attributes are deprecated"
        ):
            self._assert_result(
                connection, u1.order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)]
            )

    @testing.requires.parens_in_union_contained_select_wo_limit_offset
    def test_order_by_selectable_in_unions(self, connection):
        table = self.tables.some_table
        s1 = select(table).where(table.c.id == 2).order_by(table.c.id)
        s2 = select(table).where(table.c.id == 3).order_by(table.c.id)

        u1 = union(s1, s2).limit(2)
        with testing.expect_deprecated(
            "The SelectBase.c and SelectBase.columns "
            "attributes are deprecated"
        ):
            self._assert_result(
                connection, u1.order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)]
            )

    def test_distinct_selectable_in_unions(self, connection):
        table = self.tables.some_table
        s1 = select(table).where(table.c.id == 2).distinct()
        s2 = select(table).where(table.c.id == 3).distinct()

        u1 = union(s1, s2).limit(2)
        with testing.expect_deprecated(
            "The SelectBase.c and SelectBase.columns "
            "attributes are deprecated"
        ):
            self._assert_result(
                connection, u1.order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)]
            )

    def test_limit_offset_aliased_selectable_in_unions(self, connection):
        table = self.tables.some_table
        s1 = (
            select(table)
            .where(table.c.id == 2)
            .limit(1)
            .order_by(table.c.id)
            .alias()
            .select()
        )
        s2 = (
            select(table)
            .where(table.c.id == 3)
            .limit(1)
            .order_by(table.c.id)
            .alias()
            .select()
        )

        u1 = union(s1, s2).limit(2)
        with testing.expect_deprecated(
            "The SelectBase.c and SelectBase.columns "
            "attributes are deprecated"
        ):
            self._assert_result(
                connection, u1.order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)]
            )
