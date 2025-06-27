import itertools

leetspeak_map = {
    'a': ['@', '4'],
    'e': ['3'],
    'i': ['1', '!'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['7']
}

def leetspeak_variants(word):
    variants = set([word])
    for i, char in enumerate(word):
        if char.lower() in leetspeak_map:
            for symbol in leetspeak_map[char.lower()]:
                variant = word[:i] + symbol + word[i+1:]
                variants.add(variant)
    return variants

def generate_wordlist(name, dob, pet):
    print("\n📦 Generating wordlist...")
    
    base_words = [name.lower(), dob, pet.lower()]
    suffixes = ["", "123", "2024", "!", "@", "#"]

    combinations = set()
    for word in base_words:
        variants = leetspeak_variants(word)
        for v in variants:
            for s in suffixes:
                combinations.add(v + s)
                combinations.add(s + v)

    # Add permutations of inputs
    for combo in itertools.permutations(base_words, 2):
        joined = ''.join(combo)
        combinations.update(leetspeak_variants(joined))

    # Export
    with open("custom_wordlist.txt", "w") as file:
        for word in sorted(combinations):
            file.write(word + "\n")

    print(f"✅ Wordlist saved to custom_wordlist.txt with {len(combinations)} words.")
