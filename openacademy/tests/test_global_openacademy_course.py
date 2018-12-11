# -*- coding: utf-8 -*-

from psycopg2 import IntegrityError

from openerp.tests.common import TransactionCase
from openerp.tools import mute_logger

# Global test to openacademy course model
# Test create course and trigger constraints.
# Method seudo-constructor of test setUp
# Define global variables to tests methods
class GlobalTestOpenAcademyCourse(TransactionCase):
    def setUp(self):
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.course = self.env['openacademy.course']
# Method of class that don't is test -
# Create a course with parameters received.

    def create_course(self, course_name,
                      course_description, course_responsible_id):
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id,
            })
        return course_id

# Method of test startswith 'def test_*(self):'
# Mute the error odoo.sql.db to avoid it in log
# Test create a course with same name and description
# To raise constraint of name different to description
# Error raised expected with message expected-
    @mute_logger('odoo.sql_db')
    def test_10_same_name_and_description(self):
        with self.assertRaisesRegexp(
                IntegrityError, 'new row for relation "openacademy_course" '
                'violates check constraint "openacademy_course'
                '_name_description_check"'):
            self.create_course('test', 'test', None)

    @mute_logger('odoo.sql_db')
    def test_20_two_courses_same_name(self):
        '''
        Test to create two courses with same name.
        To raise constraint of unique name
        '''

        new_id = self.create_course('test1', 'test_description', None)
        print("new_id", new_id)
        with self.assertRaisesRegexp(
                IntegrityError,
                'duplicate key value violates'
                ' unique constraint "openacademy_course_name_unique"'):
            new_id2 = self.create_course('test1', 'test_description', None)
            print("new_id2", new_id2)

    def test_15_duplicate_course(self):
        '''
        Test to duplicate a course and check work fine!
        '''
        course = self.env.ref('openacademy.course0')
        course_id = course.copy()
        print("course_id", course_id)
