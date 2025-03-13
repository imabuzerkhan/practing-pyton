def process_customer_data(file_name):
    customer_dict = {}

    # Read the file and populate customer_dict
    with open(file_name, "r") as f:
        for line in f:
            Name, score = line.strip().split(",")
            score = int(score)
            customer_dict[Name] = score

    # Define reward function
    def reward(total):
        if total >= 500:
            return "Gold"
        elif total >= 200:
            return "Silver"
        elif total >= 100:
            return "Bronze"
        else:
            return "No reward"

    # Process customer data into customer_summary
    customer_summary = {}
    for name, total in customer_dict.items():
        rewards_level = reward(total)
        customer_summary[name] = (total, rewards_level)

    return customer_summary

# Example usage
file_name = "customer.txt"
summary = process_customer_data(file_name)
print(summary)
