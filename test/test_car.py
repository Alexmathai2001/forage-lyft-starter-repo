import unittest
from datetime import date
from capulet import Calliope, Glissade

class TestCalliope(unittest.TestCase):
    def setUp(self):
        self.calliope = Calliope(date(2022, 6, 1), 50000, 40000)
    
    def test_needs_service_battery_should_be_serviced(self):
        # Last service date is more than 3 days ago
        self.assertTrue(self.calliope.needs_service())
    
    def test_needs_service_engine_should_be_serviced(self):
        # Current mileage minus last service mileage is more than 30000
        self.assertTrue(self.calliope.needs_service())
    
    def test_needs_service_no_service_needed(self):
        self.calliope.last_service_date = date.today()  # Set last service date to today
        self.calliope.current_mileage = 52000  # Set current mileage
        self.assertFalse(self.calliope.needs_service())
    
    def test_battery_should_be_serviced(self):
        self.calliope.last_service_date = date.today()  # Set last service date to today
        self.assertTrue(self.calliope.battery_should_be_serviced())
    
    def test_battery_should_not_be_serviced(self):
        self.assertFalse(self.calliope.battery_should_be_serviced())
    
    def test_engine_should_be_serviced(self):
        self.assertTrue(self.calliope.engine_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self):
        self.calliope.last_service_mileage = 55000  # Set last service mileage
        self.assertFalse(self.calliope.engine_should_be_serviced())

class TestGlissade(unittest.TestCase):
    def setUp(self):
        self.glissade = Glissade(date(2022, 6, 1), 70000, 60000)
    
    def test_needs_service_battery_should_be_serviced(self):
        # Last service date is more than 3 days ago
        self.assertTrue(self.glissade.needs_service())
    
    def test_needs_service_engine_should_be_serviced(self):
        # Current mileage minus last service mileage is more than 60000
        self.assertTrue(self.glissade.needs_service())
    
    def test_needs_service_no_service_needed(self):
        self.glissade.last_service_date = date.today()  # Set last service date to today
        self.glissade.current_mileage = 72000  # Set current mileage
        self.assertFalse(self.glissade.needs_service())
    
    def test_battery_should_be_serviced(self):
        self.glissade.last_service_date = date.today()  # Set last service date to today
        self.assertTrue(self.glissade.battery_should_be_serviced())
    
    def test_battery_should_not_be_serviced(self):
        self.assertFalse(self.glissade.battery_should_be_serviced())
    
    def test_engine_should_be_serviced(self):
        self.assertTrue(self.glissade.engine_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self):
        self.glissade.last_service_mileage = 65000  # Set last service mileage
        self.assertFalse(self.glissade.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
