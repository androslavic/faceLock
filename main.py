import dbus
import dbus.mainloop.glib
from gi.repository import GLib

def on_properties_changed(interface, changed_properties, invalidated_properties, path=None):
    # Only interested in session lock/unlock changes
    if interface == "org.freedesktop.login1.Session":
        if "LockedHint" in changed_properties:
            locked = changed_properties["LockedHint"]
            session_id = path.split("/")[-1] if path else "?"
            if locked:
                print(f"🔒 Session {session_id} locked.")
            else:
                print(f"🔓 Session {session_id} unlocked. Resetting condition...")

def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()

    # Listen for all PropertiesChanged signals, and pass object path as 'path'
    bus.add_signal_receiver(
        handler_function=on_properties_changed,
        signal_name="PropertiesChanged",
        dbus_interface="org.freedesktop.DBus.Properties",
        path_keyword="path"
    )

    print("👀 Listening for lock/unlock events from ALL sessions...")
    GLib.MainLoop().run()

if __name__ == "__main__":
    main()
