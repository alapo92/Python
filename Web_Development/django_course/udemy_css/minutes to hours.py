minutes = 126
seconds = 150

minutes = minutes + seconds / 60
hours = minutes / 60

RemMinutes = minutes % 60
RemSeconds = seconds % 60

print(int(hours), "hours and ", int(RemMinutes), " minutes and ", RemSeconds, " Seconds")

# print(int(minutes))
