from datetime import datetime
from typing import Dict

FORMAT = "%Y/%m/%d %H:%M:%S"
NOW_DATE_TIME = datetime.now().strftime(FORMAT)
TABLE_HEADER = [
    ['Отчет от', NOW_DATE_TIME],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]

ROWS = 100
COLUMNS = 4
BODY_TABLE = Dict(
    properties=Dict(
        title=f'Отчет от {NOW_DATE_TIME}',
        locale='ru_RU',
    ),
    sheets=[Dict(properties=Dict(
        sheetType='GRID',
        sheetId=0,
        title='Лист1',
        gridProperties=Dict(
            rowCount=ROWS,
            columnCount=COLUMNS,
        )
    ))]
)
