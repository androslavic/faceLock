import dbus
import dbus.mainloop.glib
from gi.repository import GLib

class SessionMonitor:
    def __init__(self, on_unlock_callback):
        self.on_unlock_callback = on_unlock_callback

    def start(self):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SystemBus()
        bus.add_signal_receiver(
            handler_function=self._on_properties_changed,
            signal_name="PropertiesChanged",
            dbus_interface="org.freedesktop.DBus.Properties",
            path_keyword="path"
        )
        print("👀 SessionMonitor running...")
        loop = GLib.MainLoop()
        loop.run()

    def _on_properties_changed(self, interface, changed_properties, invalidated, path=None):

        if interface == "org.freedesktop.login1.Session":
            if "LockedHint" in changed_properties:
                locked = changed_properties["LockedHint"]
                session_id = path.split("/")[-1] if path else "?"
                if locked:
                    print(f"🔒 Session {session_id} locked.")
                else:
                    print(f"🔓 Session {session_id} unlocked. Resetting condition...")
                    self.on_unlock_callback()
