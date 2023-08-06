# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest.mock import Mock, patch

import mysql.connector

import opentelemetry.instrumentation.mysql
from opentelemetry import trace as trace_api
from opentelemetry.instrumentation.mysql import MySQLInstrumentor
from opentelemetry.sdk import resources
from opentelemetry.test.test_base import TestBase


def mock_connect(*args, **kwargs):
    class MockConnection:
        def cursor(self):
            # pylint: disable=no-self-use
            return Mock()

    return MockConnection()


def connect_and_execute_query():
    cnx = mysql.connector.connect(database="test")
    cursor = cnx.cursor()
    query = "SELECT * FROM test"
    cursor.execute(query)

    return cnx, query


class TestMysqlIntegration(TestBase):
    def tearDown(self):
        super().tearDown()
        with self.disable_logging():
            MySQLInstrumentor().uninstrument()

    @patch("mysql.connector.connect", new=mock_connect)
    # pylint: disable=unused-argument
    def test_instrumentor(self):
        MySQLInstrumentor().instrument()

        connect_and_execute_query()

        spans_list = self.memory_exporter.get_finished_spans()
        self.assertEqual(len(spans_list), 1)
        span = spans_list[0]

        # Check version and name in span's instrumentation info
        self.assertEqualSpanInstrumentationInfo(
            span, opentelemetry.instrumentation.mysql
        )

        # check that no spans are generated after uninstrumen
        MySQLInstrumentor().uninstrument()

        connect_and_execute_query()

        spans_list = self.memory_exporter.get_finished_spans()
        self.assertEqual(len(spans_list), 1)

    @patch("mysql.connector.connect", new=mock_connect)
    def test_custom_tracer_provider(self):
        resource = resources.Resource.create({})
        result = self.create_tracer_provider(resource=resource)
        tracer_provider, exporter = result

        MySQLInstrumentor().instrument(tracer_provider=tracer_provider)
        connect_and_execute_query()

        span_list = exporter.get_finished_spans()
        self.assertEqual(len(span_list), 1)
        span = span_list[0]

        self.assertIs(span.resource, resource)

    @patch("mysql.connector.connect", new=mock_connect)
    # pylint: disable=unused-argument
    def test_instrument_connection(self):
        cnx, query = connect_and_execute_query()

        spans_list = self.memory_exporter.get_finished_spans()
        self.assertEqual(len(spans_list), 0)

        cnx = MySQLInstrumentor().instrument_connection(cnx)
        cursor = cnx.cursor()
        cursor.execute(query)

        spans_list = self.memory_exporter.get_finished_spans()
        self.assertEqual(len(spans_list), 1)

    @patch("mysql.connector.connect", new=mock_connect)
    def test_instrument_connection_no_op_tracer_provider(self):
        tracer_provider = trace_api.NoOpTracerProvider()
        MySQLInstrumentor().instrument(tracer_provider=tracer_provider)
        connect_and_execute_query()

        spans_list = self.memory_exporter.get_finished_spans()
        self.assertEqual(len(spans_list), 0)

    @patch("mysql.connector.connect", new=mock_connect)
    # pylint: disable=unused-argument
    def test_uninstrument_connection(self):
        MySQLInstrumentor().instrument()
        cnx, query = connect_and_execute_query()

        spans_list = self.memory_exporter.get_finished_spans()
        self.assertEqual(len(spans_list), 1)

        cnx = MySQLInstrumentor().uninstrument_connection(cnx)
        cursor = cnx.cursor()
        cursor.execute(query)

        spans_list = self.memory_exporter.get_finished_spans()
        self.assertEqual(len(spans_list), 1)
