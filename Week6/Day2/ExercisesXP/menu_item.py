import psycopg2


class MenuItem:
    __HOSTNAME = "localhost"
    __USERNAME = "anton"
    __PASSWORD = "psqlpass"
    __DATABASE = "menu"

    def __init__(self, name: str, price: int = 0) -> None:
        self.name: str = name
        self.price: int = price

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

    def save(self):
        result = self.run_query(
            f"insert into menu_items (item_name, item_price) values ('{self.name}', {self.price}) returning *;"
        )
        return len(result) > 0

    def delete(self):
        result = self.run_query(
            f"delete from menu_items where item_name = '{self.name}' returning *;"
        )
        return len(result) > 0

    def update(self, name: str | None = None, price: int | None = None):
        if name is None:
            name = self.name
        if price is None:
            price = self.price
        result = self.run_query(
            f"update menu_items set item_name = '{name}', item_price = {price} where item_name = '{self.name}' returning *;"
        )
        self.name = name
        self.price = price

        return len(result) > 0
