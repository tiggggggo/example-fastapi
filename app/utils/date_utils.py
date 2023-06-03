from datetime import datetime

# The format of the date string "2023-05-28"
QUERY_DAY_FORMAT = "%Y-%m-%d"
QUERY_MONTH_FORMAT = "%Y-%m"


def get_datetime(date_string: str,
                 date_format: str = QUERY_DAY_FORMAT,
                 contract_hour: int = 0) -> datetime:
    result = datetime.strptime(date_string, date_format)
    if contract_hour:
        result = result.replace(hour=contract_hour)
    return result
