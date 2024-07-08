import sqlite3
import pandas as pd

EXCEL_PATH = "Bases de datos (Test analista de datos).xlsx"

tables_map = {
        "Tabla creditos": "credits",
        "Tabla gestores": "managers",
        "Tabla oficina": "offices"
        }

# conexion sql lite
con = sqlite3.connect("creditos.db")


def read_excel() -> dict:
    """
    Leer archivo fuente
    """
    # leer todas las hojas del excel
    excel_file = pd.read_excel(EXCEL_PATH,
        sheet_name=None)

    excel_file.pop("Ejercicio conocimiento negocio", None)
    return excel_file



def create_tables() -> None:
    """
    crear tablas en base
    """
    with open("esquemas.sql", "r", encoding="utf-8") as sql_file:
        schemas = sql_file.read()
        schemas = schemas.split(";")

    for schema in schemas:
        if schema != "":
            table_name = schema.split(" ")[5].replace('"', "")
            con.execute(f"""DROP TABLE IF EXISTS {table_name};""")
            con.execute(schema)
            print(f"Tabla {table_name} creada con exito")
    con.commit()




def insert_data(dataframe:pd.DataFrame, table_name):
    """
    Insertar df en sqlite
    """
    dataframe.to_sql(name=tables_map[table_name],
              con = con,
              if_exists="append", index=False)
    print("Registros insertados", dataframe.shape[0])



# llenar tablas

if __name__ == "__main__":

    data = read_excel()
    for name, df in data.items():
        print(name)
        insert_data(df, name)
