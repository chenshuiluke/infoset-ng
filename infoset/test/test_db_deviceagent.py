#!/usr/bin/env python3
"""Test the db_deviceagent library in the infoset.db module."""

import unittest
import os
import sys

# Try to create a working PYTHONPATH
_TEST_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
_LIB_DIRECTORY = os.path.abspath(os.path.join(_TEST_DIRECTORY, os.pardir))
_ROOT_DIRECTORY = os.path.abspath(os.path.join(_LIB_DIRECTORY, os.pardir))
if _TEST_DIRECTORY.endswith('/infoset/test') is True:
    sys.path.append(_ROOT_DIRECTORY)
else:
    print(
        'This script is not installed in the "infoset-ng/bin" directory. '
        'Please fix.')
    sys.exit(2)

# Import infoset stuff
from infoset.db import db_deviceagent
from infoset.test import unittest_setup_db
from infoset.test import unittest_setup


class TestGetDeviceAgent(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    # Setup database based on the config
    database = unittest_setup_db.TestData()

    # Define expected values
    expected = {}
    expected['idx_deviceagent'] = database.idx_deviceagent()
    expected['idx_device'] = database.idx_device()
    expected['idx_agent'] = database.idx_agent()
    expected['last_timestamp'] = database.last_timestamp()
    expected['enabled'] = True
    expected['exists'] = True

    # Create device object
    good_device = db_deviceagent.GetDeviceAgent(
        expected['idx_device'], expected['idx_agent'])

    def test___init__(self):
        """Testing method __init__."""
        # Test with non existent IDXDevice
        record = db_deviceagent.GetDeviceAgent('bogus', 'bogus')
        self.assertEqual(record.exists(), False)
        self.assertEqual(record.enabled(), None)
        self.assertEqual(record.idx_agent(), None)
        self.assertEqual(record.idx_device(), None)
        self.assertEqual(record.idx_deviceagent(), None)
        self.assertEqual(record.last_timestamp(), None)

    def test_exists(self):
        """Testing method exists."""
        # Testing with known good value
        result = self.good_device.exists()
        self.assertEqual(result, True)

        # Test with known bad value
        expected = db_deviceagent.GetDeviceAgent(None, None)
        result = expected.exists()
        self.assertEqual(result, False)

    def test_enabled(self):
        """Testing method enabled."""
        # Testing with known good value
        result = self.good_device.enabled()
        self.assertEqual(result, True)

    def test_last_timestamp(self):
        """Testing method last_timestamp."""
        # Testing with known good value
        result = self.good_device.last_timestamp()
        self.assertEqual(result, self.expected['last_timestamp'])

    def test_idx_deviceagent(self):
        """Testing method idx_deviceagent."""
        # Testing with known good value
        result = self.good_device.idx_deviceagent()
        self.assertEqual(result, self.expected['idx_deviceagent'])

    def test_idx_agent(self):
        """Testing method idx_agent."""
        # Testing with known good value
        result = self.good_device.idx_agent()
        self.assertEqual(result, self.expected['idx_agent'])

    def test_idx_device(self):
        """Testing method idx_device."""
        # Testing with known good value
        result = self.good_device.idx_device()
        self.assertEqual(result, self.expected['idx_device'])

    def test_everything(self):
        """Testing method everything."""
        # Testing with known good value
        result = self.good_device.everything()
        for key, _ in self.expected.items():
            self.assertEqual(result[key], self.expected[key])

        # Test the number and names of keys
        keys = [
            'last_timestamp', 'idx_deviceagent',
            'idx_agent', 'idx_device', 'enabled', 'exists']
        self.assertEqual(len(result), len(keys))
        for key in keys:
            self.assertEqual(key in result, True)


class TestGetIDXDeviceAgent(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    # Setup database based on the config
    database = unittest_setup_db.TestData()

    # Define expected values
    expected = {}
    expected['idx_deviceagent'] = database.idx_deviceagent()
    expected['idx_device'] = database.idx_device()
    expected['idx_agent'] = database.idx_agent()
    expected['last_timestamp'] = database.last_timestamp()
    expected['enabled'] = True
    expected['exists'] = True

    # Create device object
    good_device = db_deviceagent.GetIDXDeviceAgent(
        expected['idx_deviceagent'])

    def test___init__(self):
        """Testing method __init__."""
        # Test with non existent IDXDevice
        record = db_deviceagent.GetIDXDeviceAgent('bogus')
        self.assertEqual(record.exists(), False)
        self.assertEqual(record.enabled(), None)
        self.assertEqual(record.idx_agent(), None)
        self.assertEqual(record.idx_device(), None)
        self.assertEqual(record.idx_deviceagent(), None)
        self.assertEqual(record.last_timestamp(), None)

        record = db_deviceagent.GetIDXDeviceAgent(-1)
        self.assertEqual(record.exists(), False)
        self.assertEqual(record.enabled(), None)
        self.assertEqual(record.idx_agent(), None)
        self.assertEqual(record.idx_device(), None)
        self.assertEqual(record.idx_deviceagent(), None)
        self.assertEqual(record.last_timestamp(), None)

    def test_exists(self):
        """Testing method exists."""
        # Testing with known good value
        result = self.good_device.exists()
        self.assertEqual(result, True)

        # Test with known bad value
        expected = db_deviceagent.GetIDXDeviceAgent(None)
        result = expected.exists()
        self.assertEqual(result, False)

    def test_enabled(self):
        """Testing method enabled."""
        # Testing with known good value
        result = self.good_device.enabled()
        self.assertEqual(result, True)

    def test_last_timestamp(self):
        """Testing method last_timestamp."""
        # Testing with known good value
        result = self.good_device.last_timestamp()
        self.assertEqual(result, self.expected['last_timestamp'])

    def test_idx_deviceagent(self):
        """Testing method idx_deviceagent."""
        # Testing with known good value
        result = self.good_device.idx_deviceagent()
        self.assertEqual(result, self.expected['idx_deviceagent'])

    def test_idx_agent(self):
        """Testing method idx_agent."""
        # Testing with known good value
        result = self.good_device.idx_agent()
        self.assertEqual(result, self.expected['idx_agent'])

    def test_idx_device(self):
        """Testing method idx_device."""
        # Testing with known good value
        result = self.good_device.idx_device()
        self.assertEqual(result, self.expected['idx_device'])

    def test_everything(self):
        """Testing method everything."""
        # Testing with known good value
        result = self.good_device.everything()
        for key, _ in self.expected.items():
            self.assertEqual(result[key], self.expected[key])

        # Test the number and names of keys
        keys = [
            'last_timestamp', 'idx_deviceagent',
            'idx_agent', 'idx_device', 'enabled', 'exists']
        self.assertEqual(len(result), len(keys))
        for key in keys:
            self.assertEqual(key in result, True)


class TestFunctions(unittest.TestCase):
    """Checks all functions."""

    #########################################################################
    # General object setup
    #########################################################################

    # Setup database based on the config
    database = unittest_setup_db.TestData()

    # Define expected values
    expected = {}
    expected['idx_deviceagent'] = database.idx_deviceagent()
    expected['idx_device'] = database.idx_device()
    expected['idx_agent'] = database.idx_agent()
    expected['last_timestamp'] = database.timestamp()
    expected['enabled'] = True
    expected['exists'] = True

    def test_device_agent_exists(self):
        """Testing function device_agent_exists."""
        # Testing with known good value
        result = db_deviceagent.device_agent_exists(
            self.expected['idx_device'], self.expected['idx_agent'])
        self.assertEqual(result, True)

        # Testing with known good value
        result = db_deviceagent.device_agent_exists(None, None)
        self.assertEqual(result, False)

    def test_all_device_indices(self):
        """Testing function all_device_indices."""
        # Testing with known good value
        result = db_deviceagent.all_device_indices()
        self.assertEqual(result, [1])

    def test_device_indices(self):
        """Testing function device_indices."""
        # Testing with known good value
        result = db_deviceagent.device_indices(self.expected['idx_agent'])
        self.assertEqual(result, [1])

    def test_agent_indices(self):
        """Testing function agent_indices."""
        # Testing with known good value
        result = db_deviceagent.agent_indices(self.expected['idx_device'])
        self.assertEqual(result, [1])

    def test_get_all_device_agents(self):
        """Testing function get_all_device_agents."""
        results = db_deviceagent.get_all_device_agents()

        # There should only be one item in the result list
        self.assertEqual(len(results), 1)

        # Verify values in only result item
        for result in results:
            for key, _ in result.items():
                self.assertEqual(result[key], self.expected[key])


if __name__ == '__main__':
    # Test the environment variables
    unittest_setup.ready()

    # Do the unit test
    unittest.main()
