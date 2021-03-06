# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
#                       Pedro M. Baeza Romero <pedro.baeza@serviciosbaeza.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Account tax report without zeroes',
    'version': '1.0',
    'category': 'Custom modifications',
    'description': """
Account tax report without zeroes
=================================

Replace current taxes report that lies on Accounting > Reporting > Generic
Reporting > Taxes with one that doesn't print lines with zero in taxes amount.
    """,
    'author': 'Serv. Tecnológ. Avanzados - Pedro M. Baeza',
    'website': 'http://www.serviciosbaeza.com',
    'depends': [
        'account',
    ],
    'data': [
        'report/account_tax_report_no_zeroes_report.xml',
    ],
    'installable': True,
}
