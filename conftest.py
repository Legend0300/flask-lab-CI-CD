"""Pytest configuration to ensure app module is discoverable."""
import sys
from pathlib import Path

# Add project root to Python path so tests can import app
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
