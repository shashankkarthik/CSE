cycle_hr = float(input("Enter the number of hours cycling: "))
running_hr = float(input("Enter the number of hours running: "))
swim_hr = float(input("Enter the number of hours swimming: "))

cal_burn = (200*cycle_hr) + (475*running_hr) + (275*swim_hr)

weight_loss = cal_burn/3500

print("Weight loss:", weight_loss,"pounds")
