import json

system_telemetry = [
  ("srv_01", 12.5, 64, "online"),
  ("srv_02", 85.0, 92, "online"),
  ("srv_03", 0.0, 0, "offline"),
  ("srv_04", 45.2, 78, "online"),
  ("srv_05", 95.1, 99, "online")
]

active_nodes = []
average_cpu = []
max_ram = []

filtered_telemetry = [
    (node_name, cpu_load, ram_usage, status) 
    for node_name, cpu_load, ram_usage, status in system_telemetry 
    if status != "offline"
]

active_nodes_count = len(filtered_telemetry)

for  node_name, cpu_load, ram_usage, status in filtered_telemetry:
  active_nodes.append(node_name)
  average_cpu.append(cpu_load)
  max_ram.append(ram_usage)

telemetry_dict = {
  "active_nodes_count": active_nodes_count,
  "metrics": {
    "average_cpu": round(sum(average_cpu) / active_nodes_count, 2),
    "max_ram": max(max_ram)
  }
}

print(f"Активные узлы в сети: {active_nodes}")
print("Итоговый отчет телеметрии:")
print(json.dumps(telemetry_dict, indent=2))