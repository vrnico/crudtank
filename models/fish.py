"""
Fish Model - Handles data operations for Fish entities
This model demonstrates CRUD operations with JSON file storage.
"""

import json
import os
import uuid
from datetime import datetime

# Path to the JSON data file
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'fish.json')


class Fish:
    """
    Fish Model Class

    Attributes:
        id (str): Unique identifier for the fish
        name (str): Display name of the fish
        image_url (str): URL to the fish image
        personality (str): 'fast', 'medium', or 'slow' - affects swim speed
        description (str): A brief description of the fish
        created_at (str): Timestamp when the fish was created
    """

    def __init__(self, name, image_url, personality='medium', description='', id=None, created_at=None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.image_url = image_url
        self.personality = personality  # 'fast', 'medium', 'slow'
        self.description = description
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        """Convert Fish object to dictionary for JSON storage."""
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url,
            'personality': self.personality,
            'description': self.description,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Fish object from a dictionary."""
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            image_url=data.get('image_url'),
            personality=data.get('personality', 'medium'),
            description=data.get('description', ''),
            created_at=data.get('created_at')
        )


# =============================================================================
# CRUD OPERATIONS - These are the core database operations
# =============================================================================

def _load_data():
    """Load all fish data from the JSON file."""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _save_data(data):
    """Save all fish data to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


# -----------------------------------------------------------------------------
# CREATE - Add a new fish to the database
# -----------------------------------------------------------------------------
def create_fish(name, image_url, personality='medium', description=''):
    """
    CREATE Operation: Add a new fish to the tank.

    Args:
        name (str): The fish's display name
        image_url (str): URL to the fish's image
        personality (str): Swimming speed - 'fast', 'medium', or 'slow'
        description (str): Optional description of the fish

    Returns:
        Fish: The newly created fish object
    """
    # Create a new Fish instance
    fish = Fish(
        name=name,
        image_url=image_url,
        personality=personality,
        description=description
    )

    # Load existing data, add new fish, and save
    data = _load_data()
    data.append(fish.to_dict())
    _save_data(data)

    return fish


# -----------------------------------------------------------------------------
# READ - Retrieve fish from the database
# -----------------------------------------------------------------------------
def get_all_fish():
    """
    READ Operation: Get all fish from the tank.

    Returns:
        list[Fish]: List of all fish objects
    """
    data = _load_data()
    return [Fish.from_dict(item) for item in data]


def get_fish_by_id(fish_id):
    """
    READ Operation: Get a specific fish by its ID.

    Args:
        fish_id (str): The unique ID of the fish

    Returns:
        Fish or None: The fish object if found, None otherwise
    """
    data = _load_data()
    for item in data:
        if item['id'] == fish_id:
            return Fish.from_dict(item)
    return None


# -----------------------------------------------------------------------------
# UPDATE - Modify an existing fish in the database
# -----------------------------------------------------------------------------
def update_fish(fish_id, name=None, image_url=None, personality=None, description=None):
    """
    UPDATE Operation: Modify an existing fish's details.

    Args:
        fish_id (str): The unique ID of the fish to update
        name (str, optional): New name for the fish
        image_url (str, optional): New image URL
        personality (str, optional): New personality type
        description (str, optional): New description

    Returns:
        Fish or None: The updated fish object if found, None otherwise
    """
    data = _load_data()

    for i, item in enumerate(data):
        if item['id'] == fish_id:
            # Update only the fields that were provided
            if name is not None:
                data[i]['name'] = name
            if image_url is not None:
                data[i]['image_url'] = image_url
            if personality is not None:
                data[i]['personality'] = personality
            if description is not None:
                data[i]['description'] = description

            _save_data(data)
            return Fish.from_dict(data[i])

    return None


# -----------------------------------------------------------------------------
# DELETE - Remove a fish from the database
# -----------------------------------------------------------------------------
def delete_fish(fish_id):
    """
    DELETE Operation: Remove a fish from the tank.

    Args:
        fish_id (str): The unique ID of the fish to delete

    Returns:
        bool: True if the fish was deleted, False if not found
    """
    data = _load_data()
    original_length = len(data)

    # Filter out the fish with the matching ID
    data = [item for item in data if item['id'] != fish_id]

    if len(data) < original_length:
        _save_data(data)
        return True

    return False
