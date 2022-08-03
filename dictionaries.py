#inside dictionary, there are key and values. keys should be unique.
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "Augest",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",

}

print(monthConversions["Nov"])
print(monthConversions.get("Mar"))
print(monthConversions.get("Sun"))
print(monthConversions.get("Sew", "Not a valid key")) 
