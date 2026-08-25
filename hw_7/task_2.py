raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
"SUCCESS:0", "SUCCESS:250", "ERROR:200"]

success_transactions = [val for raw in raw_transactions if raw.startswith("SUCCESS") and (val := int(raw.split(":")[1])) > 0]

print(success_transactions)