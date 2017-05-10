# SmartTime

This program allow small business to have a full-fledged timesheet system at low cost. Basically it offers the ability to employees to use theirs smartphones or desktop to timestamp. The system will record the timestamp and do intergrity and security check on it.

I'm wirting this on free time, but any help is welcome if you have comment or advice or, even better want to contribute.
## Projet  
### Project phases

Phase 1 : Get a demonstration version <- (Current)
Phase 2 : Based on feedback, adapt layout, add/remove features 
Phase 3 : Integration testing 
Phase 4 : Freeze branch 



### Roadmap for initial version
System allows to : 
1. Register devices
2. Manipulate devices
3. Register new users
3. Manipulate users
4. Timestamping with 'web browser'
5. Manipulate timestamps
  1. Manual request (Holiday, sickness, etc..)
6. Detect anomalies (eg. odd number of timestamp, refused timestamps)
7. Manipulate timestamping zones
8. Compute following statistics
  1. Zones where timestamps appears (based on a defined radius) in order
  2. Number of denied timestamps (avg error type)
  3. Avergae of work hours
  4. % timestamp request success / request error 
9. Export 
  1. Employee weekly-monthly-annualy time at work
  2. All company weekly-monthly-annualy time at work


### Roadmap next version

1. Add Android support (Timestamp / get own timesheet on device)
2. LDAP intgration
3. Outlook/Calendar support


# Developpment
## Installation 
This project is based on Django 1.11.1 and python 2.7
