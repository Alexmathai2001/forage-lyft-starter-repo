class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    
    def needs_service(self, tire_wear):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced() or self.tires_should_be_serviced(tire_wear):
            return True
        return False
    
    def battery_should_be_serviced(self):
        # Existing implementation
    
    def engine_should_be_serviced(self):
        # Existing implementation
    
    def tires_should_be_serviced(self, tire_wear):
        # Check tire servicing criteria based on tire wear array
        if isinstance(tire_wear, list):
            tire_type = self.get_tire_type()  # Assuming a method to get the tire type (Carrigan or Octoprime)
            if tire_type == "Carrigan":
                if any(wear >= 0.9 for wear in tire_wear):
                    return True
            elif tire_type == "Octoprime":
                if sum(tire_wear) >= 3:
                    return True
        return False
class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        return False
    
    def battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = self.last_service_date
        battery_service_interval = 3  # Changed from 2 to 3 years
        if (today - last_service_date).days >= battery_service_interval * 365:
            return True
        return False

class TestCalliope(unittest.TestCase):
    def setUp(self):
        self.calliope = Calliope(date(2020, 6, 1), 50000, 40000)  # Last service date two years ago
    
    def test_needs_service_battery_should_be_serviced(self):
        # Last service date is more than 3 years ago
        self.assertTrue(self.calliope.needs_service())
    
    def test_battery_should_be_serviced(self):
        self.calliope.last_service_date = date.today() - timedelta(days=3 * 365)  # Set last service date to 3 years ago
        self.assertTrue(self.calliope.battery_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
