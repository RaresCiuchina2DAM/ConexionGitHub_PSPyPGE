from util import logcfg
import logging
import asyncpg
import asyncio
from datetime import datetime
import json


async def main():
    # CREAMOS LA CONEXION A LA BASE DE DATOS DE ODOO UTILIZANDO LA DIRECCION EL PUERTO Y LA CONTRASEÑA
    connection = await asyncpg.connect(
        # ASIGNAMOS LA IP
        host='192.168.56.207',
        # ASIGNAMOS EL PUERTO
        port=5432,
        # ASIGNAMOS
        user='odoo',
        database='Enero',
        password='odoo')

    # CREAMOS LA SENTENCIA DE SELECCION CON ALIAS
    brand_query = 'SELECT res_country.name as pais,' \
                  ' res_currency.name as moneda, ' \
                  'res_currency.symbol as ' \
                  'simbolo FROM res_country JOIN res_currency ' \
                  'ON res_country.currency_id = res_currency.id'

    # RECOGEMOS EL SELECT EN LA VARIABLE RESULTS
    results = await connection.fetch(brand_query)

    # CON EL FICHERO CONSULTAS.CSV ABIERTO EN MODO ESCRITURA:
    with open('consultas.csv', "w", encoding='utf-8') as f:
        for brand in results:
            # GUARDAMOS EL PAIS Y LO METEMOS EN UN JSON PARA PODER TRABAJAR CON ELLO
            a = brand['pais']
            pdict = json.loads(a)

            # EN CASO DE QUE SEA ES_ES PONDREMOS ES_ES,
            # SI ES EN_US PONDREMOS EN_US Y SINO,
            # PONDREMOS DESCONOCIDO
            if 'es_ES' in pdict.keys():
                nombre = pdict['es_ES']
            elif 'en_US' in pdict.keys():
                nombre = pdict['en_US']
            else:
                nombre = "Desconocido"

            # ESCRIBIMOS EN EL FICHERO LA LINEA RECOGIDA
            f.write(f" {nombre}; "
                    f" {brand['moneda']};"
                    f" {brand['simbolo']}\n")

    # CERRAMOS LA CONEXIÓN
    await connection.close()


if __name__ == "__main__":
    stime = datetime.now()
    logcfg(__file__)
    asyncio.run(main())
    logging.info(f"El programa ha tardado {datetime.now() - stime}")
