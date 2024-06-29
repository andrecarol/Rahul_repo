# src/Function.py
import json
import logging
from typing import Any, Dict
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(service="cloudformation_demo")

def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> None:
    """
    This method is called for every Lambda invocation. This method takes in an SQS event object and can be used 
    to respond to SQS messages.
    """
    for record in event['Records']:
        process_message(record, context)

def process_message(message: Dict[str, Any], context: LambdaContext) -> None:
    """
    Process a single SQS message.
    """
    logger.info(f"Processed message {message['body']}")
    
    # Simulate some processing work
    # TODO: Replace this with actual processing logic
    logger.info("Processing the message...")
    logger.info("Async task completed")
