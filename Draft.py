import json
with open("ex_7.json", 'w', encoding="utf-8") as write_f, open("test_text_7.txt", encoding="utf-8") as my_file:
    income = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_file}
    f_up = [n for n in income.values() if n > 0]
    result = [income, {"real_income": round(sum(f_up) / len(f_up))}]

    json.dump(result, write_f, ensure_ascii=False, indent=4)