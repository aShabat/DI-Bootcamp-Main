import psycopg2
from menu_item import MenuItem  # pyright: ignore[reportImplicitRelativeImport]


class MenuManager:
    __HOSTNAME = "localhost"
    __USERNAME = "anton"
    __PASSWORD = "psqlpass"
    __DATABASE = "menu"

    def run_query(self, query: str):
        connection = psycopg2.connect(
            host=self.__HOSTNAME,
            user=self.__USERNAME,
            password=self.__PASSWORD,
            dbname=self.__DATABASE,
        )

        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        connection.commit()
        connection.close()

        return results

    def get_by_name(self, name: str):
        query_result = self.run_query(
            f"select item_name, item_price from menu_items where item_name = '{name}';"
        )
        if len(query_result) > 0:
            return MenuItem(name=query_result[0][0], price=query_result[0][1])
        else:
            return None

    def all_items(self):
        query_result = self.run_query(f"select item_name, item_price from menu_items")
        return [MenuItem(name=item[0], price=item[1]) for item in query_result]
