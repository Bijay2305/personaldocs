import unittest
import requests
import cv2
import numpy as np
from io import BytesIO

class TestFlaskService(unittest.TestCase):
    def setUp(self):
        # Start the Flask app in a separate thread
        import threading
        from your_flask_app import app  # Import your Flask app
        
        self.server = threading.Thread(target=app.run, kwargs={'debug': False})
        self.server.start()

        # Wait for the server to start
        import time
        time.sleep(1)

    def tearDown(self):
        # Shutdown the Flask app after tests
        import requests
        requests.post('http://127.0.0.1:5000/shutdown')

    def test_upload_image(self):
        # Read a sample image
        image_path = 'path_to_your_sample_image.jpg'
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # Encode the image using cv2.imencode
        _, img_encoded = cv2.imencode('.jpg', cv2.imread(image_path))

        # Prepare form data with image
        files = {'file': ('test_image.jpg', BytesIO(image_data), 'image/jpeg')}

        # Make a POST request to the Flask service
        response = requests.post('http://127.0.0.1:5000/upload_image', files=files)

        # Check if the request was successful (HTTP status code 200)
        self.assertEqual(response.status_code, 200)

        # Optionally, check the response content
        # self.assertEqual(response.json(), {'message': 'Image received and processed successfully'})

if __name__ == '__main__':
    unittest.main()
