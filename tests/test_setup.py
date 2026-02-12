import sys
import os

# Fix path so we can import from 'utils'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logger import get_logger
import numpy as np
import pandas as pd
import spacy

# Start Logger
logger = get_logger("TEST_SETUP")

def check_environment():
    logger.info("🚀 Starting Environment Check...")

    # Check Libraries
    try:
        logger.info(f"✅ Numpy Version: {np.__version__}")
        logger.info(f"✅ Pandas Version: {pd.__version__}")
        logger.info("✅ Spacy imported successfully.")
    except ImportError as e:
        logger.error(f"❌ Library Missing: {e}")

    # Check Folders
    folders = ['data', 'ats_engine', 'interview_ai', 'utils']
    for f in folders:
        if os.path.exists(f):
            logger.info(f"✅ Folder found: {f}")
        else:
            logger.error(f"❌ Folder Missing: {f}")

    logger.info("🎉 Zecpath AI Setup Complete!")

if __name__ == "__main__":
    check_environment()