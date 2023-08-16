def calculate_calories(weight, height, age, gender, activity_level, body_fat, goal, health_condition, pregnancy, sports_activity_hours, metabolic_rate, sleep_hours):
    # Berechnung des Basal Metabolic Rate (BMR)
    if gender.lower() == "männlich":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == "weiblich":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Ungültiges Geschlecht. Bitte geben Sie 'männlich' oder 'weiblich' ein.")

    # Berücksichtigung des Körperfettanteils (optional)
    if body_fat:
        if gender.lower() == "männlich":
            bmr *= (1 - body_fat / 100)
        elif gender.lower() == "weiblich":
            bmr *= (1 - body_fat / 100)

    # Berücksichtigung des Ziels (Gewichtsabnahme, Gewichtszunahme oder Gewichtserhaltung)
    if goal.lower() == "gewichtsabnahme":
        bmr *= 0.85
    elif goal.lower() == "gewichtszunahme":
        bmr *= 1.15

    # Berücksichtigung des Gesundheitszustands (optional)
    if health_condition.lower() == "gesundheitliche bedingung":
        bmr *= 0.9

    # Berücksichtigung der Schwangerschaft oder Stillzeit (optional)
    if pregnancy.lower() == "schwanger" or pregnancy.lower() == "stillend":
        bmr += 300

    activity_factors = {
        "inaktiv": 1.2,
        "leicht aktiv": 1.375,
        "mäßig aktiv": 1.55,
        "sehr aktiv": 1.725,
        "extrem aktiv": 1.9
    }

    if activity_level.lower() not in activity_factors:
        raise ValueError("Ungültiger Aktivitätsgrad. Bitte wählen Sie 'inaktiv', 'leicht aktiv', 'mäßig aktiv', 'sehr aktiv' oder 'extrem aktiv'.")

    total_calories = bmr * activity_factors[activity_level.lower()]

    # Berücksichtigung der sportlichen Aktivitäten (optional)
    if sports_activity_hours:
        total_calories += sports_activity_hours * 1  # Beispiel: Annahme, dass jede Stunde Sport 5 zusätzliche Kalorien pro Stunde verbrennt

    # Berücksichtigung der individuellen Stoffwechselrate (optional)
    if metabolic_rate:
        total_calories += metabolic_rate  # Beispiel: Annahme, dass der Stoffwechsel 100 zusätzliche Kalorien verbrennt

    # Berücksichtigung der Schlafstunden (optional)
    if sleep_hours:
        total_calories -= sleep_hours * 1.1  # Beispiel: Annahme, dass jede Schlafstunde 1,2 Kalorien weniger verbraucht

    # Berücksichtigung von Makronährstoffen
    # Beispiel: Annahme, dass für jede 1 g Protein und Kohlenhydrate 4 Kalorien und für 1 g Fett 9 Kalorien berechnet werden
    protein_grams = weight * 2.2 * 1.2
    carbohydrate_grams = weight * 2.2 * 1.5
    fat_grams = (total_calories - (protein_grams * 4 + carbohydrate_grams * 4)) / 9
    total_calories += protein_grams * 4 + carbohydrate_grams * 4 + fat_grams * 9

    # Anpassung an individuelle Ziele
    if goal.lower() == "muskelaufbau":
        total_calories += 200  # Beispiel: Annahme, dass beim Muskelaufbau 200 zusätzliche Kalorien benötigt werden
    elif goal.lower() == "fettverlust":
        total_calories -= 300  # Beispiel: Annahme, dass beim Fettverlust 300 Kalorien eingespart werden müssen

    # Berücksichtigung von Mahlzeiten und Snacks
    # Beispiel: Annahme, dass 3 Hauptmahlzeiten und 2 Snacks pro Tag den Kalorienbedarf um 100 Kalorien erhöhen
    total_calories += 100

    # Erfassung von Aktivitäten und Bewegungsmustern
    # Beispiel: Annahme, dass sitzende Tätigkeiten den Kalorienbedarf um 100 Kalorien reduzieren und stehende Tätigkeiten den Bedarf um 50 Kalorien erhöhen
    total_calories += (activity_factors[activity_level.lower()] - 1) * 100

    # Berücksichtigung des Klimas und der Umgebung
    # Beispiel: Annahme, dass kalte Umgebungen den Kalorienbedarf um 50 Kalorien erhöhen
    total_calories += 50

    return total_calories

def main():
    print("Willkommen zum Kalorienrechner!")
    weight = float(input("Bitte geben Sie Ihr Gewicht in Kilogramm ein: "))
    height = float(input("Bitte geben Sie Ihre Größe in Zentimetern ein: "))
    age = int(input("Bitte geben Sie Ihr Alter ein: "))
    gender = input("Bitte geben Sie Ihr Geschlecht (männlich/weiblich) ein: ")
    activity_level = input("Bitte geben Sie Ihren Aktivitätsgrad ein (inaktiv/leicht aktiv/mäßig aktiv/sehr aktiv/extrem aktiv): ")
    body_fat = float(input("Bitte geben Sie Ihren Körperfettanteil in Prozent ein (optional, falls nicht bekannt einfach Enter drücken): ") or 0)
    goal = input("Bitte geben Sie Ihr Ziel ein (Gewichtsabnahme/Gewichtszunahme/Gewichtserhaltung/Muskelaufbau/Fettverlust): ")
    health_condition = input("Haben Sie eine gesundheitliche Bedingung, die Ihren Kalorienbedarf beeinflusst? (ja/nein): ")
    pregnancy = input("Befinden Sie sich in der Schwangerschaft oder Stillzeit? (ja/nein): ")
    sports_activity_hours = float(input("Bitte geben Sie die Anzahl der Stunden sportlicher Aktivitäten pro Tag ein (optional, falls nicht bekannt einfach Enter drücken): ") or 0)
    metabolic_rate = float(input("Bitte geben Sie eine grobe Schätzung Ihrer individuellen Stoffwechselrate in Kalorien pro Tag ein (optional, falls nicht bekannt einfach Enter drücken): ") or 0)
    sleep_hours = float(input("Bitte geben Sie die Anzahl der Stunden Schlaf pro Tag ein (optional, falls nicht bekannt einfach Enter drücken): ") or 0)

    try:
        daily_calories = calculate_calories(weight, height, age, gender, activity_level, body_fat, goal, health_condition, pregnancy, sports_activity_hours, metabolic_rate, sleep_hours)
        print("Ihr täglicher Kalorienbedarf beträgt:", round(daily_calories, 2), "Kalorien.")
    except ValueError as e:
        print("Fehler:", str(e))

if __name__ == "__main__":
    main()
