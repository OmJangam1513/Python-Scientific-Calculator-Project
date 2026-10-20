# Python Scientific Calculator

A desktop scientific calculator built with Python, Tkinter, and the built-in `math` module. It provides a graphical interface for performing arithmetic calculations and scientific mathematical operations.

## Features

- **Basic Arithmetic:** Addition, subtraction, multiplication, and division.
- **Scientific Functions:** Square root, sine, cosine, tangent, and inverse trigonometric functions.
- **Hyperbolic Functions:** `sinh`, `cosh`, and `tanh`.
- **Logarithmic Functions:** Natural logarithm (`log`) and base-10 logarithm (`log10`).
- **Mathematical Constants:** Support for π and Euler's number (e).
- **Expression Evaluation:** Evaluate mathematical expressions using parentheses and supported functions.
- **Editing Controls:** Clear the display or delete the last entered character.
- **Error Handling:** Display an error message when a calculation fails.
- **Graphical Interface:** Tkinter-based interface with a calculator display and buttons.

## Technologies Used

- **Python** — Application logic and calculations.
- **Tkinter** — Graphical user interface.
- **math** — Mathematical functions and constants.
- **eval()** — Evaluation of mathematical expressions with restricted built-ins and an explicitly defined set of available mathematical functions.

## Requirements

- Python 3.x
- Tkinter (usually included with standard Python installations)

No third-party Python packages are required.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/OmJangam1513/Python-Scientific-Calculator-Project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Python-Scientific-Calculator-Project
   ```

3. Run the application:

   ```bash
   python main.py
   ```

   Replace `main.py` with the actual Python filename if it differs.

## Implementation

The application uses a `ScientificCalculator` class to manage the calculator window, display, button creation, and mathematical operations. Tkinter's grid layout organizes the buttons, while callback functions handle user input and calculations.

The `math` module supplies scientific functions and constants. The expression evaluator restricts built-ins and exposes only a selected set of mathematical names.

## Future Improvements

- Implement and verify the natural logarithm (`ln`) button.
- Add keyboard input support.
- Improve input validation and calculation error messages.
- Add additional scientific operations and memory functions.

## License

Specify a license if you intend to distribute or reuse this project publicly.
