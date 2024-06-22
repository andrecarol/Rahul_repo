import unittest
from unittest.mock import Mock
from typing import Dict, Any

from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def test_sqs_event_lambda_function(self):
        # Create a mock SQS event
        sqs_event: Dict[str, Any] = {
            "Records": [
                {
                    "messageId": "1a2b3c4d-5678-90ab-cdef-EXAMPLE11111",
                    "receiptHandle": "MessageReceiptHandle",
                    "body": "foobar",
                    "attributes": {
                        "ApproximateReceiveCount": "1",
                        "SentTimestamp": "1523232000000",
                        "SenderId": "123456789012",
                        "ApproximateFirstReceiveTimestamp": "1523232000001"
                    },
                    "messageAttributes": {},
                    "md5OfBody": "7b270e59b47ff90a553787216d55d91d",
                    "eventSource": "aws:sqs",
                    "eventSourceARN": "arn:aws:sqs:us-west-2:123456789012:MyQueue",
                    "awsRegion": "eu-west-1"
                }
            ]
        }

        # Create a mock context with a logger
        mock_context = Mock()
        mock_context.get_remaining_time_in_millis = Mock(return_value=10000)
        mock_context.aws_request_id = "test_request_id"
        
        # Create a string buffer to capture log output
        log_output = []
        mock_context.logger = Mock()
        mock_context.logger.info = lambda message: log_output.append(message)

        # Call the lambda handler
        lambda_handler(sqs_event, mock_context)

        # Verify the log output contains the expected message
        self.assertIn("Processed message foobar", log_output)

if __name__ == '__main__':
    unittest.main()
