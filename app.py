
"""from Detection.logger import logging
from Detection.exception import AppException
import sys
try:
    a = 3/ "s"
except Exception as e:
    raise AppException(e,sys)"""
from Detection.pipeline.training_pipeline import TrainPipelines

print("Starting app.py") # Debugging output

obj = TrainPipelines()
print("Before running pipeline") # Debugging output
obj.run_pipeline() # Ensure parentheses are added
print("After running pipeline") # Debugging output
