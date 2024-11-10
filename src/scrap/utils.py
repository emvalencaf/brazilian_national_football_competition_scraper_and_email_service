def format_date(date_str: str) -> str:
    months = {
        'jan': '01', 'feb': '02', 'mar': '03', 'abr': '04',
        'mai': '05', 'jun': '06', 'jul': '07', 'ago': '08',
        'set': '09', 'out': '10', 'nov': '11', 'dez': '12'
    }
    day, month_abbr, year = date_str.split('.')
    month = months.get(month_abbr[:3].lower())
    return f"{day}/{month}/{year}"