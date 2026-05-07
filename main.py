seats = 5
bookings = {}

while True:
    print("\n--- Railway Reservation System ---")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Seats:", seats)

    elif choice == 2:
        if seats > 0:
            name = input("Enter passenger name: ")
            age = input("Enter passenger age: ")
            booking_id = "B" + str(len(bookings) + 1)

            bookings[booking_id] = {
                "name": name,
                "age": age
            }

            seats = seats - 1
            print("Ticket Booked Successfully")
            print("Your Booking ID is:", booking_id)
        else:
            print("No seats available")

    elif choice == 3:
        bid = input("Enter Booking ID: ")
        if bid in bookings:
            print("Passenger Name:", bookings[bid]["name"])
            print("Passenger Age:", bookings[bid]["age"])
            print("Seat Confirmed")
        else:
            print("Booking ID not found")

    elif choice == 4:
        bid = input("Enter Booking ID to cancel: ")
        if bid in bookings:
            del bookings[bid]
            seats = seats + 1
            print("Ticket Cancelled Successfully")
        else:
            print("Booking ID not found")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
