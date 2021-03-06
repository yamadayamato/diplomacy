import unittest

from adjudicator.order import Build
from adjudicator.piece import Army, Fleet, PieceTypes
from adjudicator.processor import process
from adjudicator.tests.data import NamedCoasts, Nations, Territories

from ..base import AdjudicatorTestCaseMixin


class TestBuilding(AdjudicatorTestCaseMixin, unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.territories = Territories(self.state)
        self.named_coasts = NamedCoasts(self.state, self.territories)

    def test_fleets_cannot_be_built_inland(self):
        """
        Physically this is possible, but it is still not allowed.

        Russia has one build and Moscow is empty.

        Russia:
        Build F Moscow
        See issue 4.C.4. Some game masters will change the order and build an
        army in Moscow.

        I prefer that the build fails.
        """
        orders = [
            Build(self.state, 0, Nations.RUSSIA, self.territories.MOSCOW, PieceTypes.FLEET),
        ]
        process(self.state)

        self.assertTrue(orders[0].illegal)
        self.assertEqual(orders[0].illegal_code, '015')
        self.assertEqual(
            orders[0].illegal_verbose,
            'Piece type cannot exist in this type of territory.'
        )

    def test_supply_center_must_be_empty_for_building(self):
        """
        You can't have two units in a sector. So, you can't build when there is a unit in the supply center.

        Germany may build a unit but has an army in Berlin. Germany orders the following:

        Germany:
        Build A Berlin

        Build fails.
        """
        Army(self.state, 0, Nations.GERMANY, self.territories.BERLIN),
        orders = [
            Build(self.state, 0, Nations.GERMANY, self.territories.BERLIN, PieceTypes.ARMY),
        ]
        process(self.state)

        self.assertTrue(orders[0].illegal)
        self.assertEqual(orders[0].illegal_code, '011')
        self.assertEqual(
            orders[0].illegal_verbose,
            'Source is already occupied by a piece.'
        )

    def test_both_coasts_must_be_empty_for_building(self):
        """
        If a sector is occupied on one coast, the other coast can not be used
        for building.

        Russia may build a unit and has a fleet in St Petersburg(sc). Russia
        orders the following:

        Russia:
        Build A St Petersburg(nc)

        Build fails.
        """
        Fleet(self.state, 0, Nations.RUSSIA, self.territories.ST_PETERSBURG, self.named_coasts.ST_PETERSBURG_NC),
        orders = [
            Build(self.state, 0, Nations.RUSSIA, self.territories.ST_PETERSBURG, PieceTypes.FLEET, self.named_coasts.ST_PETERSBURG_SC),
        ]
        process(self.state)

        self.assertTrue(orders[0].illegal)
        self.assertEqual(orders[0].illegal_code, '011')
        self.assertEqual(
            orders[0].illegal_verbose,
            'Source is already occupied by a piece.'
        )

    def test_building_in_home_supply_center_that_is_not_owned(self):
        """
        Building a unit is only allowed when supply center is a home supply
        center and is owned. If not owned, build fails.
        """
        self.territories.ST_PETERSBURG.controlled_by = Nations.GERMANY
        orders = [
            Build(self.state, 0, Nations.RUSSIA, self.territories.ST_PETERSBURG, PieceTypes.FLEET, self.named_coasts.ST_PETERSBURG_SC),
        ]
        process(self.state)

        self.assertTrue(orders[0].illegal)
        self.assertEqual(orders[0].illegal_code, '014')
        self.assertEqual(
            orders[0].illegal_verbose,
            ('Cannot build in a supply center which is controlled by a '
             'foreign power.')
        )

    def test_building_in_owned_supply_center_that_is_not_home(self):
        """
        Building a unit is only allowed when supply center is a home supply
        center and is owned. If it is not a home supply center, the build fails.
        """
        self.territories.ST_PETERSBURG.controlled_by = Nations.GERMANY
        orders = [
            Build(self.state, 0, Nations.GERMANY, self.territories.ST_PETERSBURG, PieceTypes.FLEET, self.named_coasts.ST_PETERSBURG_SC),
        ]
        process(self.state)

        self.assertTrue(orders[0].illegal)
        self.assertEqual(orders[0].illegal_code, '013')
        self.assertEqual(
            orders[0].illegal_verbose,
            'Source is outside of national borders.'
        )
