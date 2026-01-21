# CRUD Tank

A Flask MVC application for teaching CRUD operations using a fun fish tank metaphor.

![CRUD Tank Screenshot](https://i.imgur.com/qBGyCpM.png)

## About

**Created by Neek for [Multiverse School](https://www.multiverse.io/)**

This application is meant to be used for **educational purposes only**.

CRUD Tank helps students understand the fundamentals of:
- **C**reate - Adding new data to a database
- **R**ead - Retrieving and displaying data
- **U**pdate - Modifying existing data
- **D**elete - Removing data from a database

Each page displays the actual Python and HTML code for that CRUD operation, showing the Model, View, and Controller layers of the MVC pattern.

## Features

- Animated fish tank with swimming fish, bubbles, and decorations
- Add fish using any image URL (great for finding fish on Google Images!)
- Fish swim at different speeds based on their "personality" (fast/medium/slow)
- Click on any fish to view its details
- Each CRUD page shows the relevant code with tabbed navigation (Model/Controller/View)
- MVC flow explanations on every page

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/crud-tank.git
   cd crud-tank
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**

   Visit [http://localhost:5000](http://localhost:5000)

## Project Structure

```
crud-tank/
├── app.py                      # Flask application entry point
├── models/
│   └── fish.py                 # Fish model with CRUD operations
├── controllers/
│   └── fish_controller.py      # Routes and request handling
├── templates/
│   ├── base.html               # Base template with navigation
│   ├── tank.html               # READ - Fish tank view
│   ├── create.html             # CREATE - Add fish form
│   ├── detail.html             # READ - Single fish details
│   ├── edit.html               # UPDATE - Edit fish form
│   └── delete.html             # DELETE - Confirmation page
├── static/
│   ├── css/
│   │   └── style.css           # Tank styling & animations
│   └── js/
│       └── tank.js             # Fish swimming animation
└── data/
    └── fish.json               # JSON file storage
```

## How to Use

1. **View the Tank (READ)** - The homepage shows all fish swimming in the tank
2. **Add a Fish (CREATE)** - Click "Create - Add Fish" to add a new fish with an image URL
3. **View Fish Details (READ)** - Click on any fish in the tank to see its details
4. **Edit a Fish (UPDATE)** - From the detail page, click "Update Fish" to modify it
5. **Delete a Fish (DELETE)** - From the detail page, click "Delete Fish" to remove it

## Learning Objectives

Students will learn:
- The MVC (Model-View-Controller) architectural pattern
- How HTTP GET and POST requests work
- How forms submit data to a server
- How to perform CRUD operations on a data store
- Basic Flask routing and templating with Jinja2

## License

This project is for educational purposes only.

---

*Made with love for Multiverse School*
