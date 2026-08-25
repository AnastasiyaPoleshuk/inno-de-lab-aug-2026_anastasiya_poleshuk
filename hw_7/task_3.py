db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

connection_dict = db_config.get("connection")

host = connection_dict.get("host")
port = connection_dict.get("port")

ssl_mode = db_config.get("ssl_settings", {}).get("ssl_mode", "verify-full")

connection_dict["user"] = "admin"
connection_dict["max_connections"] = 100

print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")
for key, value in connection_dict.items():
    print(f"* {key}: {value}")
