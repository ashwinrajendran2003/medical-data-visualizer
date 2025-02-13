import unittest
import medical_data_visualizer

class TestMedicalDataVisualizer(unittest.TestCase):
    def test_cat_plot(self):
        self.assertIsNotNone(medical_data_visualizer.draw_cat_plot())

    def test_heat_map(self):
        self.assertIsNotNone(medical_data_visualizer.draw_heat_map())

if __name__ == "__main__":
    unittest.main()
