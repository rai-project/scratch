#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `carml_python_client` package."""


import unittest
from click.testing import CliRunner

from carml_python_client import carml_python_client
from carml_python_client import cli


class TestCarml_python_client(unittest.TestCase):
    """Tests for `carml_python_client` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'carml_python_client.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
