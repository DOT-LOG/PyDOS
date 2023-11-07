import os
import shutil
import random
import subprocess
import platform
import datetime
import psutil
import getpass

class SimpleDOS:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.user = getpass.getuser()
        self.available_commands = {
            "dir": self.list_directory,
            "cd": self.change_directory,
            "cls": self.clear_screen,
            "type": self.display_file_contents,
            "edit": self.edit_file,
            "create": self.create_file,
            "mkdir": self.create_directory,
            "del": self.delete_file,
            "rmdir": self.delete_directory,
            "copy": self.copy,
            "move": self.move,
            "rename": self.rename,
            "calc": self.open_calculator,
            "notepad": self.open_notepad,
            "run": self.run_program,
            "random": self.random_number,
            "time": self.display_current_time,
            "date": self.display_current_date,
            "ipconfig": self.display_ip_config,
            "help": self.display_help,
            "sac": self.show_all_commands,
            # Additional commands
            "list-drives": self.list_drives,
            "system-info": self.display_system_info,
            "tree": self.display_directory_tree,
            "find": self.find_files,
            "echo": self.echo,
            "shutdown": self.shutdown_system,
            "restart": self.restart_system,
            "hibernate": self.hibernate_system,
            "suspend": self.suspend_system,
            "uptime": self.display_system_uptime,
            "clear-cache": self.clear_system_cache,
            "list-users": self.list_users,
            "list-groups": self.list_groups,
            "list-processes": self.list_processes,
            "kill": self.kill_process,
            "memory-info": self.display_memory_info,
            "disk-space": self.display_disk_space,
            "list-services": self.list_services,
            "start-service": self.start_service,
            "stop-service": self.stop_service,
            "list-network-interfaces": self.list_network_interfaces,
            "list-ports": self.list_ports,
            "list-tasks": self.list_tasks,
            "list-registry-keys": self.list_registry_keys,
            "list-environment-variables": self.list_environment_variables,
        }

    def run(self):
        while True:
            command = input(f"{self.user}@PY-DOS:{self.current_directory}> ").strip()
            if command.lower() == "exit":
                print("Exiting PY-DOS.")
                break
            self.execute_command(command)

    def execute_command(self, command):
        parts = command.split(" ", 1)
        base_command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        if base_command in self.available_commands:
            self.available_commands[base_command](args)
        else:
            print(f"'{base_command}' is not recognized as an internal or external command. Type 'help' for a list of commands.")

    def list_directory(self, _):
        files = os.listdir(self.current_directory)
        for file in files:
            print(file)

    def change_directory(self, args):
        new_path = os.path.join(self.current_directory, args)
        if os.path.exists(new_path) and os.path.isdir(new_path):
            self.current_directory = new_path
        else:
            print(f"The system cannot find the path specified: {args}")

    def clear_screen(self, _):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_file_contents(self, args):
        file_path = os.path.join(self.current_directory, args)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                print(file.read())
        else:
            print(f"File not found: {args}")

    def edit_file(self, args):
        file_path = os.path.join(self.current_directory, args)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.system(f"notepad {file_path}" if os.name == 'nt' else f"nano {file_path}")
        else:
            print(f"File not found: {args}")

    def create_file(self, args):
        file_path = os.path.join(self.current_directory, args)
        if not os.path.exists(file_path):
            with open(file_path, 'w'):
                pass
        else:
            print(f"File already exists: {args}")

    def create_directory(self, args):
        dir_path = os.path.join(self.current_directory, args)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        else:
            print(f"Directory already exists: {args}")

    def delete_file(self, args):
        file_path = os.path.join(self.current_directory, args)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.remove(file_path)
        else:
            print(f"File not found: {args}")

    def delete_directory(self, args):
        dir_path = os.path.join(self.current_directory, args)
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            os.rmdir(dir_path)
        else:
            print(f"Directory not found: {args}")

    def copy(self, args):
        source, destination = args.split()
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)
        else:
            print(f"Source file not found: {source}")

    def move(self, args):
        source, destination = args.split()
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            print(f"Source file not found: {source}")

    def rename(self, args):
        source, destination = args.split()
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.exists(source_path):
            os.rename(source_path, destination_path)
        else:
            print(f"Source file not found: {source}")

    def open_calculator(self, _):
        os.system("calc" if os.name == 'nt' else "gnome-calculator")

    def open_notepad(self, _):
        os.system("notepad" if os.name == 'nt' else "gedit")

    def run_program(self, args):
        try:
            subprocess.run(args, shell=True, check=True)
        except subprocess.CalledProcessError:
            print(f"Error running program: {args}")

    def random_number(self, _):
        print(f"Random Number: {random.randint(1, 100)}")

    def display_current_time(self, _):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")

    def display_current_date(self, _):
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        print(f"Current Date: {current_date}")

    def display_ip_config(self, _):
        if os.name == 'nt':
            ip_config = subprocess.check_output("ipconfig", shell=True, text=True)
        else:
            ip_config = subprocess.check_output("ifconfig", shell=True, text=True)
        print(ip_config)

    def display_help(self, _):
        print("Available Commands:")
        for command, description in self.available_commands.items():
            print(f"{command} - {description}")

    def show_all_commands(self, _):
        print("Available Commands:")
        for command in self.available_commands:
            print(command)

    # Additional commands start here
    def list_drives(self, _):
        drives = [f"{drive}:\\" for drive in range(ord('A'), ord('Z') + 1) if os.path.exists(f"{chr(drive)}:\\")]
        print("Available Drives:")
        for drive in drives:
            print(drive)

    def display_system_info(self, _):
        system_info = platform.uname()
        print("System Information:")
        print(f"System: {system_info.system}")
        print(f"Node Name: {system_info.node}")
        print(f"Release: {system_info.release}")
        print(f"Version: {system_info.version}")
        print(f"Machine: {system_info.machine}")
        print(f"Processor: {system_info.processor}")

    def display_directory_tree(self, args):
        try:
            os.system(f"tree {args}" if os.name == 'nt' else f"find {args}")
        except:
            print(f"Error displaying tree for directory: {args}")

    def find_files(self, args):
        try:
            os.system(f"dir /s /b /a-d | findstr /i {args}" if os.name == 'nt' else f"find {self.current_directory} -type f -iname '*{args}*' -print")
        except:
            print(f"Error searching for files with query: {args}")

    def echo(self, message):
        print(message)

    def shutdown_system(self, _):
        os.system("shutdown /s /t 0" if os.name == 'nt' else "shutdown -h now")

    def restart_system(self, _):
        os.system("shutdown /r /t 0" if os.name == 'nt' else "reboot")

    def hibernate_system(self, _):
        os.system("shutdown /h" if os.name == 'nt' else "systemctl hibernate")

    def suspend_system(self, _):
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0" if os.name == 'nt' else "systemctl suspend")

    def display_system_uptime(self, _):
        uptime = None
        if os.name == 'nt':
            try:
                uptime = subprocess.check_output("systeminfo | findstr /i 'boot time'", shell=True, text=True)
            except:
                pass
        else:
            try:
                with open("/proc/uptime", "r") as uptime_file:
                    uptime_seconds = float(uptime_file.readline().split()[0])
                    uptime = str(datetime.timedelta(seconds=uptime_seconds))
            except:
                pass
        if uptime:
            print(f"System Uptime: {uptime}")
        else:
            print("Unable to retrieve system uptime information.")

    def clear_system_cache(self, _):
        if os.name == 'nt':
            os.system("ipconfig /flushdns")
        else:
            os.system("sync && echo 3 | sudo tee /proc/sys/vm/drop_caches")

    def list_users(self, _):
        users = None
        if os.name == 'nt':
            try:
                users = subprocess.check_output("net user", shell=True, text=True)
            except:
                pass
        else:
            try:
                users = subprocess.check_output("cat /etc/passwd", shell=True, text=True)
            except:
                pass
        if users:
            print("User Accounts:")
            print(users)
        else:
            print("Unable to list user accounts.")

    def list_groups(self, _):
        groups = None
        if os.name == 'nt':
            try:
                groups = subprocess.check_output("net localgroup", shell=True, text=True)
            except:
                pass
        else:
            try:
                groups = subprocess.check_output("cat /etc/group", shell=True, text=True)
            except:
                pass
        if groups:
            print("User Groups:")
            print(groups)
        else:
            print("Unable to list user groups.")

    def list_processes(self, _):
        processes = None
        if os.name == 'nt':
            try:
                processes = subprocess.check_output("tasklist", shell=True, text=True)
            except:
                pass
        else:
            try:
                processes = subprocess.check_output("ps aux", shell=True, text=True)
            except:
                pass
        if processes:
            print("Running Processes:")
            print(processes)
        else:
            print("Unable to list running processes.")

    def kill_process(self, args):
        if os.name == 'nt':
            try:
                os.system(f"taskkill /F /PID {args}")
            except:
                print(f"Error terminating process with PID: {args}")
        else:
            try:
                os.system(f"kill {args}")
            except:
                print(f"Error terminating process with PID: {args}")

    def display_memory_info(self, _):
        memory_info = None
        if os.name == 'nt':
            try:
                memory_info = subprocess.check_output("systeminfo | findstr /i 'total physical memory'", shell=True, text=True)
            except:
                pass
        else:
            try:
                memory_info = subprocess.check_output("free -h", shell=True, text=True)
            except:
                pass
        if memory_info:
            print("Memory Information:")
            print(memory_info)
        else:
            print("Unable to retrieve memory information.")

    def display_disk_space(self, _):
        disk_space = None
        if os.name == 'nt':
            try:
                disk_space = subprocess.check_output("wmic logicaldisk get deviceid,freespace,size", shell=True, text=True)
            except:
                pass
        else:
            try:
                disk_space = subprocess.check_output("df -h", shell=True, text=True)
            except:
                pass
        if disk_space:
            print("Disk Space Usage:")
            print(disk_space)
        else:
            print("Unable to retrieve disk space information.")

    def list_services(self, _):
        services = None
        if os.name == 'nt':
            try:
                services = subprocess.check_output("net start", shell=True, text=True)
            except:
                pass
        else:
            try:
                services = subprocess.check_output("systemctl list-units --type=service --all", shell=True, text=True)
            except:
                pass
        if services:
            print("System Services:")
            print(services)
        else:
            print("Unable to list system services.")

    def start_service(self, args):
        if os.name == 'nt':
            try:
                os.system(f"net start {args}")
            except:
                print(f"Error starting service: {args}")
        else:
            try:
                os.system(f"systemctl start {args}")
            except:
                print(f"Error starting service: {args}")

    def stop_service(self, args):
        if os.name == 'nt':
            try:
                os.system(f"net stop {args}")
            except:
                print(f"Error stopping service: {args}")
        else:
            try:
                os.system(f"systemctl stop {args}")
            except:
                print(f"Error stopping service: {args}")

    def list_network_interfaces(self, _):
        network_interfaces = None
        if os.name == 'nt':
            try:
                network_interfaces = subprocess.check_output("ipconfig", shell=True, text=True)
            except:
                pass
        else:
            try:
                network_interfaces = subprocess.check_output("ifconfig", shell=True, text=True)
            except:
                pass
        if network_interfaces:
            print("Network Interfaces:")
            print(network_interfaces)
        else:
            print("Unable to list network interfaces.")

    def list_ports(self, _):
        ports = None
        if os.name == 'nt':
            try:
                ports = subprocess.check_output("netstat -ano", shell=True, text=True)
            except:
                pass
        else:
            try:
                ports = subprocess.check_output("ss -tuln", shell=True, text=True)
            except:
                pass
        if ports:
            print("Open Network Ports:")
            print(ports)
        else:
            print("Unable to list open network ports.")

    def list_tasks(self, _):
        tasks = None
        if os.name == 'nt':
            try:
                tasks = subprocess.check_output("schtasks", shell=True, text=True)
            except:
                pass
        else:
            try:
                tasks = subprocess.check_output("crontab -l", shell=True, text=True)
            except:
                pass
        if tasks:
            print("Scheduled Tasks:")
            print(tasks)
        else:
            print("Unable to list scheduled tasks.")

    def list_registry_keys(self, _):
        registry_keys = None
        if os.name == 'nt':
            try:
                registry_keys = subprocess.check_output("reg query HKLM", shell=True, text=True)
            except:
                pass
        if registry_keys:
            print("Registry Keys:")
            print(registry_keys)
        else:
            print("Registry keys are not supported on this platform.")

    def list_environment_variables(self, _):
        environment_variables = os.environ
        print("Environment Variables:")
        for var, value in environment_variables.items():
            print(f"{var}={value}")

if __name__ == "__main__":
    dos = SimpleDOS()
    dos.run()
