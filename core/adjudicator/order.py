from .state import state
from . import decisions


class Order:

    def __init__(self, nation, source):
        state.all_orders.append(self)
        self.nation = nation
        self.source = source
        self._piece = None
        self._piece_cached = False
        self._hold_support_commands = []
        self._hold_support_commands_cached = False

    def __getattr__(self, name):
        """
        Adds the ability to ask an order what type it is using the syntax
        `order.is_<order_subclass>`.
        """
        subclasses = Order.__subclasses__()
        for s in subclasses:
            if name == 'is_' + s.__name__.lower():
                return isinstance(self, s)
        raise AttributeError(
            f'{self.__class__.__name__} has no attribute \'{name}\'.'
        )

    @property
    def piece(self):
        """
        Gets the `Piece` instance which exists in `self.source` or `None` if
        there is no piece in the territory.

        Returns:
            * `Piece` or `None`
        """
        if not self._piece_cached:
            for p in state.all_pieces:
                if p.territory == self.source:
                    self._piece = p
            self._piece_cached = True
        return self._piece

    # TODO test
    def hold_support(self, *args):
        if not self._hold_support_commands_cached:
            for order in state.all_orders:
                if order.is_support and order.aux == self.source and \
                        order.target == self.source:
                    self._hold_support_commands.append(order)
            self._hold_support_commands_cached = True
        return [s for s in self._hold_support_commands
                if s.support_decision() in args]


class Hold(Order):
    pass


class Move(Order):
    def __init__(self, nation, source, target, via_convoy=False):
        super().__init__(nation, source)
        self.target = target
        self.via_convoy = via_convoy
        self._move_support_commands = []
        self._move_support_commands_cached = False
        self.move_decision = decisions.Move(self)
        self.path_decision = decisions.Path(self)

    # TODO test
    # TODO DRY
    def move_support(self, *args):
        if not self._move_support_commands_cached:
            for order in state.all_orders:
                if order.is_support and order.aux == self.source and \
                        order.target == self.target:
                    self._move_support_commands.append(order)
            self._move_support_commands_cached = True
        return [s for s in self._move_support_commands
                if s.support_decision() in args]

    def is_head_to_head(self):
        """
        Determine whether the move is a head to head battle, i.e. the target
        piece is trying to move to this territory.

        Returns:
            * `bool`
        """
        opposing_piece = self.target.piece
        if opposing_piece:
            if opposing_piece.order.is_move:
                return opposing_piece.order.target == self
        return False


class Support(Order):
    def __init__(self, nation, source, aux, target):
        super().__init__(nation, source)
        self.aux = aux
        self.target = target


class Convoy(Order):
    def __init__(self, nation, source, aux, target):
        super().__init__(nation, source)
        self.aux = aux
        self.target = target
