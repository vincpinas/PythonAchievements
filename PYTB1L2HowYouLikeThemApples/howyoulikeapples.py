totaalbomen = 333
schaduwbomen = totaalbomen / 3 * 2
zonbomen = totaalbomen / 3 * 1
zonappels = 146
schaduwappels = zonappels / 10 * 8
totaalappels = zonappels * zonbomen + schaduwbomen * schaduwappels
appelsverkopen = totaalappels / 4
print("Totaals appels: ", totaalappels)
print("Appels die ik mag verkopen: ", appelsverkopen)