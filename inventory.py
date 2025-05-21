# Create an inventory management system (add, remove, and view items in the inventory)
# Use loops to display / update a list of stock items

# dictionary to hold the items + quantities
inventory = {}

# list to hold the action log messages
action_log = []

# A while loop to keep the system running until the user exits.
while True:
    
    # Menu options to choose actions.
    print("\n*** Abisha's Inventory Mgt System***")  
    print("1. View Inventory")
    print("2. Update Inventory")
    print("3. View Action Log")
    print("4. Exit")

    main_choice = input("Choose an option between 1-4: ")

    if main_choice == '1':
        
        # Display the current inventory.
        if inventory:
            
            print("\nCurrent Inventory:")
            
            for item, quantity in inventory.items():
                print(f"{item}: {quantity}")
        else:
            print("Inventory is empty.")

    elif main_choice == '2':
        
        while True:
            print("\n--- Inventory Update Menu ---")
            print("Type 'back' anytime to return to the main menu.")
        
            item = input("Enter the item name: ")
            if item.lower() == 'back':
                break
            
            action = input("What do you wish to do to this item? (add/remove): ").lower()
            if action == 'back':
                break

            
            if action in ['add', 'remove']:
                
                # For remove, check item existence first to avoid unnecessary quantity input
                if action == 'remove' and item not in inventory:
                    print(f"{item} doesn't exist in this inventory.")
                    continue

                # Ask for quantity and validate it once here
                try:
                    quantity = input(f"Enter the quantity to {action}: ").strip()
                    if quantity.lower() == 'back':
                        break
                    #  Convert to integer 
                    quantity = int(quantity)
                    
                except ValueError:
                    print("Invalid input. Please enter a whole number.")
                    continue

                if quantity <= 0:
                    print("Quantity must be a greater than 0.")
                    continue
            
                if action == 'add': 

                    # Check if the item already exists in the inventory
                    if item in inventory:
                        inventory[item] += quantity
                    else:
                        inventory[item] = quantity
                        
                    print(f"Added {quantity} of {item} to the inventory.")
                    
                    # Log the action
                    action_log.append(f"Added {quantity} of '{item}' to inventory. Total: {inventory[item]}")
            
                elif action == 'remove':
                    
                    if item in inventory:
                        
                        if quantity > inventory[item]:
                            print(f"You cannot remove {quantity}. Only {inventory[item]} available in stock.")
                        
                        elif quantity == inventory[item]:
                            
                            confirm = input(f"You are about to remove all '{item}' from the inventory. Do you wish to proceed? (yes/no): ").lower()
                            
                            if confirm == "yes":
                                del inventory[item]
                                print(f"'{item}' removed completely from inventory.")
                                
                                action_log.append(f"Removed all of '{item}'")
                                
                            else:
                                print(f"Removal of '{item}' cancelled.")

                        else:
                            # Remove the specified quantity from the inventory hence why we use -=
                            # This is a shorthand for inventory[item] = inventory[item] - quantity
                            inventory[item] -= quantity
                            print(f"Removed {quantity} of {item} from the inventory.")
                            
                            action_log.append(f"Removed {quantity} of '{item}' (remaining {inventory[item]})")
                         
            else:
                print("Invalid action. Please choose 'add' or 'remove'.")
        
    elif main_choice == '3':
        # View action log
        if action_log:
            print("\n--- Action Log ---")
            
            for entry in action_log:
                print(f"• {entry}")
        else:
            print("Action log is empty.")   
   
    elif main_choice == '4':
        print("Exiting....Thank you!")
        break

    else:
        print("Invalid menu option. Please choose 1, 2, 3 or 4.")

