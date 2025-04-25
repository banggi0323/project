def calculateElectricRate(month, usage):
    if month == 7 or month == 8:
        if usage <= 300:
           return usage * 112
        elif usage <= 450:
           return (300 * 112) + (usage - 300) * 206.6
        elif usage <= 1000:
            return (300 * 112) + (150 * 206.6) + (usage - 450) * 299.3
        else:
            return (300 * 112) + (150 * 206.6) + (450 * 299.3) + (usage - 1000) * 728.2
    else:
        if usage <= 200:
            return usage * 112
        elif usage <= 400:
            return (200 * 112) + (usage - 200) * 206.6
        elif usage <= 1000:
            return (200 * 112) + (200 * 206.6) + (usage - 400) * 299.3
        else:
            if (month == 12 or month == 1 or month == 2):
                return (200 * 112) + (200 * 206.6) + (400 * 299.3) + (usage - 1000) * 728.2
            else:
                return (200 * 112) + (200 * 206.6) + (usage - 400) * 299.3


month = int(input("지금은 몇월인가요? "))
usage = int(input("사용량은 몇 kWh인가요? "))
    
total_cost = calculateElectricRate(month, usage)
print(f"전력량요금은 {int(total_cost)}원입니다.")

