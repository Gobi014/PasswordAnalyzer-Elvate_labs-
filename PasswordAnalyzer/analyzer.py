from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    score = result['score']  # 0 = very weak, 4 = strong

    feedback = result['feedback']['suggestions']
    crack_times = result['crack_times_display']['offline_fast_hashing_1e10_per_second']

    print(f"\n🧠 Password Score (0-4): {score}")
    print("🛠️ Crack Time Estimate:", crack_times)
    
    if feedback:
        print("📋 Suggestions to improve:")
        for suggestion in feedback:
            print(f" - {suggestion}")
    else:
        print("✅ No suggestions. Strong password!")

    return score
