![Invento Logo](assets/light_logo_color.svg#gh-dark-mode-only)
![Invento Logo](assets/dark_logo_color.svg#gh-light-mode-only)

## :globe_with_meridians: Description

Inventory management system that tracks sales performance and inventory changes.
A project for Discrete Structures II.

-----------------------------------------------------------------

## :abacus: Features

### Core
- [x] Login system
- [x] Register user account
- [x] Administrator account
- [x] Add, modify, delete inventory items
- [x] Evaluate and modify current stock
- [x] Calculate total sales per day
- [x] Show graph of sales per day

### Extras
- Generate account photo
- Theme changes
- Widget scaling


-----------------------------------------------------------------

## :clipboard: Setup Guide

### Prerequisites

- Requires Python 3.10.x
- Install `customtkinter`, `pillow`, and `matplotlib` via `pip install`

### Execution

1. Clone the repository to your machine and change directory to cloned project.

    ```sh
    git clone https://github.com/steguiosaur/invento.git && cd ./invento
    ```

2. Execute `Main.py` to run the application.

    ```sh
    python Main.py
    ```

    > In case `dependencies.py` failed to execute, manually install the required dependencies.

    ```sh
    pip install -r requirements.txt
    ```

    > If failed, try upgrading `pip` and its packages.
    
    ```sh
    pip install --upgrade pip customtkinter Pillow matplotlib
    ```

### Build Compilation
