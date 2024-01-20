# Conexión base de datos

class DatabaseConnectionManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DatabaseConnectionManager, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self, database_url):
        # Lógica para establecer la conexión a la base de datos
        self.connection = f"Connected to {database_url}"

    def get_connection(self):
        return self.connection

# Uso del Singleton
db_manager = DatabaseConnectionManager()
db_manager.connect("mysql://localhost:3306/mydatabase")
print(db_manager.get_connection())

# Intentar crear otra instancia, debería devolver la misma instancia creada anteriormente
another_db_manager = DatabaseConnectionManager()
print(another_db_manager.get_connection())
