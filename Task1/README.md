<!-- @format -->

# Expense Tracker

A comprehensive desktop application for managing personal finances. Track income and expenses, categorize transactions, set budget limits, and visualize your spending patterns with an intuitive Tkinter-based GUI.

## Features

- **Transaction Management**
    - Add, edit, and delete income/expense transactions
    - Elegant date picker with spinboxes (year, month, day)
    - Automatic leap year handling for date validation
    - Real-time form validation with user-friendly error messages

- **Advanced Filtering**
    - Filter by year, month, and category
    - Full-text search in transaction descriptions
    - Combined filter criteria for precise data views
    - Toggle "All Years" mode for year-independent filtering

- **Financial Summary**
    - Real-time calculation of total income, expenses, and net
    - Monthly financial overview
    - Dynamic updates on every transaction change

- **Visualizations**
    - Income and expense category pie charts
    - Separate chart panels for income and expense breakdowns

- **Budget Management**
    - Set spending limits per category
    - Track budget utilization across all categories
    - Visual feedback on budget status

- **Predefined Categories**
    - Food
    - Transport
    - Rent
    - Entertainment
    - Salary
    - Utilities
    - Shopping
    - Groceries
    - Bonus

- **Data Persistence**
    - Automatic CSV-based storage
    - Atomic writes for crash safety
    - Data loads on application startup
    - Auto-save on application exit

## Quick Start

### Requirements

- Python 3.7+
- tkinter (included with Python on most systems)

### Running the Application

```bash
python main.py
```

The application will:

- Load existing transactions from `data/transactions.csv`
- Open in fullscreen/maximized window mode
- Display the current financial summary
- Ready for immediate use

## Project Structure

```
Task1/
├── main.py                      # Application entry point and bootstrap
├── README.md                    # This file
├── data/
│   └── transactions.csv         # Transaction data storage
├── gui/
│   ├── main_window.py          # Main application window with Treeview display
│   └── add_window.py           # Modal window for adding/editing transactions
├── managers/
│   └── expense_manager.py       # Business logic for transaction operations
├── models/
│   ├── transaction.py          # Transaction data model
│   ├── category.py             # Category data model with color visualization
│   └── budget.py               # Budget management for spending limits
└── utils/
    └── data_handler.py          # CSV file I/O and data persistence
```

## Architecture

### Core Components

**ExpenseManager** (`managers/expense_manager.py`)

- Central business logic hub
- Manages transaction CRUD operations
- Handles filtering (year, month, category, keyword)
- Calculates financial summaries
- Manages category-specific budget limits

**MainWindow** (`gui/main_window.py`)

- Primary GUI displaying transaction table (Treeview)
- Financial summary display (income/expense/net)
- Filter controls (year spinbox, month dropdown, category dropdown, search field)
- Action buttons (Add, Edit, Delete, Budget settings)
- Auto-refresh on data changes

**TransactionFormWindow** (`gui/add_window.py`)

- Modal window for transaction entry/editing
- Date picker using spinboxes (year 2000-2030, month 1-12, dynamic day 1-31)
- Amount field with real-time numeric validation
- Category dropdown selection
- Description text input
- Transaction type selection (Income/Expense)
- Comprehensive form validation before saving

**Data Models**

- `Transaction`: Individual financial transaction with ID, date, amount, category, type, description
- `Category`: Expense category with hex color code for UI visualization
- `Budget`: Per-category and total monthly budget limits

**Data Persistence**

- `DataHandler`: CSV-based storage with atomic write pattern
- Validates all required fields
- Logs corrupted rows without blocking load
- Graceful handling of missing files

## Usage Guide

### Adding a Transaction

1. Click **"Add Transaction"** button
2. Set the date using spinbox controls:
    - Adjust year (2000-2030)
    - Select month (1-12)
    - Day range automatically adjusts for February leap years
3. Enter transaction amount (must be positive number)
4. Select category from dropdown
5. Enter optional description
6. Choose type: **Income** or **Expense**
7. Click **"Save"** to add transaction
8. Form closes automatically; transaction appears in table

### Filtering Transactions

- **By Year**: Check "All Years" to view all transactions, or uncheck and select specific year from spinbox
- **By Month**: Select month from dropdown (or "All Months" for no filter)
- **By Category**: Select category from dropdown (or "All Categories" for no filter)
- **By Description**: Type keywords in search field to find transactions by description

Filters combine automatically — set multiple filters to narrow results.

### Editing Transactions

1. Click on any transaction in the table
2. Click **"Edit"** button
3. Form opens with current values pre-filled
4. Modify any fields as needed
5. Click **"Save"** to apply changes
6. Transaction updates in table

### Deleting Transactions

1. Select a transaction in the table
2. Click **"Delete"** button
3. Confirm deletion in popup dialog
4. Transaction removed immediately

### Setting Budget Limits

1. Click **"Budget Settings"** button
2. Modal displays current budget configuration
3. Edit category-specific limits and total monthly limit
4. Changes apply immediately to financial calculations

## Data Storage

Transactions are stored in `data/transactions.csv` with the following columns:

| Column      | Description                          | Example        |
| ----------- | ------------------------------------ | -------------- |
| date        | ISO format date (YYYY-MM-DD)         | 2026-04-09     |
| amount      | Transaction amount (positive number) | 45.99          |
| category    | Transaction category                 | Food           |
| type        | Transaction type                     | income/expense |
| description | Transaction description              | Lunch at cafe  |

**Example CSV:**

```
date,amount,category,type,description
2026-04-09,45.99,Food,expense,Lunch at cafe
2026-04-08,2500.00,Salary,income,Monthly salary
2026-04-07,1200.00,Rent,expense,Monthly rent payment
```

## Files

- **main.py**: Entry point with `bootstrap_manager()` initialization and graceful shutdown handling
- **expense_manager.py**: Core business logic with transaction operations and financial calculations
- **transaction.py**: Transaction model with validation (amount ≥ 0, type must be income/expense)
- **category.py**: Category model with predefined categories and hex color codes
- **budget.py**: Budget model for tracking spending limits
- **data_handler.py**: CSV I/O with comprehensive error handling and logging
- **main_window.py**: Primary GUI with Treeview display, filters, and action buttons
- **add_window.py**: Modal form window with date picker and validation
