from __future__ import absolute_import, unicode_literals


from substrapp.ledger_utils import invokeLedger


def createLedgerTraintuple(args, sync=False):
    return invokeLedger(fcn='createTraintuple', args=args, sync=sync)
