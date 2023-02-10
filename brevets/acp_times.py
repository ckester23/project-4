"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders

Algorithm
https://rusa.org/pages/acp-brevet-control-times-calculator
"""
import arrow
import math

# If control_dist is longer than brev_dist_km, just use brev_dist_km
# open time is the fastest a person can go
# close time is the slowest a person can go

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.

       34 km/hr max speed 0-200
       ctrl loc.    max sp.   min sp. 
       0-200        34         15 // should we do french for low dists?
       200-400      32         15
       400-600      30         15
       600 - 1000   28         11.428
       1000-1300    26         13.333
   """
   # determine max speed for calculations

   # if control is over brev_dist, use brev_dist-control_dist for 
      # determining max_speed

   max_speed = 0
   if (control_dist_km == 0):
      return brevet_start_time

   if (control_dist_km <= 200):
      max_speed = 34

   elif (control_dist_km <= 400):
      max_speed = 32

   elif (control_dist_km <= 600):
      max_speed= 30

   elif(control_dist_km <= 1000):
      max_speed = 28

   else:
      # error?? only allowed to go up to 1000 km
      max_speed = 26

   temp = control_dist_km / max_speed
   hours = math.floor(temp)
   minutes = (temp - hours) * 60
   # arrow.shift(hours+=blah, minutes=blah)
   # return brev_start.shift(hours=hours, minutes=minutes) something like this
   # arrow.get() string to arrow format
   # arrow.format() arrow to string format

   # first checkpoint is always at 0!

   return arrow.now() # basically dateTime.now() we want to return something else


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
   """
   # for control<= 60: 
      # do control_dist/20 + 1 instead of all the extra stuff

   # control == 0: close time is exactly one hour after brev_start
   # the very last control will return brevet_start_time.shift by a pre-determined amount
   # make a dictionary of the wikipedia values with brevet and final close time

   # if this control is the last checkpoint, return brev_start.shift by specified time
      # last checkpoint can be up to 20% of brev_dist
      # so if control >= brev_dist return brev_start.shift(specified shift by wikipedia)
   min_speed = 0
   if (brevet_dist_km <= 200):
      min_speed = 15

   elif (brevet_dist_km <= 400):
      min_speed = 15

   elif (brevet_dist_km <= 600):
      min_speed= 15

   elif(brevet_dist_km <= 1000):
      min_speed = 11.428

   else:
      min_speed = 13.333

   temp = control_dist_km / min_speed
   hours = math.floor(temp)
   minutes = (temp - hours) * 60

   return arrow.now() # basically dateTime.now() we want to return something else
