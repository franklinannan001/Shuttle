# Transit Fare Calculator

A lightweight Python command-line application that calculates travel fares in Kenyan Shillings (KSH) based on trip distance.

## Features

* **Automated Trip Categorization:** Classifies journeys into *Short Hop*, *Standard*, or *Long Haul* tiers based on distance.
* **Tiered Pricing Calculation:** Applies flat-rate or per-kilometer pricing rules depending on the trip category.
* **Input Validation & Formatting:** Automatically formats passenger names and safely handles invalid or non-positive distance inputs without crashing.

## Pricing Tiers

| Distance (km) | Trip Category | Fare Calculation |
| :--- | :--- | :--- |
| `0 < distance <= 3` | **Short Hop** | Flat rate of **KSH 20** |
| `3 < distance <= 10` | **Standard** | **KSH 15** per km |
| `distance > 10` | **Long Haul** | **KSH 10** per km |

## Prerequisites

* Python 3.6 or higher

## Getting Started

1. **Clone the repository** (or save the script locally as `fare_calculator.py`):
   ```bash
   git clone https://github.com
   cd your-repo-name
   ```

2. **Run the script:**
   ```bash
   python fare_calculator.py
   ```

## Usage Example

```text
What is your name: john doe
Distance travelling(km): 7.5
John Doe, your Standard trip of 7.5km costs KSH 112.5.
```

> **Note:** If you enter a non-numeric value or a distance less than or equal to `0`, the program exits quietly without displaying a fare.

## Code Structure

* `main()`: Prompts the user for their name and distance, validates input, and prints the formatted fare summary.
* `get_category(d)`: Evaluates the distance `d` and returns the corresponding category string (or `None` if `d <= 0`).
* `calculate_fare(d, c)`: Computes and returns the total fare based on the distance `d` and category `c`.
