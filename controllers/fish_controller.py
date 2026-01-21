"""
Fish Controller - Handles HTTP requests and responses for Fish operations
This controller demonstrates how to connect routes to model operations.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.fish import (
    create_fish,
    get_all_fish,
    get_fish_by_id,
    update_fish,
    delete_fish
)

# Create a Blueprint for fish-related routes
fish_bp = Blueprint('fish', __name__)


# =============================================================================
# CONTROLLER ACTIONS - Handle HTTP requests and call Model methods
# =============================================================================

# -----------------------------------------------------------------------------
# READ (Index) - Display the fish tank with all fish
# Route: GET /
# -----------------------------------------------------------------------------
@fish_bp.route('/')
def tank():
    """
    Controller Action: Display the fish tank (READ all fish)

    This action:
    1. Calls the Model's get_all_fish() to retrieve data
    2. Passes the data to the View (tank.html template)
    3. Returns the rendered HTML response
    """
    # Call the Model to get all fish
    fish_list = get_all_fish()

    # Render the View with the data
    return render_template('tank.html', fish_list=fish_list)


# -----------------------------------------------------------------------------
# CREATE - Show form and handle new fish creation
# Routes: GET /fish/new (show form), POST /fish/new (process form)
# -----------------------------------------------------------------------------
@fish_bp.route('/fish/new', methods=['GET', 'POST'])
def new_fish():
    """
    Controller Action: Create a new fish

    GET: Display the create form
    POST: Process the form data and create the fish
    """
    if request.method == 'POST':
        # Extract data from the form submission
        name = request.form.get('name')
        image_url = request.form.get('image_url')
        personality = request.form.get('personality', 'medium')
        description = request.form.get('description', '')
        color = request.form.get('color', 'none')

        # Validate required fields
        if not name or not image_url:
            flash('Name and Image URL are required!', 'error')
            return render_template('create.html')

        # Call the Model to create the fish
        fish = create_fish(
            name=name,
            image_url=image_url,
            personality=personality,
            description=description,
            color=color
        )

        flash(f'Fish "{fish.name}" has been added to the tank!', 'success')
        return redirect(url_for('fish.tank'))

    # GET request - just show the form
    return render_template('create.html')


# -----------------------------------------------------------------------------
# READ (Show) - Display a single fish's details
# Route: GET /fish/<id>
# -----------------------------------------------------------------------------
@fish_bp.route('/fish/<fish_id>')
def show_fish(fish_id):
    """
    Controller Action: Display a single fish's details (READ one)

    This action:
    1. Receives the fish_id from the URL
    2. Calls the Model's get_fish_by_id() to retrieve the fish
    3. Passes the fish to the View (detail.html template)
    """
    # Call the Model to get the specific fish
    fish = get_fish_by_id(fish_id)

    if not fish:
        flash('Fish not found!', 'error')
        return redirect(url_for('fish.tank'))

    # Render the View with the fish data
    return render_template('detail.html', fish=fish)


# -----------------------------------------------------------------------------
# UPDATE - Show edit form and handle fish updates
# Routes: GET /fish/<id>/edit (show form), POST /fish/<id>/edit (process form)
# -----------------------------------------------------------------------------
@fish_bp.route('/fish/<fish_id>/edit', methods=['GET', 'POST'])
def edit_fish(fish_id):
    """
    Controller Action: Update an existing fish

    GET: Display the edit form with current fish data
    POST: Process the form data and update the fish
    """
    # First, get the current fish data
    fish = get_fish_by_id(fish_id)

    if not fish:
        flash('Fish not found!', 'error')
        return redirect(url_for('fish.tank'))

    if request.method == 'POST':
        # Extract updated data from the form
        name = request.form.get('name')
        image_url = request.form.get('image_url')
        personality = request.form.get('personality')
        description = request.form.get('description')
        color = request.form.get('color')

        # Call the Model to update the fish
        updated_fish = update_fish(
            fish_id=fish_id,
            name=name,
            image_url=image_url,
            personality=personality,
            description=description,
            color=color
        )

        if updated_fish:
            flash(f'Fish "{updated_fish.name}" has been updated!', 'success')
            return redirect(url_for('fish.show_fish', fish_id=fish_id))
        else:
            flash('Failed to update fish.', 'error')

    # GET request - show the edit form with current data
    return render_template('edit.html', fish=fish)


# -----------------------------------------------------------------------------
# DELETE - Show confirmation and handle fish deletion
# Routes: GET /fish/<id>/delete (show confirm), POST /fish/<id>/delete (delete)
# -----------------------------------------------------------------------------
@fish_bp.route('/fish/<fish_id>/delete', methods=['GET', 'POST'])
def remove_fish(fish_id):
    """
    Controller Action: Delete a fish

    GET: Display the delete confirmation page
    POST: Process the deletion
    """
    # Get the fish to show its details on the confirmation page
    fish = get_fish_by_id(fish_id)

    if not fish:
        flash('Fish not found!', 'error')
        return redirect(url_for('fish.tank'))

    if request.method == 'POST':
        # Call the Model to delete the fish
        fish_name = fish.name
        success = delete_fish(fish_id)

        if success:
            flash(f'Fish "{fish_name}" has been removed from the tank.', 'success')
            return redirect(url_for('fish.tank'))
        else:
            flash('Failed to delete fish.', 'error')

    # GET request - show the delete confirmation page
    return render_template('delete.html', fish=fish)
