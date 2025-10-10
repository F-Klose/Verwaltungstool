from datetime import datetime, timedelta

def get_num_days_in_month(year, month):
    """Die Funktion berechnet die Tage eines Monats,
       indem sie einfach den Unterschied zwischen dem ersten Tag des nächsten Monats und dem ersten Tag des aktuellen Monats nimmt.
       Dadurch müssen wir nicht extra prüfen, wie viele Tage jeder Monat hat oder ob Schaltjahre vorliegen – das erledigt Python automatisch.
       
    Args:
        year (int): Das Jahr, z. B. 2025
        month (int): Der Monat als Zahl von 1 (Januar) bis 12 (Dezember)

    Returns:
        int: Die Anzahl der Tage in diesem Monat (28–31)

    Beispiel:
        >>> get_num_days_in_month(2024, 2)
        29  # 2024 ist ein Schaltjahr
        >>> get_num_days_in_month(2025, 4)
        30
    """
       
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    return (next_month - datetime(year, month, 1)).days