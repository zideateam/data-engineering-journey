
import os
import my_tools

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
    lines = my_tools.read_lines(path)

    # Calculate results
    bkash, nagad, card, rocket, cash, grand = my_tools.calculate_sales(lines)

    # All print statements are at the end
    print("Sales Summary")
    print("------------------------------")
    print(f"bkash            {bkash[0]}টা   {my_tools.taka(bkash[1])}")
    print(f"nagad            {nagad[0]}টা   {my_tools.taka(nagad[1])}")
    print(f"card             {card[0]}টা   {my_tools.taka(card[1])}")
    print(f"rocket           {rocket[0]}টা   {my_tools.taka(rocket[1])}")
    print(f"cash on delivery {cash[0]}টা   {my_tools.taka(cash[1])}")
    print("------------------------------")
    print(f"সব মিলিয়ে: {my_tools.taka(grand)}")


if __name__ == "__main__":
    main()
