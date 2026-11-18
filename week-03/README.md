# Payment Totals — Python Assignment

This project reads `module-02/data/raw_sales.txt` and summarizes sales by payment method, excluding cancelled orders.

`my_tools.py` provides `clean_amount()`, `taka()`, `read_lines()`, and `calculate_sales()` for cleaning, formatting, loading, and totaling sales.

`payment_totals.py` imports these functions and displays transaction counts, totals for bKash, Nagad, Card, Rocket, and Cash on Delivery, plus the grand total.

Run from the project root with `python3 module-03/assignments/payment_totals.py` 
(keep `my_tools.py` in the same assignments folder).
