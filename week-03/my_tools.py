
import os


# Function 1: Clean and convert amount
def clean_amount(text):
    """Remove ৳ and commas, then return a float."""
    amount = text.strip().replace("৳", "").replace(",", "")
    return float(amount)


# Function 2: Format amount as Bangladeshi Taka
def taka(amount):
    """Convert 1240.5 into '৳1240.50'."""
    return f"৳{amount:.2f}"


# Function 3: Read sales data from file
def read_lines(path):
    """Read file and return a list of lines."""
    with open(path, encoding="utf-8") as fh:
        return fh.read().strip().split("\n")


# Function 4: Calculate sales by payment method
def calculate_sales(lines):
    """Calculate total amount and count for each payment method."""

    bkash_total, bkash_count = 0.0, 0
    nagad_total, nagad_count = 0.0, 0
    card_total, card_count = 0.0, 0
    rocket_total, rocket_count = 0.0, 0
    cash_total, cash_count = 0.0, 0

    for raw in lines:
        if not raw.strip():
            continue

        parts = raw.split(";")

        amount = clean_amount(parts[5])
        payment = parts[6].strip().lower()
        status = parts[7].strip().lower()

        # Ignore cancelled orders
        if status == "cancelled":
            continue

        if payment == "bkash":
            bkash_total += amount
            bkash_count += 1

        elif payment == "nagad":
            nagad_total += amount
            nagad_count += 1

        elif payment == "card":
            card_total += amount
            card_count += 1

        elif payment == "rocket":
            rocket_total += amount
            rocket_count += 1

        else:
            cash_total += amount
            cash_count += 1

    grand_total = (
        bkash_total + nagad_total + card_total
        + rocket_total + cash_total
    )

    return (
        (bkash_count, bkash_total),
        (nagad_count, nagad_total),
        (card_count, card_total),
        (rocket_count, rocket_total),
        (cash_count, cash_total),
        grand_total
    )

def highest_sales_date(lines):
    """Find the date with the highest sales using if/elif."""

    date_07 = 0.0
    date_08 = 0.0
    date_09 = 0.0
    date_10 = 0.0
    date_11 = 0.0

    for raw in lines:
        if not raw.strip():
            continue

        parts = raw.split(";")

        date = parts[1].strip()
        amount = clean_amount(parts[5])
        status = parts[7].strip().lower()

        # Skip cancelled orders
        if status == "cancelled":
            continue

        # Calculate sales for each date
        if date == "2026-10-07":
            date_07 += amount

        elif date == "2026-10-08":
            date_08 += amount

        elif date == "2026-10-09":
            date_09 += amount

        elif date == "2026-10-10":
            date_10 += amount

        elif date == "2026-10-11":
            date_11 += amount

    # Find highest sales amount
    highest_amount = max(
        date_07, date_08, date_09, date_10, date_11
    )

    # Identify highest sales date
    if highest_amount == date_07:
        highest_date = "2026-10-07"

    elif highest_amount == date_08:
        highest_date = "2026-10-08"

    elif highest_amount == date_09:
        highest_date = "2026-10-09"

    elif highest_amount == date_10:
        highest_date = "2026-10-10"

    else:
        highest_date = "2026-10-11"

    return highest_date, highest_amount

# Main function
def main():

    # Build path relative to project root
    base_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    path = os.path.join(
        base_dir, "module-02", "data", "raw_sales.txt"
    )

    # Read file
    lines = read_lines(path)

    # Calculate results
    bkash, nagad, card, rocket, cash, grand = calculate_sales(lines)

    # All print statements are at the end
    print("Sales Summary")
    print("------------------------------")
    print(f"bkash            {bkash[0]}টা   {taka(bkash[1])}")
    print(f"nagad            {nagad[0]}টা   {taka(nagad[1])}")
    print(f"card             {card[0]}টা   {taka(card[1])}")
    print(f"rocket           {rocket[0]}টা   {taka(rocket[1])}")
    print(f"cash on delivery {cash[0]}টা   {taka(cash[1])}")
    print("------------------------------")
    print(f"সব মিলিয়ে: {taka(grand)}")


#if __name__ == "__main__":
#    main()

if __name__ == "__main__":
    print(clean_amount(" ৳ 1,240.50 "))    # 1240.5
    print(taka(1240.5))                     # ৳1240.50