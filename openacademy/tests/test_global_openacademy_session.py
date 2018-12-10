# -*- coding: utf-8 -*-

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class GlobalTestOpenAcademySession(TransactionCase):
    '''
    This create global test to session
    '''
    # Seudo - constructor method
    def setUp(self):
        super(GlobalTestOpenAcademySession, self).setUp()
        self.session = self.env['openacademy.session']
        self.partner = self.env.ref('base.res_partner_10')
        self.course = self.env.ref('openacademy.course1')
        self.partner_attende = self.env.ref('base.res_partner_2')

# Generic method
# Test methods
    def test_10_instructor_is_attende(self):
        '''
        Check that raise of 'A session's instructor can't be an attendee'
        '''
        with self.assertRaisesRegexp(
                ValidationError,
                "A session's instructor can't be an attendee"):
            self.session.create({
                'name': 'Session test 1',
                'seats': 1,
                'instructor_id': self.partner.id,
                'attendee_ids': [(6, 0, [self.partner.id])],
                'course_id': self.course.id,
            })

    def test_20_wkf_done(self):
        '''
        Check that the workflow work fine!
        '''
# session_test = self.session.create({
# 'name': 'Session test 1',
# 'seats': 1,
# 'instructor_id': self.partner.id,
# 'attendee_ids': [(6, 0, [self.partner_attende.id])],
# 'course_id': self.course.id,
# })
# session_test.signal_workflow('button_confirm')
# NOTA:A partir del minuto 1:39 del video, el rgrep workflow .
# --include=*.py• | grep tests no mostró el método
# signal_workflow, luego openacademy_session_workflow.xml no está en el
# proyecto que he manejado en el curso
# AttributeError: 'openacademy.session' object has no attribute
# 'signal_workflow' Min 1:48 la funcionalidad mostrada no coincide
# con el openacademy de mi curso.
# self.assertEqual(session_test.state, 'draft',
# 'Initial state should be in "draft"')
# print ("session_test.state", session_test.state)
# NOTA: No se tiene definida la variable state
