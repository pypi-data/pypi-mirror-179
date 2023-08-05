# -*- coding: utf-8 -*-
# This file is part of the cashbook-module from m-ds for Tryton.
# The COPYRIGHT file at the top level of this repository contains the
# full copyright notices and license terms.

from trytond.model import Workflow, ModelView, ModelSQL, fields, Check, tree
from trytond.pyson import Eval, Or, Bool, Id, Len
from trytond.exceptions import UserError
from trytond.i18n import gettext
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.report import Report
from decimal import Decimal
from sql import Literal
from sql.aggregate import Sum
from sql.conditionals import Case, Coalesce
from sql.functions import CurrentDate
from .model import order_name_hierarchical


STATES = {
    'readonly': Eval('state', '') != 'open',
    }
DEPENDS=['state']

# states in case of 'btype'!=None
STATES2 = {
    'readonly': Or(
            Eval('state', '') != 'open',
            ~Bool(Eval('btype')),
        ),
    'invisible': ~Bool(Eval('btype')),
    }
STATES3 = {}
STATES3.update(STATES2)
STATES3['required'] = ~STATES2['invisible']
DEPENDS2 = ['state', 'btype']

sel_state_book = [
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('archive', 'Archive'),
    ]


class Book(tree(separator='/'), Workflow, ModelSQL, ModelView):
    'Cashbook'
    __name__ = 'cashbook.book'

    company = fields.Many2One(string='Company', model_name='company.company',
        required=True, ondelete="RESTRICT")
    name = fields.Char(string='Name', required=True,
        states=STATES, depends=DEPENDS)
    description = fields.Text(string='Description',
        states=STATES, depends=DEPENDS)
    btype = fields.Many2One(string='Type',
        help='A cash book with type can contain postings. Without type is a view.',
        model_name='cashbook.type', ondelete='RESTRICT',
        states={
            'readonly': Or(
                    STATES['readonly'],
                    Len(Eval('lines')) > 0,
                ),
        }, depends=DEPENDS+['lines'])
    owner = fields.Many2One(string='Owner', required=True, select=True,
        model_name='res.user', ondelete='SET NULL',
        states=STATES, depends=DEPENDS)
    reviewer = fields.Many2One(string='Reviewer', select=True,
        help='Group of users who have write access to the cashbook.',
        model_name='res.group', ondelete='SET NULL',
        states=STATES, depends=DEPENDS)
    observer = fields.Many2One(string='Observer', select=True,
        help='Group of users who have read-only access to the cashbook.',
        model_name='res.group', ondelete='SET NULL',
        states=STATES, depends=DEPENDS)
    lines = fields.One2Many(string='Lines', field='cashbook',
        model_name='cashbook.line',
        states=STATES, depends=DEPENDS)
    reconciliations = fields.One2Many(string='Reconciliations',
        field='cashbook', model_name='cashbook.recon',
        states=STATES2, depends=DEPENDS2)
    number_sequ = fields.Many2One(string='Line numbering',
        help='Number sequence for numbering of the cash book lines.',
        model_name='ir.sequence',
        domain=[
            ('sequence_type', '=', Id('cashbook', 'sequence_type_cashbook_line')),
            ['OR',
                ('company', '=', None),
                ('company', '=', Eval('company', -1)),
                ],
            ],
        states=STATES3, depends=DEPENDS2+['company'])
    number_atcheck = fields.Boolean(string="number when 'Checking'",
        help="The numbering of the lines is done in the step Check. If the check mark is inactive, this happens with Done.",
        states=STATES2, depends=DEPENDS2)
    start_date = fields.Date(string='Initial Date',
        states={
            'readonly': Or(
                STATES2['readonly'],
                Len(Eval('lines')) > 0,
                ),
            'invisible': STATES2['invisible'],
            'required': ~STATES2['invisible'],
        }, depends=DEPENDS2+['lines'])
    balance = fields.Function(fields.Numeric(string='Balance', readonly=True,
        help='Balance of bookings to date',
        digits=(16, Eval('currency_digits', 2)),
        depends=['currency_digits']), 'on_change_with_balance')
    balance_all = fields.Function(fields.Numeric(string='Total balance',
        readonly=True, help='Balance of all bookings',
        digits=(16, Eval('currency_digits', 2)),
        depends=['currency_digits']), 'on_change_with_balance_all')

    balance_ref = fields.Function(fields.Numeric(string='Balance (Ref.)',
        help='Balance in company currency',
        readonly=True, digits=(16, Eval('company_currency_digits', 2)),
        states={
            'invisible': ~Bool(Eval('company_currency')),
        }, depends=['company_currency_digits', 'company_currency']),
        'on_change_with_balance_ref')
    company_currency = fields.Function(fields.Many2One(readonly=True,
        string='Company Currency', states={'invisible': True},
        model_name='currency.currency'),
        'on_change_with_company_currency')
    company_currency_digits = fields.Function(fields.Integer(
        string='Currency Digits (Ref.)', readonly=True),
        'on_change_with_currency_digits')

    currency = fields.Many2One(string='Currency', select=True,
        model_name='currency.currency',
        states={
            'readonly': Or(
                STATES2['readonly'],
                Len(Eval('lines', [])) > 0,
                ),
        }, depends=DEPENDS2+['lines'])
    currency_digits = fields.Function(fields.Integer(string='Currency Digits',
        readonly=True), 'on_change_with_currency_digits')
    state = fields.Selection(string='State', required=True,
        readonly=True, selection=sel_state_book)
    state_string = state.translated('state')

    parent = fields.Many2One(string="Parent",
        model_name='cashbook.book', ondelete='RESTRICT',
        left='left', right='right')
    childs = fields.One2Many(string='Children', field='parent',
        model_name='cashbook.book')
    left = fields.Integer(string='Left', required=True, select=True)
    right = fields.Integer(string='Right', required=True, select=True)

    @classmethod
    def __register__(cls, module_name):
        super(Book, cls).__register__(module_name)

        table = cls.__table_handler__(module_name)
        table.drop_column('start_balance')

    @classmethod
    def __setup__(cls):
        super(Book, cls).__setup__()
        cls._order.insert(0, ('rec_name', 'ASC'))
        cls._order.insert(0, ('state', 'ASC'))
        t = cls.__table__()
        cls._sql_constraints.extend([
            ('state_val',
                Check(t, t.state.in_(['open', 'closed', 'archive'])),
                'cashbook.msg_book_wrong_state_value'),
            ])
        cls._transitions |= set((
                ('open', 'closed'),
                ('closed', 'open'),
                ('closed', 'archive'),
            ))
        cls._buttons.update({
            'wfopen': {
                'invisible': Eval('state', '') != 'closed',
                'depends': ['state'],
                },
            'wfclosed': {
                'invisible': Eval('state') != 'open',
                'depends': ['state'],
                },
            'wfarchive': {
                'invisible': Eval('state') != 'closed',
                'depends': ['state'],
                },
            })

    @staticmethod
    def default_left():
        return 0

    @staticmethod
    def default_right():
        return 0

    @classmethod
    def default_number_atcheck(cls):
        return True

    @classmethod
    def default_currency(cls):
        """ currency of company
        """
        Company = Pool().get('company.company')

        company = cls.default_company()
        if company:
            company = Company(company)
            if company.currency:
                return company.currency.id

    @staticmethod
    def default_company():
        return Transaction().context.get('company') or None

    @classmethod
    def default_start_date(cls):
        """ today
        """
        IrDate = Pool().get('ir.date')
        return IrDate.today()

    @classmethod
    def default_state(cls):
        return 'open'

    @classmethod
    def default_owner(cls):
        """ default: current user
        """
        return Transaction().user

    @staticmethod
    def order_state(tables):
        """ edit = 0, check/done = 1
        """
        Book2 = Pool().get('cashbook.book')
        tab_book = Book2.__table__()
        table, _ = tables[None]

        query = tab_book.select(
                Case(
                    (tab_book.state == 'open', 0),
                    else_ = 1),
                where=tab_book.id==table.id
                )
        return [query]

    @staticmethod
    def order_rec_name(tables):
        """ order by pos
            a recursive sorting
        """
        return order_name_hierarchical('cashbook.book', tables)

    def get_rec_name(self, name):
        """ name, balance, state
        """
        recname = super(Book, self).get_rec_name(name)
        if self.btype:
            return '%(name)s | %(balance)s %(symbol)s | %(state)s' % {
                'name': recname or '-',
                'balance': Report.format_number(self.balance or 0.0, None),
                'symbol': getattr(self.currency, 'symbol', '-'),
                'state': self.state_string,
                }
        return recname

    def get_balance_of_cashbooks(self, date_limit=True):
        """ compute balance
        """
        pool = Pool()
        Book2 = pool.get('cashbook.book')
        Book3 = pool.get('cashbook.book')
        Line = pool.get('cashbook.line')
        Currency = pool.get('currency.currency')
        IrDate = pool.get('ir.date')

        tab_line = Line.__table__()
        tab_book = Book3.__table__()
        cursor = Transaction().connection.cursor()
        context = Transaction().context

        # select cashbook-lines from current cashbook and below
        query = [
                ('cashbook.id', 'in', Book2.search([
                        ('parent', 'child_of', [self.id]),
                    ], query=True)),
            ]
        if date_limit == True:
            dt1 = context.get('date', None)
            dt2 = IrDate.today()
            if not isinstance(dt1, type(dt2)):
                dt1 = dt2
            query.append(
                    ('date', '<=', dt1)
                )
        line_query = Line.search(query, query=True)

        # sum lines by currency
        bal_by_currency = line_query.join(tab_line,
                condition=tab_line.id==line_query.id,
            ).join(tab_book,
                condition=tab_book.id==tab_line.cashbook,
            ).select(
                Sum(tab_line.credit - tab_line.debit).as_('balance'),
                tab_book.currency,
                group_by=[tab_book.currency],
            )

        if self.id:
            total = Decimal('0.0')

            cursor.execute(*bal_by_currency)
            balance_lines = cursor.fetchall()

            for line in balance_lines:
                (balance, id_currency) = line

                total += Currency.compute(
                        Currency(id_currency),  # from
                        balance,
                        self.currency, # to
                    )
            return total

    @fields.depends('currency')
    def on_change_with_currency_digits(self, name=None):
        """ currency of cashbook
        """
        if self.currency:
            return self.currency.digits
        else:
            return 2

    @fields.depends('company', 'currency', 'btype')
    def on_change_with_company_currency(self, name=None):
        """ get company-currency if its different from current
            cashbook-currency, disable if book is a view
        """
        if self.company:
            if self.currency:
                if self.btype:
                    if self.company.currency.id != self.currency.id:
                        return self.company.currency.id

    @fields.depends('id')
    def on_change_with_balance(self, name=None):
        """ compute balance until today
        """
        return self.get_balance_of_cashbooks()

    @fields.depends('id')
    def on_change_with_balance_all(self, name=None):
        """ compute balance of all bookings
        """
        return self.get_balance_of_cashbooks(date_limit=False)

    @fields.depends('company', 'currency', 'id', 'btype')
    def on_change_with_balance_ref(self, name=None):
        """ balance converted to company-currency
        """
        pool = Pool()
        Line = pool.get('cashbook.line')
        tab_line = Line.__table__()
        cursor = Transaction().connection.cursor()

        if self.btype is None:
            return None

        query = tab_line.select(
                Sum(tab_line.credit - tab_line.debit),
                where = tab_line.cashbook == self.id,
            )

        if self.id:
            cursor.execute(*query)
            result = cursor.fetchone()
            balance = Decimal('0.0')
            if result:
                if result[0] is not None:
                    balance += result[0]
            if self.currency:
                return self.currency.compute(
                        self.currency,          # from
                        balance,
                        self.company.currency   # to
                    )

    @classmethod
    @ModelView.button
    @Workflow.transition('open')
    def wfopen(cls, books):
        """ open cashbook
        """
        pass

    @classmethod
    @ModelView.button
    @Workflow.transition('closed')
    def wfclosed(cls, books):
        """ cashbook is closed
        """
        pass

    @classmethod
    @ModelView.button
    @Workflow.transition('archive')
    def wfarchive(cls, books):
        """ cashbook is archived
        """
        pass

    @classmethod
    def write(cls, *args):
        """ deny update if book is not 'open'
        """
        ConfigUser = Pool().get('cashbook.configuration_user')

        actions = iter(args)
        to_write_config = []
        for books, values in zip(actions, actions):
            for book in books:
                # deny btype-->None if lines not empty
                if 'btype' in values.keys():
                    if (values['btype'] is None) and (len(book.lines) > 0):
                        raise UserError(gettext(
                            'cashbook.msg_book_btype_with_lines',
                            cbname = book.rec_name,
                            numlines = len(book.lines),
                            ))

                if book.state != 'open':
                    # allow state-update, if its the only action
                    if not (('state' in values.keys()) and (len(values.keys()) == 1)):
                        raise UserError(gettext(
                            'cashbook.msg_book_deny_write',
                            bookname = book.rec_name,
                            state_txt = book.state_string,
                            ))

                # if owner changes, remove book from user-config
                if 'owner' in values.keys():
                    if book.owner.id != values['owner']:
                        for x in ['defbook', 'book1', 'book2', 'book3',
                            'book4', 'book5']:
                            cfg1 = ConfigUser.search([
                                    ('iduser.id', '=', book.owner.id),
                                    ('%s.id' % x, '=', book.id),
                                ])
                            if len(cfg1) > 0:
                                to_write_config.extend([ cfg1, {x: None} ])
        super(Book, cls).write(*args)

        if len(to_write_config) > 0:
            ConfigUser.write(*to_write_config)

    @classmethod
    def delete(cls, books):
        """ deny delete if book has lines
        """
        for book in books:
            if (len(book.lines) > 0) and (book.state != 'archive'):
                raise UserError(gettext(
                    'cashbook.msg_book_deny_delete',
                    bookname = book.rec_name,
                    booklines = len(book.lines),
                    ))
        super(Book, cls).delete(books)

# end Book
