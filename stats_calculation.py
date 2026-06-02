python
# Simple script to calculate interference percentages
russian_intrusions = 43
english_intrusions = 3
l1_intrusions = 5
‌
total = russian_intrusions + english_intrusions + l1_intrusions
‌
print(f"Total Intrusions: {total}")
print(f"Russian (L4) Impact: {(russian_intrusions/total)*100:.2f}%")
print(f"English (L3) Impact: {(english_intrusions/total)*100:.2f}%")
print(f"L1/L2 Impact: {(l1_intrusions/total)*100:.2f}%")
