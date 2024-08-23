import unittest
from unittest.mock import Mock
from typing import Dict, Any
#import src
#from cloudformation_demo.src.la_function import lambda_handler

#from src import la_function
from la_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def test_sqs_event_lambda_function(self):
        # Create a mock SQS event
        sqs_event: Dict[str, Any] = {
            "Records": [
                {
                    "messageId": "1a2b3c4d-5678-90ab-cdef-EXAMPLE11111",
                    "receiptHandle": "MessageReceiptHandle",
                    "body": "the message...foobar",
                    "attributes": {
                        "ApproximateReceiveCount": "1",
                        "SentTimestamp": "1523232000000",
                        "SenderId": "123456789012",
                        "ApproximateFirstReceiveTimestamp": "1523232000001"
                    },
                    "messageAttributes": {},
                    "md5OfBody": "7b270e59b47ff90a553787216d55d91d",
                    "eventSource": "aws:sqs",
                    "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:MyQueue",
                    "awsRegion": "us-east-1"
                }
            ]
        }

        # Create a mock context with a logger
        mock_context = Mock()
        mock_context.get_remaining_time_in_millis = Mock(return_value=10000)
        mock_context.aws_request_id = "test_request_id"

        # Set up a logger to capture the log output
        import logging
        import io
        log_stream = io.StringIO()
        logging.basicConfig(stream=log_stream, level=logging.INFO)

        # Call the lambda handler
        #la_function.lambda_handler(sqs_event, mock_context)
        lambda_handler(sqs_event, mock_context)
        # Capture and print the log output
        log_contents = log_stream.getvalue()
        #print(log_contents)  # Added print statement for demonstration

        # Verify the log output contains the expected message
        self.assertIn("Processing the message...the message...foobar", log_contents)

        print("Tout est OK")


if __name__ == '__main__':
    unittest.main()
