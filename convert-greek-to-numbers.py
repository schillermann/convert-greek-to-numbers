import argparse

# Greek letter to number mapping
GREEK_NUMERAL_MAP = {
    'α': 1, 'Α': 1, 'ά': 1,
    'β': 2, 'Β': 2,
    'γ': 3, 'Γ': 3,
    'δ': 4, 'Δ': 4,
    'ε': 5, 'Ε': 5, 'ἐ': 5,
    'ϛ': 6,
    'ζ': 7, 'Ζ': 7,
    'η': 8, 'Η': 8,
    'θ': 9, 'Θ': 9,
    'ι': 10, 'Ι': 10, 'Ἰ': 10,
    'κ': 20, 'Κ': 20,
    'λ': 30, 'Λ': 30,
    'μ': 40, 'Μ': 40,
    'ν': 50, 'Ν': 50,
    'ξ': 60, 'Ξ': 60,
    'ο': 70, 'Ο': 70, 'ὁ': 70,
    'π': 80, 'Π': 80,
    'ϟ': 90, 'Ϟ': 90,
    'ρ': 100, 'Ρ': 100,
    # When the Greek letter σ is at the end of a word, it is written ς
    'σ': 200, 'Σ': 200, 'ς': 200,  
    'τ': 300, 'Τ': 300,
    'υ': 400, 'Υ': 400, 'ῦ': 400,
    'φ': 500, 'Φ': 500,
    'χ': 600, 'Χ': 600,
    'ψ': 700, 'Ψ': 700,
    'ω': 800, 'Ω': 800,
    'ϡ': 900, 'Ϡ': 900,
}

def greek_to_number(text):
    return sum(GREEK_NUMERAL_MAP.get(char, 0) for char in text)

def letter_values(text):
    result = []
    for char in text:
        if char == ' ':
            result.append((None, None))  # Insert blank line for space
        else:
            result.append((char, GREEK_NUMERAL_MAP.get(char, 0)))
    return result

def main():
    parser = argparse.ArgumentParser(description="Convert Greek letters in text to numeric values.")
    parser.add_argument("text", nargs="?", help="Greek text to convert")
    parser.add_argument("--per-word", action="store_true", help="Show total numeric value of each word")
    parser.add_argument("--per-letter", action="store_true", help="Show numeric value of each letter")
    args = parser.parse_args()

    input_text = args.text if args.text else input("Enter Greek text: ")

    if args.per_letter:
        print("Letter values:")
        for char, val in letter_values(input_text):
            if char is None:
                print()  # Print blank line for space
            else:
                print(f"{char}: {val}")

    if args.per_word:
        print("\nWord values:")
        for word in input_text.split():
            value = greek_to_number(word)
            print(f"{word}: {value}")

    if not args.per_word and not args.per_letter:
        total_value = greek_to_number(input_text)
        print(f"Total numeric value: {total_value}")

if __name__ == "__main__":
    main()
