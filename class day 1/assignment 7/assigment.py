#Ask for the holiday type
holiday_type=input("Do you want to go to a cruise or go to Riyadh for 2 days ")
#Check the first holiday then ask questions
if holiday_type=="cruise":
    cruise_activity=input("Do you want to go swim or catch fish ")
    if cruise_activity=="swim":
        print("Your plan:Go swim in the ocean and rent a jetski")
    else:
        print("Your plan: Go in the ocean and catch fish with a spear")
elif holiday_type=="Riyadh":
    riyadh_activity=input("Do you want to go to a mall or go or visit your friends")
    if riyadh_activity=="Mall":
        print("Your plan: Go with your family to play laser tag and go eat")
    else:
        print("Your plan: Go to your friend's house and play video games and go out to play football")
else:
    if holiday_type!="cruise" and holiday_type!="Riyadh":
        print("Skill issue take it or leave!")