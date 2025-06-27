import argparse
from analyzer import analyze_password
from wordlist_generator import generate_wordlist

def main():
    parser = argparse.ArgumentParser(description="🔐 Password Strength Analyzer & Wordlist Generator")
    parser.add_argument("-p", "--password", help="Password to analyze", required=True)
    parser.add_argument("-n", "--name", help="User name", required=False)
    parser.add_argument("-d", "--dob", help="Date of birth", required=False)
    parser.add_argument("-t", "--pet", help="Pet name", required=False)
    parser.add_argument("-w", "--wordlist", help="Generate wordlist", action="store_true")

    args = parser.parse_args()

    analyze_password(args.password)

    if args.wordlist:
        if args.name and args.dob and args.pet:
            generate_wordlist(args.name, args.dob, args.pet)
        else:
            print("⚠️ Missing name, DOB, or pet info for wordlist generation.")

if __name__ == "__main__":
    main()
