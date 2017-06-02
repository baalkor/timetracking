from dashboardView import DashboardView
from zonesEditorView import ZonesEditorView
from zonesView import ZoneView, ZoneDetailView
from userView import NewUserView, ListUsers, DetailUserView
from devicesView import NewDeviceView, ListDeviceView, DeviceDetail, AssignDeviceToZone
from timesheetsView import ManualTimesheetList, TimestampDetail, TimesheetView, TimesheetList
from anonamliesView import AnomaliesView
from agendaView import AgendaView

def inContentAdmin(user):
    if user:
        return user.groups.filter(name='contentadmin').count() == 0
    return False