import unittest
import pandas as pd
from scripts.pipeline import mask_sensitive_data

class TestPipeline(unittest.TestCase):
    def test_pii_masking(self):
        # Create a tiny fake dataset
        data = {'name': ['Test User'], 'email': ['secret@example.com']}
        df = pd.DataFrame(data)
        
        # Run the masking function
        masked_df = mask_sensitive_data(df)
        
        # Verify the email is actually masked
        email_result = masked_df['email'].iloc[0]
        self.assertIn("****", email_result)
        self.assertNotIn("secret@example", email_result)
        print(f"Test Passed: {email_result}")

if __name__ == '__main__':
    unittest.main()
