stations = ["North Avenue", "Quezon Avenue", "GMA-Kamuning", "Araneta Center-Cubao", 
            "Santolan-Annapolis", "Ortigas", "Shaw Boulevard", "Boni", "Guadalupe",
            "Buendia", "Ayala", "Magallanes", "Taft Avenue"]

passengers = list(map(int, input().split()))
drop_off = list(map(int, input().split()))

station_idx, p_onboard= 0, 0

for i in range(len(passengers)):
    p_onboard -= drop_off[i]
    p_onboard += passengers[i]
    if p_onboard >= 30:
        p += 1
    else:
        p = 0
    if p >= 2:
        print(stations[station_idx])
        print(p_onboard)
        break

    station_idx += 1

if station_idx == 12:
    print("Taft Avenue")
    print(p_onboard)
