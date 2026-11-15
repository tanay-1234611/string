def convert_date(date_str):
    """Convert a date string from 'YYYY-MM-DD' format to 'DD/MM/YYYY' format."""
    try:
        year, month, day = date_str.split('-')
        return f"{day}/{month}/{year}"
    except ValueError:
        raise ValueError("Date must be in 'YYYY-MM-DD' format.")