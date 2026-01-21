# STEP 1: HotelRoom class
class HotelRoom:
    def __init__(self, room_no, room_type, price, status):
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
        self.status = status   # Available / Booked

    def display(self):
        print("Room No:", self.room_no)
        print("Room Type:", self.room_type)
        print("Price per Day:", self.price)
        print("Status:", self.status)
        print("----------------------------")


# STEP 2: HotelManagementSystem class
class HotelManagementSystem:
    def __init__(self):
        self.rooms = []   # list to store room objects

    # STEP 3: Add Room
    def add_room(self):
        print("\nAdd New Room")

        room_no = input("Enter Room Number: ")
        room_type = input("Enter Room Type (AC/Non-AC): ")
        price = input("Enter Price per Day: ")
        status = "Available"

        room = HotelRoom(room_no, room_type, price, status)
        self.rooms.append(room)

        print("Room added successfully!")

    # STEP 4: View All Rooms
    def view_rooms(self):
        print("\nAll Rooms")

        if len(self.rooms) == 0:
            print("No rooms available.")
            return

        for room in self.rooms:
            room.display()

    # STEP 5: Search Room by Room Number
    def search_room(self):
        print("\nSearch Room")

        search_no = input("Enter Room Number: ")

        for room in self.rooms:
            if room.room_no == search_no:
                print("Room Found:")
                room.display()
                return

        print("Room not found.")

    # STEP 6: Book Room
    def book_room(self):
        print("\nBook Room")

        book_no = input("Enter Room Number to Book: ")

        for room in self.rooms:
            if room.room_no == book_no:
                if room.status == "Available":
                    room.status = "Booked"
                    print("Room booked successfully!")
                else:
                    print("Room already booked!")
                return

        print("Room not found.")

    # STEP 7: Delete Room
    def delete_room(self):
        print("\nDelete Room")

        delete_no = input("Enter Room Number to Delete: ")

        for room in self.rooms:
            if room.room_no == delete_no:
                self.rooms.remove(room)
                print("Room deleted successfully!")
                return

        print("Room not found.")


# STEP 8: Main Menu (Menu Driven Program)
def main():
    system = HotelManagementSystem()

    while True:
        print("\n===== Hotel Management System =====")
        print("1. Add Room")
        print("2. View All Rooms")
        print("3. Search Room")
        print("4. Book Room")
        print("5. Delete Room")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            system.add_room()
        elif choice == "2":
            system.view_rooms()
        elif choice == "3":
            system.search_room()
        elif choice == "4":
            system.book_room()
        elif choice == "5":
            system.delete_room()
        elif choice == "6":
            print("Exiting application...")
            break
        else:
            print("Invalid choice! Please try again.")


# STEP 9: Run Program
if __name__ == "__main__":
    main()
