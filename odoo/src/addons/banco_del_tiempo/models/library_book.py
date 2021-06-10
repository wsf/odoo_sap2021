# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import UserError


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Banco del Tiempo'

    name = fields.Char('Donación', required=True)
    date_release = fields.Date('Vencimiento')
    active = fields.Boolean(default=True)
    author_ids = fields.Many2many('res.partner',string='Voluntario')
    beneficiario_ids = fields.Many2one('res.partner', string='Beneficiario')
    state = fields.Selection(
        [('available', 'Disponible'),
         ('borrowed', 'En evaluación'),
         ('lost', 'No disponible')],
        'State', default="available")
    cost_price = fields.Float('Cantidad de Horas')
    category_id = fields.Many2one('library.book.category')

    def make_available(self):
        self.ensure_one()
        self.state = 'available'

    def make_borrowed(self):
        self.ensure_one()
        self.state = 'borrowed'

    def make_lost(self):
        self.ensure_one()
        self.state = 'lost'

    def book_rent(self):
        self.ensure_one()
        if self.state != 'available':
            raise UserError(_('Donación no disponible'))
        rent_as_superuser = self.env['library.book.rent'].sudo()
        rent_as_superuser.create({
            'book_id': self.id,
            'borrower_id': self.env.user.partner_id.id,
        })
