def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item_name = input("What is the item name? ").strip()
            shopping_list.append(item_name)
            print("Updated shopping list:", shopping_list)

        elif choice == '2':
            item_name = input("What is the item name to remove? ").strip()
            if item_name not in shopping_list:
                print("The item is not found.")
            else:
                shopping_list.remove(item_name)
                print(f"Removed '{item_name}'. Updated list:", shopping_list)

        elif choice == '3':
            if shopping_list:
                print("Current shopping list:")
                for item in shopping_list:
                    print("-", item)
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
