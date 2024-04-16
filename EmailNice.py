def Main():
    while True:
        Name = input("Whats your name?\n")
        Receiver = input("Who is receiving this email?\n")
        MainMessage = input('Whats the main email subject?\n')
        Email = f"Dear {Receiver}\n\n{MainMessage}\n\nSincerely, Karson Ulerick"
        print(f"Email:\n{Email}")

if(__name__ == "__main__"):
    Main()