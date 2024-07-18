# from flask import Flask, jsonify, request
# from flask_cors import CORS  # Import CORS from flask_cors
# import pyodbc

# # app = Flask(__name__)
# # #za live CORS(app, resources={r"/api/*": {"origins": "http://10.3.41.24"}})
# # CORS(app, resources={r"/api/*": {"origins": "127.0.0.1"}})
# # #CORS(app)


# # # Replace these with your actual SQL Server credentials
# # server = "127.0.0.1"
# # port = 3306
# # database = "Foam_tools"
# # username = "bde"
# # password = "!bde1234"
# # driver = "ODBC Driver 17 for SQL Server"

# # conn_str = (
# #     f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
# # )
# # conn = pyodbc.connect(conn_str)
# # cursor = conn.cursor()

# app = Flask(__name__)
# #CORS(app) 
# CORS(app, resources={r"/api/*": {"origins": "*"}})
# # Replace these with your actual SQL Server credentials
# #"NB-JI-0316\\SQLEXPRESS" for testing on local pc
# #za db gdje je live 10.3.28.68
# server = "10.3.41.24"
# port = 3306
# database = 'Foam_tools'
# username = 'bde'
# password = '!bde1234'
# driver = 'ODBC Driver 18 for SQL Server'

# conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=no'
# conn = pyodbc.connect(conn_str)
# cursor = conn.cursor()

# @app.route(
#     "/api/active",
#     methods=["GET", "POST", "DELETE"],
# )
# def handle_active():
#     if request.method == "GET":
#         cursor.execute(
#             "SELECT TOP (1000)  [Alat] FROM [Foam_tools].[dbo].[Active]"
#         )
#         active_data = [
#             dict(zip([column[0] for column in cursor.description], row))
#             for row in cursor.fetchall()
#         ]
#         return jsonify(active_data)

#     elif request.method == "POST":
#         data = request.get_json()
#         tool_name = data.get('tool')  # Assuming the key for tool name is 'tool'

#         # Insert new tool into the Active table
#         insert_query = """
#             INSERT INTO [Foam_tools].[dbo].[Active] ([Alat])
#             VALUES (?)
#         """
#         try:
#             cursor.execute(insert_query, (tool_name,))
#             conn.commit()
#             print(f"Tool '{tool_name}' added to the database.")
#             return jsonify({"message": "Tool added successfully"})
#         except Exception as e:
#             conn.rollback()
#             print(f"Error adding tool '{tool_name}': {str(e)}")
#             return jsonify({"error": str(e)}), 500

#     elif request.method == "DELETE":
#         data = request.get_json()
#         tool_name = data.get('tool')  # Assuming the key for tool name is 'tool'

#         # Delete tool from the Active table
#         delete_query = """
#             DELETE FROM [Foam_tools].[dbo].[Active]
#             WHERE [Alat] = ?
#         """
#         try:
#             cursor.execute(delete_query, (tool_name,))
#             conn.commit()
#             print(f"Tool '{tool_name}' deleted from the database.")
#             return jsonify({"message": "Tool deleted successfully"})
#         except Exception as e:
#             conn.rollback()
#             print(f"Error deleting tool '{tool_name}': {str(e)}")
#             return jsonify({"error": str(e)}), 500


# # Route for /api/karijeri
# @app.route("/api/karijers", methods=["GET", "POST", "DELETE"])
# def handle_carrier():
#     if request.method == "GET":
#         cursor.execute(
#             "SELECT TOP (1000)  [Serijski_broj] FROM [Foam_tools].[dbo].[Karijers]"
#         )
#         karijeri_data = [
#             dict(zip([column[0] for column in cursor.description], row))
#             for row in cursor.fetchall()
#         ]
#         return jsonify(karijeri_data)

#     elif request.method == "POST":
#         data = request.get_json()
#         carrier_name = data.get('Serijski_broj')
        
#         # Ensure your connection and cursor are properly set up
#         try:
#             # Correct SQL query with parameter placeholder
#             insert_query = "INSERT INTO [Foam_tools].[dbo].[Karijers] ([Serijski_broj]) VALUES (?)"
            
#             # Execute query with parameter tuple
#             cursor.execute(insert_query, (carrier_name,))
#             conn.commit()
            
#             print(f"Carrier '{carrier_name}' added to the database.")
#             return jsonify({"message": "Carrier added successfully"})
        
#         except Exception as e:
#             conn.rollback()
#             print(f"Error adding carrier '{carrier_name}': {str(e)}")
#             return jsonify({"error": str(e)}), 500


#     elif request.method == "DELETE":
#         data = request.get_json()
#         carrier_name = data.get('Serijski_broj')
        
#         try:
#             # Example SQL delete query
#             delete_query = """DELETE FROM [dbo].[Karijers] WHERE Serijski_broj = ? """
            
#             # Execute query with parameter tuple
#             cursor.execute(delete_query, (carrier_name))
#             conn.commit()
            
#             print(f"Carrier '{carrier_name}' deleted from the database.")
#             return jsonify({"message": "Carrier deleted successfully"})
        
#         except Exception as e:
#             conn.rollback()
#             print(f"Error deleting carrier '{carrier_name}': {str(e)}")
#             return jsonify({"error": str(e)}), 500



# @app.route('/api/users', methods=['GET', 'POST', 'DELETE'])
# def handle_users():
#     cursor = conn.cursor()

#     if request.method == 'GET':
#         cursor.execute('SELECT id, username, email, permissions FROM dbo.Users')
#         rows = cursor.fetchall()

#         users = []
#         for row in rows:
#             user = {
#                 'id': row[0],
#                 'username': row[1],
#                 'email': row[2],
#                 'permissions': row[3]
#             }
#             users.append(user)

#         return jsonify(users)

#     elif request.method == 'POST':
#         data = request.json
#         username = data.get('username')
#         email = data.get('email')
#         permissions = data.get('permissions')

#         if username and email and permissions:
#             cursor.execute('INSERT INTO dbo.Users (username, email, permissions) VALUES (?, ?, ?)',
#                            (username, email, permissions))
#             conn.commit()
#             return jsonify({'message': 'User added successfully'}), 201
#         else:
#             return jsonify({'error': 'Missing data. Required fields: username, email, permissions'}), 400

#     elif request.method == 'DELETE':
#         user_id = request.args.get('id')  # Get the user id from query parameters

#         if user_id:
#             cursor.execute('DELETE FROM dbo.Users WHERE id = ?', (user_id,))
#             conn.commit()
#             return jsonify({'message': f'User with id {user_id} deleted successfully'}), 200
#         else:
#             return jsonify({'error': 'Missing user id parameter'}), 400



# # Route for /api/oficijalno
# @app.route("/api/oficijalno", methods=["GET"])
# def handle_oficijalno():
#     if request.method == "GET":
#         cursor.execute(
#             "SELECT TOP (1000) [Interni_broj], [Kupac], [Projekat], [Vrsta_alata], [Broj_proizvoda], [Kavitet] FROM [Foam_tools].[dbo].[Oficijalno]"
#         )
#         oficijalno_data = [
#             dict(zip([column[0] for column in cursor.description], row))
#             for row in cursor.fetchall()
#         ]
#         return jsonify(oficijalno_data)


# # Route for /api/rezerva
# @app.route("/api/rezerva", methods=["GET"])
# def handle_rezerva():
#     if request.method == "GET":
#         cursor.execute(
#             "SELECT TOP (1000) [RB], [Pozicija], [Alat], [Lokacija] FROM [Foam_tools].[dbo].[Rezerva]"
#         )
#         rezerva_data = [
#             dict(zip([column[0] for column in cursor.description], row))
#             for row in cursor.fetchall()
#         ]
#         return jsonify(rezerva_data)


# # Route for /api/trenutno_stanje
# @app.route("/api/trenutno_stanje", methods=["GET"])
# def handle_trenutno_stanje():
#     if request.method == "GET":
#         cursor.execute(
#             "SELECT TOP (1000) [RB], [Pozicija], [Alat], [Kerijer] FROM [Foam_tools].[dbo].[Trenutno_stanje]"
#         )
#         trenutno_stanje_data = [
#             dict(zip([column[0] for column in cursor.description], row))
#             for row in cursor.fetchall()
#         ]
#         return jsonify(trenutno_stanje_data)


# if __name__ == "__main__":
#     app.run(debug=True)


# # Fa87362/..aa!fF

from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS from flask_cors
import pyodbc

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Replace these with your actual SQL Server credentials
server = "10.3.28.68"
port = 1433 # Default port for SQL Server is sometimes 3306
database = 'Foam_tools'
username = 'bde'
password = '!bde1234'
driver = 'ODBC Driver 18 for SQL Server'

# Update connection string to use the correct port
conn_str = f'DRIVER={driver};SERVER={server},{port};DATABASE={database};UID={username};PWD={password};Encrypt=no'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

@app.route(
    "/api/active",
    methods=["GET", "POST", "DELETE"],
)
def handle_active():
    if request.method == "GET":
        cursor.execute(
            "SELECT TOP (1000)  [Alat] FROM [Foam_tools].[dbo].[Active]"
        )
        active_data = [
            dict(zip([column[0] for column in cursor.description], row))
            for row in cursor.fetchall()
        ]
        return jsonify(active_data)

    elif request.method == "POST":
        data = request.get_json()
        tool_name = data.get('tool')  # Assuming the key for tool name is 'tool'

        # Insert new tool into the Active table
        insert_query = """
            INSERT INTO [Foam_tools].[dbo].[Active] ([Alat])
            VALUES (?)
        """
        try:
            cursor.execute(insert_query, (tool_name,))
            conn.commit()
            print(f"Tool '{tool_name}' added to the database.")
            return jsonify({"message": "Tool added successfully"})
        except Exception as e:
            conn.rollback()
            print(f"Error adding tool '{tool_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500

    elif request.method == "DELETE":
        data = request.get_json()
        tool_name = data.get('tool')  # Assuming the key for tool name is 'tool'

        # Delete tool from the Active table
        delete_query = """
            DELETE FROM [Foam_tools].[dbo].[Active]
            WHERE [Alat] = ?
        """
        try:
            cursor.execute(delete_query, (tool_name,))
            conn.commit()
            print(f"Tool '{tool_name}' deleted from the database.")
            return jsonify({"message": "Tool deleted successfully"})
        except Exception as e:
            conn.rollback()
            print(f"Error deleting tool '{tool_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500


# Route for /api/karijeri
@app.route("/api/karijers", methods=["GET", "POST", "DELETE"])
def handle_carrier():
    if request.method == "GET":
        cursor.execute(
            "SELECT TOP (1000)  [Serijski_broj] FROM [Foam_tools].[dbo].[Karijers]"
        )
        karijeri_data = [
            dict(zip([column[0] for column in cursor.description], row))
            for row in cursor.fetchall()
        ]
        return jsonify(karijeri_data)

    elif request.method == "POST":
        data = request.get_json()
        carrier_name = data.get('Serijski_broj')
        
        # Ensure your connection and cursor are properly set up
        try:
            # Correct SQL query with parameter placeholder
            insert_query = "INSERT INTO [Foam_tools].[dbo].[Karijers] ([Serijski_broj]) VALUES (?)"
            
            # Execute query with parameter tuple
            cursor.execute(insert_query, (carrier_name,))
            conn.commit()
            
            print(f"Carrier '{carrier_name}' added to the database.")
            return jsonify({"message": "Carrier added successfully"})
        
        except Exception as e:
            conn.rollback()
            print(f"Error adding carrier '{carrier_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500


    elif request.method == "DELETE":
        data = request.get_json()
        carrier_name = data.get('Serijski_broj')
        
        try:
            # Example SQL delete query
            delete_query = """DELETE FROM [dbo].[Karijers] WHERE Serijski_broj = ? """
            
            # Execute query with parameter tuple
            cursor.execute(delete_query, (carrier_name))
            conn.commit()
            
            print(f"Carrier '{carrier_name}' deleted from the database.")
            return jsonify({"message": "Carrier deleted successfully"})
        
        except Exception as e:
            conn.rollback()
            print(f"Error deleting carrier '{carrier_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500



@app.route('/api/users', methods=['GET', 'POST', 'DELETE'])
def handle_users():
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute('SELECT id, username, email, permissions FROM dbo.Users')
        rows = cursor.fetchall()

        users = []
        for row in rows:
            user = {
                'id': row[0],
                'username': row[1],
                'email': row[2],
                'permissions': row[3]
            }
            users.append(user)

        return jsonify(users)

    elif request.method == 'POST':
        data = request.json
        username = data.get('username')
        email = data.get('email')
        permissions = data.get('permissions')

        if username and email and permissions:
            cursor.execute('INSERT INTO dbo.Users (username, email, permissions) VALUES (?, ?, ?)',
                           (username, email, permissions))
            conn.commit()
            return jsonify({'message': 'User added successfully'}), 201
        else:
            return jsonify({'error': 'Missing data. Required fields: username, email, permissions'}), 400

    elif request.method == 'DELETE':
        user_id = request.args.get('id')  # Get the user id from query parameters

        if user_id:
            cursor.execute('DELETE FROM dbo.Users WHERE id = ?', (user_id,))
            conn.commit()
            return jsonify({'message': f'User with id {user_id} deleted successfully'}), 200
        else:
            return jsonify({'error': 'Missing user id parameter'}), 400



# Route for /api/oficijalno
@app.route("/api/oficijalno", methods=["GET"])
def handle_oficijalno():
    if request.method == "GET":
        cursor.execute(
            "SELECT TOP (1000) [Interni_broj], [Kupac], [Projekat], [Vrsta_alata], [Broj_proizvoda], [Kavitet] FROM [Foam_tools].[dbo].[Oficijalno]"
        )
        oficijalno_data = [
            dict(zip([column[0] for column in cursor.description], row))
            for row in cursor.fetchall()
        ]
        return jsonify(oficijalno_data)


# Route for /api/rezerva
@app.route("/api/rezerva", methods=["GET"])
def handle_rezerva():
    if request.method == "GET":
        cursor.execute(
            "SELECT TOP (1000) [RB], [Pozicija], [Alat], [Lokacija] FROM [Foam_tools].[dbo].[Rezerva]"
        )
        rezerva_data = [
            dict(zip([column[0] for column in cursor.description], row))
            for row in cursor.fetchall()
        ]
        return jsonify(rezerva_data)


# Route for /api/trenutno_stanje
@app.route("/api/trenutno_stanje", methods=["GET"])
def handle_trenutno_stanje():
    if request.method == "GET":
        cursor.execute(
            "SELECT TOP (1000) [Kerijer] FROM [Foam_tools].[dbo].[Trenutno_stanje]"
        )
        trenutno_stanje_data = [
            dict(zip([column[0] for column in cursor.description], row))
            for row in cursor.fetchall()
        ]
        return jsonify(trenutno_stanje_data)
    
@app.route("/api/table_name_carriers", methods=["GET", 'POST'])
def handle_table_name_carriers():
    if request.method == "GET":
        cursor.execute(
            "SELECT TOP (1) [id], [name] FROM [Foam_tools].[dbo].[table_name_carriers]"
        )
        names = [
            dict(zip([column[0] for column in cursor.description], row))
            for row in cursor.fetchall()
        ]
        return jsonify(names)
    elif request.method == "POST":
        data = request.get_json()
        table_name = data.get('name')
        
        # Ensure your connection and cursor are properly set up
        try:
            # Begin transaction
            cursor.execute("BEGIN TRANSACTION")
            
            # Delete existing record with id = 0
            cursor.execute("DELETE FROM [Foam_tools].[dbo].[table_name_carriers] WHERE id = 0")
            
            # Insert new record
            insert_query = "INSERT INTO [Foam_tools].[dbo].[table_name_carriers] ([id], [name]) VALUES (?, ?)"
            cursor.execute(insert_query, (0, table_name))
            
            # Commit transaction
            cursor.execute("COMMIT")
            conn.commit()
            
            print(f"Carrier '{table_name}' added to the database.")
            return jsonify({"message": "Carrier added successfully", "id": 0})
        
        except Exception as e:
            cursor.execute("ROLLBACK")
            conn.rollback()
            print(f"Error adding tool '{table_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500

@app.route("/api/table_name_tools", methods=["GET", 'POST'])
def handle_table_name_tools():
    if request.method == "GET":
        cursor.execute(
            "SELECT TOP (1) [id], [name] FROM [Foam_tools].[dbo].[table_name_tools]"
        )
        names = [
            dict(zip([column[0] for column in cursor.description], row))
            for row in cursor.fetchall()
        ]
        return jsonify(names)
    elif request.method == "POST":
        data = request.get_json()
        table_name = data.get('name')
        
        # Ensure your connection and cursor are properly set up
        try:
            # Begin transaction
            cursor.execute("BEGIN TRANSACTION")
            
            # Delete existing record with id = 0
            cursor.execute("DELETE FROM [Foam_tools].[dbo].[table_name_tools] WHERE id = 0")
        
            # Insert new record
            insert_query = "INSERT INTO [Foam_tools].[dbo].[table_name_tools] ([id], [name]) VALUES (?, ?)"
            cursor.execute(insert_query, (0, table_name))
            
            # Commit transaction
            cursor.execute("COMMIT")
            conn.commit()
            
            print(f"Tools '{table_name}' added to the database.")
            return jsonify({"message": "Tool added successfully", "id": 0})
        
        except Exception as e:
            cursor.execute("ROLLBACK")
            conn.rollback()
            print(f"Error adding tool '{table_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500

@app.route("/api/carriers_allocation", methods=["GET", "POST", "DELETE"])
def handle_carriers_allocation():
    if request.method == "GET":
        cursor.execute(
            "SELECT TOP (1000)  [name], [position] FROM [Foam_tools].[dbo].[carriers_allocation]"
        )
        carriers_allocation = [
            dict(zip([column[0] for column in cursor.description], row))
            for row in cursor.fetchall()
        ]
        return jsonify(carriers_allocation)

    elif request.method == "POST":
        data = request.get_json()
        carrier_name = data.get('name')
        carrier_position = data.get('position')
        
        # Ensure your connection and cursor are properly set up
        try:
            cursor.execute("DELETE FROM [Foam_tools].[dbo].[carriers_allocation] WHERE name = ?", (carrier_name))
        
            # Insert new record
            insert_query = "INSERT INTO [Foam_tools].[dbo].[carriers_allocation] ([name], [position]) VALUES (?, ?)"
            cursor.execute(insert_query, (carrier_name, carrier_position))
            
            print(f"Carrier '{carrier_name}' added to the database.")
            return jsonify({"message": "Carrier added successfully"})
        
        except Exception as e:
            conn.rollback()
            print(f"Error adding carrier '{carrier_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500


    elif request.method == "DELETE":
        data = request.get_json()
        carrier_name = data.get('name')
        
        try:
            # Example SQL delete query
            delete_query = """DELETE FROM [Foam_tools].[dbo].[carriers_allocation] WHERE name = ? """
            
            # Execute query with parameter tuple
            cursor.execute(delete_query, (carrier_name))
            conn.commit()
            
            print(f"Carrier '{carrier_name}' deleted from the database.")
            return jsonify({"message": "Carrier deleted successfully"})
        
        except Exception as e:
            conn.rollback()
            print(f"Error deleting carrier '{carrier_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500

@app.route("/api/tools_allocation", methods=["GET", "POST", "DELETE"])
def handle_tools_allocation():
    if request.method == "GET":
        cursor.execute(
            "SELECT TOP (1000)  [name], [position] FROM [Foam_tools].[dbo].[tools_allocation]"
        )
        tool_allocation = [
            dict(zip([column[0] for column in cursor.description], row))
            for row in cursor.fetchall()
        ]
        return jsonify(tool_allocation)

    elif request.method == "POST":
        data = request.get_json()
        tool_name = data.get('name')
        tool_position = data.get('position')
        
        # Ensure your connection and cursor are properly set up
        try:
            cursor.execute("DELETE FROM [Foam_tools].[dbo].[tools_allocation] WHERE name = ?", (tool_name))
        
            # Insert new record
            insert_query = "INSERT INTO [Foam_tools].[dbo].[tools_allocation] ([name], [position]) VALUES (?, ?)"
            cursor.execute(insert_query, (tool_name, tool_position))
            
            print(f"Tool '{tool_name}' added to the database.")
            return jsonify({"message": "Tool added successfully"})
        
        except Exception as e:
            conn.rollback()
            print(f"Error adding tool '{tool_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500


    elif request.method == "DELETE":
        data = request.get_json()
        tool_name = data.get('name')
        
        try:
            # Example SQL delete query
            delete_query = """DELETE FROM [Foam_tools].[dbo].[tools_allocation] WHERE name = ? """
            
            # Execute query with parameter tuple
            cursor.execute(delete_query, (tool_name))
            conn.commit()
            
            print(f"Tool '{tool_name}' deleted from the database.")
            return jsonify({"message": "Tool deleted successfully"})
        
        except Exception as e:
            conn.rollback()
            print(f"Error deleting tool '{tool_name}': {str(e)}")
            return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
