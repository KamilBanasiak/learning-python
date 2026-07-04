distance_mi = 2
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True
if bool(distance_mi) == False:
    print("False")
else:
    if distance_mi <= 1: 
        if is_raining == False:
            print("True")
        else:
            print("False")
    elif distance_mi > 1 and distance_mi <= 6:
        if has_bike and is_raining == False:
            print("True")
        else:
            print("False")
    else:
        if has_car or has_ride_share_app:
            print("True")
        else:
            print("False")