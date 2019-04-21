#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `djangocms_simple_news` package."""


import unittest
from click.testing import CliRunner

from djangocms_simple_news import djangocms_simple_news
from djangocms_simple_news import cli


class TestDjangocms_simple_news(unittest.TestCase):
    """Tests for `djangocms_simple_news` package."""

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
        assert 'djangocms_simple_news.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
