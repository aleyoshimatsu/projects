total_segs = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = total_segs // 86400
segs_restantes = total_segs % 86400
horas = segs_restantes // 3600
segs_restantes = segs_restantes % 3600
minutos = segs_restantes // 60
segundos = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
