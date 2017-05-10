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
*. Register devices
*. Manipulate devices
*. Register new users
*. Manipulate users
*. Timestamping with 'web browser'
*. Manipulate timestamps
..* Manual request (Holiday, sickness, etc..)
*. Detect anomalies (eg. odd number of timestamp, refused timestamps)
*. Manipulate timestamping zones
*. Compute following statistics
..* Zones where timestamps appears (based on a defined radius) in order
..* Number of denied timestamps (avg error type)
..* Avergae of work hours
..* % timestamp request success / request error 
*. Export 
..* Employee weekly-monthly-annualy time at work
..* All company weekly-monthly-annualy time at work


### Roadmap next version

*. Add Android support (Timestamp / get own timesheet on device)
*. LDAP intgration
*. Outlook/Calendar support


# Developpment
## Installation 
This project is based on Django 1.11.1 and python 2.7
