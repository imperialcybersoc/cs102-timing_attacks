import time
import hmac


def insecure_compare(val1, val2):
    if len(val1) != len(val2):
        return False
    for x, y in zip(val1, val2):
        if x != y:
            return False
        time.sleep(0.01)  # Simulate time delay for each character comparison
    return True

def secure_compare(val1, val2):
    return hmac.compare_digest(val1, val2)


def timing_attack_demo():
    correct_password = "securepassword"
    attempt = "securepassw0rd"
    
    start_time = time.time()
    insecure_result = insecure_compare(correct_password, attempt)
    insecure_duration = time.time() - start_time
    
    start_time = time.time()
    secure_result = secure_compare(correct_password, attempt)
    secure_duration = time.time() - start_time
    
    print(f"Insecure comparison result: {insecure_result}, Time taken: {insecure_duration:.6f} seconds")
    print(f"Secure comparison result: {secure_result}, Time taken: {secure_duration:.6f} seconds")


if __name__ == "__main__":
    timing_attack_demo()
