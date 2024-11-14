VCARD_PRICE = 250
GPU_PERCENT = 0.35
RAM_PERCENT = 0.10
DISCOUNT = 0.15

budget = float(input())
vcards = int(input())
gpus = int(input())
rams = int(input())

gpu_price = (vcards * VCARD_PRICE) * GPU_PERCENT
rams_price = (vcards * VCARD_PRICE) * RAM_PERCENT

sum_total = vcards * VCARD_PRICE + gpus * gpu_price + rams * rams_price

if vcards > gpus:
    sum_total = sum_total - (sum_total * DISCOUNT)

if sum_total <= budget:
    print(f"You have {budget - sum_total:.2f} leva left!")
else:
    print(f"Not enough money! You need {sum_total - budget:.2f} leva more!")
